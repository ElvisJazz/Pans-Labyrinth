﻿using System;
using System.Net.Sockets;
using System.Net;
using System.Collections.Generic;
using System.Threading;
using UnityEngine;
using System.Text;
using System.Collections;
using LitJson;

public class ClientSocket
{
	// Socket
	private Socket socket;
	// Message container
	public List<JsonData> messageList;
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
	private void Init(){
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
			messageList = new List<JsonData>();
			Thread thread = new Thread (new ThreadStart (ReceiveMessage));
			thread.IsBackground = true;
			thread.Start ();
		}
	}

	// Receive message from server
	private void ReceiveMessage(){
		string s = "";
		while (true) {
			if (!socket.Connected) {
				// Failed to connect server
				MessageTip.SetTip ("Failed to connect server!");  
				socket.Close ();
				break;
			}
			try {
				Byte[] buf = new byte[4096];
				int len = 0;
				// Wait to receive message
				while((len = socket.Receive (buf))>0){
					if (len <= 0) {
						socket.Close ();
						break;
					} else {
						s += Encoding.Default.GetString(buf);   
						Array.Clear(buf, 0, 4096);
						if(s.EndsWith("/$/")){
							s = s.Substring(0, s.Length-3);
							Debug.Log("Receive message from server: "+s);   
							AddMessageList(s);
							break;
						}
					}
				}
			} catch (Exception e) {
				MessageTip.SetTip (e.ToString());
				socket.Close ();
				break;
			}
		}
	}

	// Send message to server
	public void SendMessage(String json){
		byte[] msg = Encoding.UTF8.GetBytes(json);     
		Debug.Log("Send message to server: "+json);   
		if(!socket.Connected)     
		{     
			socket.Close();     
			return;     
		}     
		try  
		{     
			//int i = clientSocket.Send(msg);     
			IAsyncResult asyncSend = socket.BeginSend (msg,0,msg.Length,SocketFlags.None, null, socket);     
			bool success = asyncSend.AsyncWaitHandle.WaitOne( 5000, true );     
			if ( !success )     
			{     
				socket.Close();  
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
		return socket.Connected;
	}

	// Add message list
	private void AddMessageList(string message){
		lock (this) {
			messageList.Add (MessagePacker.unpack(message));
		}
	}

	// Pop message list
	public JsonData PopMessageList(){
		lock (this) {
			if (messageList.Count > 0) {
				JsonData message = messageList [0];
				messageList.RemoveAt (0);
				return message;
			}
			return null;
		}
	}

	// Get specific message
	public JsonData GetMessage(MessagePacker.Type type, MessagePacker.TargetType targetType){
		lock (this) {
			foreach (JsonData data in messageList) {
				if ((int)data ["message_type"] == type.GetHashCode() && (int)data ["target_type"] == targetType.GetHashCode()) {
					messageList.Remove (data);
					return data;
				}
			}
			return null;
		}
	}
}