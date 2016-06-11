//
// Control the bullet effects
// 
// 2016/05/12 Elvis Jia
//
using UnityEngine;
using System.Collections;

public class BulletEffect : MonoBehaviour {
	
	// Bullet damage value
	public int DamageValue = 40;
	// Fire sound
	public AudioClip FireSound;
	// Effect display time
	public float EffectDisplayTime = 0.1f;
	// Shoot distance
	public float ShootDistance = 200f;
	// Enable hit explosion
	public bool EnableHitExplosion = false;
	// Explosion type
	public HitEffects.ExplosionType ExplosionType = HitEffects.ExplosionType.NONE;

	// Shoot flare particle
	ParticleSystem shootParticle;
	// Shoot light
	Light shootLight;
	// Effect time
	float time;

	// Use this for initialization
	void Start () {
		time = 0f;
		shootParticle = GetComponent<ParticleSystem> ();
		shootLight = GetComponent<Light> ();
	}
	
	// Update is called once per frame
	void Update () {
		time += Time.deltaTime;

		if(time >= EffectDisplayTime)
		{
			DisableFireEffects ();
		}
	}

	// Start fire according to the shoot ray
	public void StartFire(Ray ray){
		// Play the shoot particle
		shootParticle.Stop ();
		shootParticle.Play ();
		// Enable the light
		shootLight.enabled = true;
		// Play shoot sound
		AudioSource.PlayClipAtPoint (FireSound, transform.position);

		// Set hit effects
		SetHitEffects(ray);

		// Reset time
		time = 0f;
	}

	// enabel fire effect
	void DisableFireEffects(){
		shootLight.enabled = false;
		shootParticle.Stop ();
	}

	// Set hit effects
	void SetHitEffects(Ray ray){
		RaycastHit hitInfo;
		if (Physics.Raycast (ray, out hitInfo, ShootDistance)) {
			if (hitInfo.collider != null) {
				bool useEffect = true;
				// Set the enemy damge if shoot the enemy
				if (!hitInfo.collider.isTrigger && hitInfo.collider.CompareTag ("Enemy")) {
					EnemyHealth enemyHealth = hitInfo.collider.gameObject.GetComponent<EnemyHealth> ();
					EnemyState enemyState = hitInfo.collider.gameObject.GetComponent<EnemyState> ();
					if (enemyState != null && enemyState.Active && enemyHealth != null) {
						enemyHealth.GetHurt (DamageValue);
					} else {
						useEffect = false;
					}
				}
				// Set hit effects
				if (useEffect) {
					HitEffects hitEffect = hitInfo.collider.gameObject.GetComponent<HitEffects> ();
					if (hitEffect != null) {
						hitEffect.EnableExplosion (EnableHitExplosion);
						hitEffect.SetExplosionType (ExplosionType);
						hitEffect.SetHitEffects (hitInfo.point, hitInfo.normal);
					}
				}
			}
		}
	}
}
