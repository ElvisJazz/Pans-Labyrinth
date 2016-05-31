//
// Control the weapon
// 
// 2016/05/10 Elvis Jia
//
using System;
using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class WeaponController : MonoBehaviour {

	// Name
	public string WeaponName;
	// Amount of bullets in gun
	public int AmountOfBulletsInGun;
	// Max amount of bullets in gun
	public int MaxAmountOfBulletsInGun;
	// Amount of bullets in the bag
	public int AmountOfBulletsInBag;
	// Max amount of bullets in the bag
	public int MaxAmountOfBulletsInBag;
	// Time of reload
	public float NextReloadTime = 2f;
	// Time between two shoot
	public float NextShootTime = 0.8f;
	// Shaking degrees 
	public float MinFireShakeDegree = 4f;
	public float MaxFireShakeDegree = 5f;
	// Enable shake around y axis
	public bool EnableShakeAroundY = false;
	// Degrees to return original position per fixed frame
	public float DeltaReturnDegree = 0.3f;
	// Reload sound
	public AudioClip ReloadSound;
	// Pull the bolt
	public AudioClip BoltSound;
	// Time between reloading and pulling the bolt
	public float GapTime;

	// Current time of shooting
	float currentShootTime = 0;
	// Current time of reload
	float currentReloadTime = 0;
	// Degrees of shaking around x axis and y axis
	Vector2 shakeDegree;
	// Bullet effect script
	BulletEffect bulletEffect= null;
	// Weapon manager
	WeaponInfoController weaponInfoController = null;
	// Camera controller script
	CameraController cameraController = null;
	// player
	GameObject player = null;
	// Animator of player and weapon
	Animator playerAnim;
	Animator weaponAnim;

	// Reload State
	public static int ReloadState = Animator.StringToHash("Base Layer.Reloads");

	// Use this for initialization
	void Start () {
		shakeDegree = new Vector2 (0, 0);
		weaponAnim = GetComponent<Animator> ();
		GameObject gunBarrierEnd = GameObject.Find ("GunBarrierEnd");
		if (gunBarrierEnd != null) {
			bulletEffect = gunBarrierEnd.GetComponent<BulletEffect> ();
		}
		cameraController = Camera.main.GetComponent<CameraController>();
		player = GameObject.Find ("Player");
		// Set weapon info controller and current weapon
		weaponInfoController = GameObject.Find ("InfoManager").GetComponent<WeaponInfoController>();
		// Get animator
		playerAnim = player.GetComponent<Animator>();
//		GameObject[] weaponPart = GameObject.FindGameObjectsWithTag ("WeaponPart");
//		if (weaponPart != null) {
//			foreach (GameObject weapon in weaponPart) {
//				if (weapon.GetComponent<Animator> () != null) {
//					weaponAnim = weapon.GetComponent<Animator> ();
//				}
//			}
//		}
	}
	
	// Update is called once per frame
	void Update () {
		if (!Cursor.visible) {
			// Fire
			currentShootTime += Time.deltaTime;
			currentReloadTime += Time.deltaTime;
			if (Input.GetButton ("Fire1") && currentShootTime > NextShootTime
			    && !weaponAnim.GetCurrentAnimatorStateInfo (0).IsTag ("Reload")) {
				Fire ();
				currentShootTime = 0;
			}

			// Reload bullets
			if (Input.GetButton ("ReloadBullets") && currentReloadTime > NextReloadTime
			    && !weaponAnim.GetCurrentAnimatorStateInfo (0).IsTag ("Reload")) {
				StartCoroutine (ReloadBullets ());
				currentReloadTime = 0;
			}

			// Set walk state
			SetWeaponWalkState ();
		}
	}

	void FixedUpdate(){
		// Make the camera return to the original position
		if (Mathf.Abs(shakeDegree.x) > 0.0001f || Mathf.Abs(shakeDegree.y) > 0.0001f) {
			ResetCamera ();
		}
	}


	// Set walk state of weapon animator
	void SetWeaponWalkState(){
		if (weaponAnim != null) {
			if (playerAnim.GetCurrentAnimatorStateInfo (0).fullPathHash == PlayerMover.locoState) {
				weaponAnim.SetBool ("Walk", true);
			} else {
				weaponAnim.SetBool ("Walk", false);
			}
		}
	}

	// Fire
	void Fire(){
		if (AmountOfBulletsInGun > 0) {
			// Play fire animation
			if (weaponAnim != null) {
				weaponAnim.SetTrigger("Fire");
				Ray ray = Camera.main.ScreenPointToRay (new Vector3(Screen.width/2, Screen.height/2, 0));
				bulletEffect.StartFire (ray);
				ShakeGun ();
			}
			AmountOfBulletsInGun -= 1;
		} else {
			weaponInfoController.ShowInfo ("The current gun has no bullets !", false);
			StartCoroutine (ReloadBullets());
		}
	}
		
	// Make it seem like shaking the gun by Shaking the camera
	void ShakeGun(){
		int seed = Mathf.RoundToInt (Time.time * 100);
		System.Random random = new System.Random (seed);
		float deltaX = 0, deltaY = 0;
		// Only shake up
		deltaX = (float)(random.NextDouble() * (MaxFireShakeDegree-MinFireShakeDegree) + MinFireShakeDegree);
		shakeDegree.x += deltaX;
		// Shake left or right
		if (EnableShakeAroundY) {
			int t = 1;
			if (seed % 2 == 0) {
				t = -1;
			}
			deltaY = (float)(t * random.NextDouble () * (MaxFireShakeDegree - MinFireShakeDegree) + MinFireShakeDegree);
			shakeDegree.y += deltaY;
		}
		player.transform.Rotate(new Vector3(0, deltaY, 0)); 
		cameraController.RotateCameraByXAxis(-deltaX); 
	}

	// Put the camera to the last position
	void ResetCamera(){
		float deltaMoveDegreeX = 0;
		float deltaMoveDegreeY = 0;
		if (EnableShakeAroundY) {
			if (Mathf.Abs (shakeDegree.y) < DeltaReturnDegree) {
				deltaMoveDegreeY = shakeDegree.y;
				shakeDegree.y = 0;
			} else if (shakeDegree.y > 0) {
				shakeDegree.y -= DeltaReturnDegree;
				deltaMoveDegreeY = DeltaReturnDegree;
			} else {
				shakeDegree.y += DeltaReturnDegree;
				deltaMoveDegreeY = -DeltaReturnDegree;
			}
		}
		if (shakeDegree.x < DeltaReturnDegree) {
			deltaMoveDegreeX = shakeDegree.x;
			shakeDegree.x = 0;
		} else {
			deltaMoveDegreeX = DeltaReturnDegree;
			shakeDegree.x -= DeltaReturnDegree;
		}
		player.transform.Rotate(new Vector3(0, -deltaMoveDegreeY, 0));
		cameraController.RotateCameraByXAxis(deltaMoveDegreeX);
	}

	// ReloadBullets
	IEnumerator ReloadBullets(){
		if (AmountOfBulletsInBag <= 0) {
			weaponInfoController.ShowInfo ("No Bullets in the bag !", true);
		} else if (AmountOfBulletsInGun < MaxAmountOfBulletsInGun) {
			// Play reload animation
			if (weaponAnim != null) {
				// Calculate amount of bullets in the gun and the bag
				int maxReload = MaxAmountOfBulletsInGun - AmountOfBulletsInGun;
				if (maxReload <= AmountOfBulletsInBag) {
					AmountOfBulletsInBag -= maxReload;
					AmountOfBulletsInGun = MaxAmountOfBulletsInGun;
				} else {
					AmountOfBulletsInBag = 0;
					AmountOfBulletsInGun += AmountOfBulletsInBag;
				}
				weaponAnim.SetTrigger ("Reload");
				AudioSource.PlayClipAtPoint (ReloadSound, transform.position);
				if (BoltSound != null) {
					yield return new WaitForSeconds(GapTime);
					AudioSource.PlayClipAtPoint (BoltSound, transform.position);
				}
			}
		} else { // The gun has full bullets
			weaponInfoController.ShowInfo ("The current gun has full bullets !", false);
		}
	}

}
