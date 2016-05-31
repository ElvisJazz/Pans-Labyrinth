//
// Control the hit effects
// 
// 2016/05/12 Elvis Jia
//
using UnityEngine;
using System.Collections;

public class HitEffects : MonoBehaviour {

	public enum ExplosionType{
		SMALL_EXPLOSION,
		GENERAL_EXPLOSION,
		BIG_EXPLOSION,
		NONE
	}
	// Hit decals
	public GameObject HitDecal = null;
	// Hit particle
	public GameObject HitParticle = null;
	// Explosion particle
	public GameObject SmallExplosionParticle = null;
	public GameObject GeneralExplosionParticle = null;
	public GameObject BigExplosionParticle = null;
	// Hit sound
	public AudioClip HitSound = null;
	// Explosion sound
	public AudioClip SmallExplosionSound = null;
	public AudioClip GeneralExplosionSound = null;
	public AudioClip BigExplosionSound = null;
	// Hit decal life time
	public float DecalLifteTime = 10f;
	// Explosion life time
	public float ExplosionLifteTime = 4f;

	// Is explosion
	bool isExplosion = false;
	// Explosion type
	ExplosionType explosionType = ExplosionType.NONE;

	// Enable explosion
	public void EnableExplosion(bool enable){
		isExplosion = enable;
	}

	// Set explosion type
	public void SetExplosionType(ExplosionType type ){
		explosionType = type;
	}

	// Set hit effects
	public void SetHitEffects(Vector3 hitPos, Vector3 hitNormal){
		// Make the decal "on" the surface of the hit point
		hitPos.x += (hitNormal.x>0? 0.001f : -0.001f);
		hitPos.y += (hitNormal.y>0? 0.001f : -0.001f);
		hitPos.z += (hitNormal.z>0? 0.001f : -0.001f);
		// Calculate each angle between y axis of hitDecal and normal of the hit point in each plane(xy, yz, xz)
		Vector2 xyNormal = new Vector2(hitNormal.x, hitNormal.y);
		Vector2 yzNormal = new Vector2(hitNormal.y, hitNormal.z);
		float xy = 0, yz = 0;
		if (xyNormal.magnitude > 0.00001f) {
			xy = Mathf.Acos (Vector2.Dot (new Vector2 (0, 1), xyNormal) / xyNormal.magnitude) * 180f / Mathf.PI;
		}
		if (yzNormal.magnitude > 0.00001f) {
			yz = Mathf.Acos (Vector2.Dot (new Vector2 (1, 0), yzNormal) / yzNormal.magnitude) * 180f / Mathf.PI;
		}
		if (hitNormal.x > 0)
			xy = -xy;
		if (hitNormal.z < 0)
			yz = -yz;
		// Set rotation angle
		Quaternion qua = Quaternion.Euler (yz, 0, xy);

		if (isExplosion) {
			GenerateExplosion (hitPos, qua);
		}

		if (HitParticle != null) {
			GameObject particle = Instantiate (HitParticle, hitPos, qua) as GameObject;
			particle.transform.parent = transform;
			Destroy (particle, DecalLifteTime);
		}
		if (HitSound != null) {
			AudioSource.PlayClipAtPoint (HitSound, hitPos);
		}
		if (HitDecal != null) {			
			GameObject decal = Instantiate (HitDecal, hitPos, qua) as GameObject;
			decal.transform.parent = transform;
			Destroy (decal, DecalLifteTime);
		}
	}

	// Generate explosion
	void GenerateExplosion(Vector3 position, Quaternion qua){
		GameObject explosionParticle = null;
		AudioClip explosionSound = null;
		// Select explosion type
		switch (explosionType) {
		case ExplosionType.SMALL_EXPLOSION: 
			explosionParticle = SmallExplosionParticle;
			explosionSound = SmallExplosionSound;
			break;
		case ExplosionType.GENERAL_EXPLOSION: 
			explosionParticle = GeneralExplosionParticle;
			explosionSound = GeneralExplosionSound;
			break;
		case ExplosionType.BIG_EXPLOSION: 
			explosionParticle = BigExplosionParticle;
			explosionSound = BigExplosionSound;
			break;
		default:
			break;
		}
		// Explosion
		if (explosionParticle != null) {
			Destroy (Instantiate (explosionParticle, position, qua), ExplosionLifteTime);
		}
		if (explosionSound != null) {
			AudioSource.PlayClipAtPoint (explosionSound, position);
		}
	}
}
