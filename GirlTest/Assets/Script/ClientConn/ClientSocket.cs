using System;
using System.Net.Sockets;
using System.Net;
using System.Collections.Generic;
using System.Threading;
using UnityEngine;
using System.Text;
using System.Collections;
using UnityEngine.SceneManagement;

public class ClientSocket
{
	// Socket
	private Socket socket;
	// Message container
	public List<string> messageList;
	// Singleton instance
	private static ClientSocket instance;
	// Connect success
	public static bool success;

	// Get instance
	public static ClientSocket GetInstance(){
		if(instance == null){
			instance = new ClientSocket();
		}
		if (!instance.IsConnected ()) {
			instance.Init ();
		}			
		return instance;
	}

	~ClientSocket (){
		Close ();
	}

	// Constructor
	ClientSocket (){
		Init ();
	}

	// Init
	public void Init(){
		// Create socket
		socket = new Socket (AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
		// Server ip and port
		IPAddress ipAddress = IPAddress.Parse("127.0.0.1");
		IPEndPoint ipEndPoint = new IPEndPoint (ipAddress, 6500);
		// Asynchronous connection
		IAsyncResult result = socket.BeginConnect(ipEndPoint, null, socket);
		// Check result
		success = result.AsyncWaitHandle.WaitOne(5000, true);
		if (!success) {
			MessageTip.SetTip ("Connect time out!");    
			Close ();
		} else if (!socket.Connected) {
			// Failed to connect server
			MessageTip.SetTip ("Failed to connect server!");  
		} else{
			// Start thread
			messageList = new List<string>();
			Thread thread = new Thread (new ThreadStart (ReceiveMessage));
			thread.IsBackground = true;
			thread.Start ();
		}
	}

	// Receive message from server
	private void ReceiveMessage(){
		string s = "";
		if (!socket.Connected) {
			// Failed to connect server
			MessageTip.SetTip ("Failed to connect server!");  
			Close ();
			return;
		}
		try {
			Byte[] buf = new byte[4096];
			int len = 0;
			int index = 0;
			string tmp;
			// Wait to receive message
			while((len = socket.Receive (buf))>0){				
				s += Encoding.Default.GetString(buf, 0, len); 
				Array.Clear(buf, 0, 4096);
				while(s.Contains(BaseMessage.END_MARK)){
					index = s.IndexOf(BaseMessage.END_MARK);
					tmp = s.Substring(0, index);
					Debug.Log("Receive message from server: "+tmp);  
					AddMessageList(tmp);
					s = s.Substring(index+BaseMessage.END_MARK.Length);
				}
			}
		} catch (Exception e) {
			MessageTip.SetTip (e.ToString());
			Close ();
			return;
		}
	}

	// Send message to server
	public void SendMessage(String json){
		byte[] msg = Encoding.UTF8.GetBytes(json);     
		Debug.Log("Send message to server: "+json);   
		if(!socket.Connected)     
		{     
			Close(); 
			MessageTip.SetTip ("Failed to connect server!");  
			return;     
		}     
		try  
		{     
			//int i = clientSocket.Send(msg);     
			IAsyncResult asyncSend = socket.BeginSend (msg,0,msg.Length,SocketFlags.None, null, socket);     
			bool success = asyncSend.AsyncWaitHandle.WaitOne( 5000, true );     
			if ( !success )     
			{     
				Close();  
				MessageTip.SetTip ("Failed to connect server!"); 
			}     
		}     
		catch  
		{     
			MessageTip.SetTip ("Send message error!");      
		}     
	}

	// Close
	public void Close(){
		if (socket != null && socket.Connected) {
			socket.Shutdown (SocketShutdown.Both);
			socket.Close ();
		}
		socket = null;
	}

	// Is connected
	public bool IsConnected(){
		return socket!=null && socket.Connected;
	}

	// Add message list
	private void AddMessageList(string message){
		if(Monitor.TryEnter (this)) {
			if(messageList != null)
				messageList.Add (message);
			Monitor.Exit (this);
		}
	}

	// Pop message list
	public string PopMessageList(){
		if(Monitor.TryEnter (this)) {
			if (messageList!=null && messageList.Count > 0) {
				string message = messageList [0];
				messageList.RemoveAt (0);
				Monitor.Exit (this);
				return message;
			}
			Monitor.Exit (this);
			return null;
		}
		return null;
	}

	// Get register and login message
	public SystemMessageFromServer GetSystemMessage(int squence_id){
		if(Monitor.TryEnter (this)) {
			if (messageList != null) {
				foreach (string message in messageList) {
					BaseMessage bm = JsonUtility.FromJson<BaseMessage> (message);
					if (bm.target_type==MessageConstant.TargetType.SYSTEM.GetHashCode()) {
						SystemMessageFromServer ralbm = JsonUtility.FromJson<SystemMessageFromServer> (message);
						if (ralbm.sequence_id == squence_id) {
							messageList.Remove (message);
							Monitor.Exit (this);
							return ralbm;
						}
					}
				}
			}
		}
		Monitor.Exit (this);
		return null;
	}
}
