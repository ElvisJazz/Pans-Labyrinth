//
// Control the player motion
// 
// 2016/05/06 Elvis Jia
//
using UnityEngine;
using System.Collections;

// Require Component
[RequireComponent(typeof (Animator))]
[RequireComponent(typeof (CapsuleCollider))]
[RequireComponent(typeof (Rigidbody))]

public class PlayerMover : MonoBehaviour
{

	public float AnimSpeed = 1.5f;				// Speed of backplay of the animation
	public float LookSmoother = 3.0f;			// A smoothing setting for camera motion
	public bool UseCurves = true;				// Whether to use mecanim curves
	public float UseCurvesHeight = 0.5f;		// CurvesHeight
	public float WalkSpeedRate = 0.5f;			// Make walk slower than run


	public float ForwardSpeed = 7.0f;			// Forward speed
	public float BackwardSpeed = 2.0f;			// Backward speed
	public float SideSpeed = 4.0f;				// Side speed
	public float RotateSpeed = 0.5f;			// Rotation speed
	public float JumpPower = 3.0f; 				// Jump power

	// Boundary of movement
	public Vector3 MinBoundaryPos;
	public Vector3 MaxBoundaryPos;

	private Vector3 velocity;					// Velocity of motion
	// CapsuleCollider and rigidbody
	private CapsuleCollider col= null;
	private Rigidbody rb= null;

	// CapsuleCollider
	private float orgColHeight;
	private Vector3 orgVectColCenter;
	
	private Animator anim= null;						// Animator
	private AnimatorStateInfo currentBaseState;	// Base layer state information
	private GameObject cameraObject= null;			// Camera
	private PlayerHealth playerHealth = null;    // Player health script

		
	// State constant
	public static int idleState = Animator.StringToHash("Base Layer.Idle");
	public static int locoState = Animator.StringToHash("Base Layer.Locomotion");
	public static int jumpState = Animator.StringToHash("Base Layer.Jump");
	public static int restState = Animator.StringToHash("Base Layer.Rest");
//	static int turnLeftState = Animator.StringToHash("Base Layer.TurnLeft");
//	static int turnRightState = Animator.StringToHash("Base Layer.TurnRight");

	void Start ()
	{
		// Get animator
		anim = GetComponent<Animator>();
		// Get player health
		playerHealth = GetComponent<PlayerHealth>();
		// Get capsuleCollider and rigidbody
		col = GetComponent<CapsuleCollider>();
		rb = GetComponent<Rigidbody>();
		// Get camera
		cameraObject = GameObject.FindWithTag("MainCamera");
		// CapsuleCollider
		orgColHeight = col.height;
		orgVectColCenter = col.center;
	}
	

