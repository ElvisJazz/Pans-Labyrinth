//
// Control cameral
// 
// 2016/05/06 Elvis Jia
//
using UnityEngine;
using UnityEngine.UI;
using System.Collections;


public class CameraController : MonoBehaviour
{
	public float Smooth = 3f;		// Smoothing degree
	public float MinView = -40f; // Minimum degree of view around the x axis
	public float MaxView = 45f; // Maximum degree of view around the x axis
	public Text AimText; // Display the aim symbol
	public float SwitchViewDelay = 0.8f; // Delay in switching view
	float cTime; // Current passed time 

	Transform thirdPos;			// The third person position for the camera, specified by a transform in the game
	Transform firstPos;			// The first person position for the camera
	Transform frontPos;			// Front camera locater

	bool useFirstview = false;	// Change Camera Position to first person view

	GameObject[] mainPlayerBody; // Main player body
	GameObject weaponPart = null; // Part of weapon, include the arm

	WeaponInfoController weaponInfoController; // Weapon info controller script

	public Transform FirstPos{ get { return firstPos; } }

	void Start(){
		// Init each position
		if(GameObject.Find ("ThirdPos"))
			thirdPos = GameObject.Find ("ThirdPos").transform;
		if(GameObject.Find ("FirstPos"))
			firstPos = GameObject.Find ("FirstPos").transform;
		if(GameObject.Find ("FrontPos"))
			frontPos = GameObject.Find ("FrontPos").transform;
		// Get main body of the player
		mainPlayerBody = GameObject.FindGameObjectsWithTag ("Player");
		// Get weapon info controller script
		weaponInfoController = GameObject.Find("InfoManager").GetComponent<WeaponInfoController>();
		// Set usual position
		SetCameraPositionNormalView ();
	}

	void FixedUpdate ()	{
		cTime += Time.deltaTime;
		if (Input.GetButton ("Fire2") && cTime>SwitchViewDelay) {	// Alt to change first view camera	
			useFirstview = !useFirstview;
			cTime = 0;
		}

		if (useFirstview) {
			SetCameraPositionFirstView ();
		} else {
			SetCameraPositionNormalView ();
		}
	}

	// Set usual view
	public void SetCameraPositionNormalView(){
		SetMainBodyVisible (true);
		SetWeaponPartVisible (false);
		weaponInfoController.SetWeaponInfoVisible (false);
		transform.position = thirdPos.position;	
		transform.forward = thirdPos.forward;
		AimText.enabled = false;
	}

	// Change first person view
	void SetCameraPositionFirstView(){
		SetMainBodyVisible (false);
		SetWeaponPartVisible (true);
		weaponInfoController.SetWeaponInfoVisible (true);
		transform.position = firstPos.position;	
		transform.forward = firstPos.forward;
		AimText.enabled = true;

	}

	// Change jump camera
	void SetCameraPositionJumpView()
	{
		transform.position = Vector3.Lerp(transform.position, thirdPos.position, Time.fixedDeltaTime * Smooth);	
		transform.forward = Vector3.Lerp(transform.forward, thirdPos.forward, Time.fixedDeltaTime * Smooth);		
	}

	// Change front camera
	void SetCameraPositionFrontView()
	{
		transform.position = Vector3.Lerp(transform.position, frontPos.position, Time.fixedDeltaTime * Smooth);	
		transform.forward = Vector3.Lerp(transform.forward, frontPos.forward, Time.fixedDeltaTime * Smooth);		
	}

	// Rotate camera eulerAngle degrees around the x aixs
	public void RotateCameraByXAxis(float eulerAngle)
	{
		Transform transform = useFirstview ? firstPos : thirdPos;
		eulerAngle += transform.rotation.eulerAngles.x;

		if (eulerAngle > 180)
			eulerAngle -= 360;
		
		eulerAngle = Mathf.Clamp (eulerAngle, MinView, MaxView);

		transform.rotation = Quaternion.Euler(eulerAngle, transform.rotation.eulerAngles.y, transform.rotation.eulerAngles.z);
	}

	// Make main body visible or invisble
	void SetMainBodyVisible(bool visible){
		if (mainPlayerBody != null) {
			foreach (GameObject body in mainPlayerBody) {
				body.SetActive (visible);
			}
		}
	}

	// Make weapon part visible
	void SetWeaponPartVisible(bool visible){
		// Get weapon part
		if (weaponPart == null) {
			weaponPart = GameObject.FindGameObjectWithTag ("WeaponPart");
		}
		if (weaponPart != null) {
			weaponPart.SetActive (visible);
		}
	}
}