	void FixedUpdate ()
	{
		if (!Cursor.visible && !playerHealth.IsDead) {
			float h = Input.GetAxis ("Horizontal");	
			float v = Input.GetAxis ("Vertical");	
			float mX = Input.GetAxis ("Mouse X");
			float mY = Input.GetAxis ("Mouse Y");

			anim.SetFloat ("Direction", h); 						// Set variable Direction
			anim.speed = AnimSpeed;								//    Set speed of playback of the animator
			currentBaseState = anim.GetCurrentAnimatorStateInfo (0);	// Get current state information of the animator
			rb.useGravity = true;		
			
			// Set velocity and Speed
			velocity = new Vector3 (h, 0, v);	
			velocity = transform.TransformDirection (velocity);
			if (Input.GetKey (KeyCode.LeftShift)) {
				anim.SetFloat ("Speed", v);
			} else {
				anim.SetFloat ("Speed", v * WalkSpeedRate);
				velocity.z *= WalkSpeedRate;
			}
			// Set motion
			if (v > 0.1) {
				velocity.z *= ForwardSpeed;		// go forward
			} else if (v < -0.1) {
				velocity.z *= BackwardSpeed;	// go backward
			}
			// Set side speed
			velocity.x *= SideSpeed;

			// Set jump
			if (Input.GetButtonDown ("Jump")) {	
				if (currentBaseState.fullPathHash == locoState) {
					if (!anim.IsInTransition (0)) {
						rb.AddForce (Vector3.up * JumpPower, ForceMode.VelocityChange);
						anim.SetBool ("Jump", true);		
					}
				}
			}		

			// Set local position 
			Vector3 tmpPos = transform.localPosition + velocity * Time.fixedDeltaTime;
			if (tmpPos.x >= MinBoundaryPos.x && tmpPos.x <= MaxBoundaryPos.x &&
			    tmpPos.y >= MinBoundaryPos.y && tmpPos.y <= MaxBoundaryPos.y &&
			    tmpPos.z >= MinBoundaryPos.z && tmpPos.z <= MaxBoundaryPos.z) {
				transform.localPosition = tmpPos;
			}

			// Control left or right rotation
			transform.Rotate (0, mX * RotateSpeed, 0);	 
			// Control up or down rotation
			cameraObject.GetComponent<CameraController> ().RotateCameraByXAxis (-mY * RotateSpeed);
			//		if (currentBaseState.fullPathHash == idleState) {
			//			if (!anim.IsInTransition (0)) {
			//				if (mY > 0.1) {
			//					anim.SetBool ("TurnLeft", true);
			//				} else if (mY < -0.1) {
			//					anim.SetBool ("TurnRight", true);
			//				}
			//			}
			//		} else if (currentBaseState.fullPathHash == turnLeftState || currentBaseState.fullPathHash == turnRightState) {
			//				if (mY < 0.1 && mY > -0.1) {
			//					anim.SetBool ("TurnRight", false);
			//					anim.SetBool ("TurnLeft", false);
			//				}
			//		}

			// Handle state of animator
			// Current state is locoState
			if (currentBaseState.fullPathHash == locoState) {
				if (UseCurves) {
					resetCollider ();
				}
			}
			// Current state is jump
			else if (currentBaseState.fullPathHash == jumpState) {
				// Set camera position
				cameraObject.SendMessage ("SetCameraPositionJumpView");
				if (!anim.IsInTransition (0)) {				
					// Use curve to control jump
					if (UseCurves) {
						// Set jump height
						// GravityControl:1⇒No gravity、0⇒Has grvavity
						float jumpHeight = anim.GetFloat ("JumpHeight");
						float gravityControl = anim.GetFloat ("GravityControl"); 
						if (gravityControl > 0)
							rb.useGravity = false;
											
						// Calculate the landing point
						Ray ray = new Ray (transform.position + Vector3.up, -Vector3.up);
						RaycastHit hitInfo = new RaycastHit ();
						// Adjust height and center of collider
						if (Physics.Raycast (ray, out hitInfo)) {
							if (hitInfo.distance > UseCurvesHeight) {
								col.height = orgColHeight - jumpHeight;			
								float adjCenterY = orgVectColCenter.y + jumpHeight;
								col.center = new Vector3 (0, adjCenterY, 0);	
							} else {
								// Reset collider				
								resetCollider ();
							}
						}
					}
					// End jump		
					anim.SetBool ("Jump", false);
				}
			}
			// Current state is idle
			else if (currentBaseState.fullPathHash == idleState) {
				// Rest collider
				if (UseCurves) {
					resetCollider ();
				}
				// Rest state
				if (Input.GetButtonDown ("Jump")) {
					anim.SetBool ("Rest", true);
				}
			}
			// Current state is rest
			else if (currentBaseState.fullPathHash == restState) {
				// End rest state
				if (!anim.IsInTransition (0)) {
					anim.SetBool ("Rest", false);
				}
			}
		}
	}

	void OnGUI()
	{
//		GUI.Box(new Rect(Screen.width -260, 10 ,250 ,150), "Interaction");
//		GUI.Label(new Rect(Screen.width -245,30,250,30),"Up/Down Arrow : Go Forwald/Go Back");
//		GUI.Label(new Rect(Screen.width -245,50,250,30),"Left/Right Arrow : Turn Left/Turn Right");
//		GUI.Label(new Rect(Screen.width -245,70,250,30),"Hit Space key while Running : Jump");
//		GUI.Label(new Rect(Screen.width -245,90,250,30),"Hit Spase key while Stopping : Rest");
//		GUI.Label(new Rect(Screen.width -245,110,250,30),"Left Control : Front Camera");
//		GUI.Label(new Rect(Screen.width -245,130,250,30),"Alt : LookAt Camera");
	}


	// Reset collider
	void resetCollider()
	{
		col.height = orgColHeight;
		col.center = orgVectColCenter;
	}

}
