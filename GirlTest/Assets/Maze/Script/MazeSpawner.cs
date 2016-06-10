//
// Create maze
// 
// 2016/05/06 Elvis Jia
//
using UnityEngine;
using System.Collections;

public class MazeSpawner : MonoBehaviour {
	
	public GameObject Floor = null;
	public GameObject Wall = null;
	public GameObject Pillar = null;
	public GameObject Goblin = null;
	public float GoblinPosHeight = 2;
	public int Rows = 5;
	public int Columns = 5;
	public float CellWidth = 5;
	public float CellHeight = 5;
	public bool AddGaps = true;
	public GameObject EnemySpawnerPrefab = null;
	private MazeCell[,] mazeArray;
	public MazeCell[,] MazeArray {
		set{
			mazeArray = value;
		}
	}
	

	public void Build () {
		// Build walls
		BuildWalls();

		// Build pillars and goblins
		BuildPillarAndGoblins();			
	}

	// Build walls
	void BuildWalls(){
		// Build inside walls
		for (int row = 0; row < Rows; row++) {
			for(int column = 0; column < Columns; column++){
				float x = GetXPos(column);
				float z = GetZPos(row);
				MazeCell cell = mazeArray[row,column];
				GameObject wall;
				wall = Instantiate(Floor,new Vector3(x,0,z), Quaternion.Euler(0,0,0)) as GameObject;
				SetTransformAndTag(wall);

				if(cell.wall_right){
					wall = Instantiate(Wall,new Vector3(x+CellWidth/2,0,z)+Wall.transform.position,Quaternion.Euler(0,90,0)) as GameObject;// right
					SetTransformAndTag(wall);
				}
				if(cell.wall_front){
					wall = Instantiate(Wall,new Vector3(x,0,z+CellHeight/2)+Wall.transform.position,Quaternion.Euler(0,0,0)) as GameObject;// front
					SetTransformAndTag(wall);
				}
				if(cell.wall_left){
					wall = Instantiate(Wall,new Vector3(x-CellWidth/2,0,z)+Wall.transform.position,Quaternion.Euler(0,270,0)) as GameObject;// left
					SetTransformAndTag(wall);
				}
				if(cell.wall_back){
					wall = Instantiate(Wall,new Vector3(x,0,z-CellHeight/2)+Wall.transform.position,Quaternion.Euler(0,180,0)) as GameObject;// back
					SetTransformAndTag(wall);
				}
				if(cell.is_enemy_spawner && EnemySpawnerPrefab != null){
					wall = Instantiate(EnemySpawnerPrefab,new Vector3(x,1,z), Quaternion.Euler(0,0,0)) as GameObject;
					SetTransformAndTag(wall);
				}
			}
		}
		// Build outside walls
		for(int row = 0; row < Rows; row++){
			float x = GetXPos(-1);
			float z = GetZPos(row);
			GameObject wall = Instantiate(Wall,new Vector3(x+CellWidth/2,0,z)+Wall.transform.position,Quaternion.Euler(0,90,0)) as GameObject;// right
			SetTransformAndTag(wall);

			x = GetXPos(Columns);
			wall = Instantiate(Wall,new Vector3(x-CellWidth/2,0,z)+Wall.transform.position,Quaternion.Euler(0,270,0)) as GameObject;// left
			SetTransformAndTag(wall);
		}
		for(int column = 0; column < Columns; column++){
			float x = GetXPos(column);
			float z = GetZPos(-1);
			GameObject wall = Instantiate(Wall,new Vector3(x,0,z+CellHeight/2)+Wall.transform.position,Quaternion.Euler(0,0,0)) as GameObject;// front
			SetTransformAndTag(wall);

			z = GetZPos(Rows);
			wall = Instantiate(Wall,new Vector3(x,0,z-CellHeight/2)+Wall.transform.position,Quaternion.Euler(0,180,0)) as GameObject;// back
			SetTransformAndTag(wall);
		}
	}

	// Build pillars and gobins
	void BuildPillarAndGoblins(){
		if(Pillar != null){
			for (int row = 0; row < Rows+1; row++) {
				for (int column = 0; column < Columns+1; column++) {
					float x = GetXPos(column);
					float z = GetZPos(row);
					GameObject pillar = Instantiate(Pillar,new Vector3(x-CellWidth/2, 0, z-CellHeight/2),Quaternion.identity) as GameObject;
					SetTransformAndTag(pillar);

					// Create goblins
					/*GameObject goblin = Instantiate(Goblin, new Vector3(x-CellWidth/2, GoblinPosHeight, z-CellHeight/2),Quaternion.identity) as GameObject;
					// Set forward
					if(row % 2 == 0){
						goblin.transform.forward = pillar.transform.forward;
					}else{
						goblin.transform.forward = -pillar.transform.forward;
					}
					goblin.GetComponent<GoblinState> ().MakeLikeStone ();

					if(enemySpawner != null){
						goblin.transform.parent = enemySpawner.transform;
					}*/

				}
			}
		}
	}

	// Get X position of walls or pillars
	float GetXPos(int column){
		return column*(CellWidth+(AddGaps?0.2f:0));;
	}

	// Get Z position of walls or pillars
	float GetZPos(int row){
		return row*(CellHeight+(AddGaps?.2f:0));
	}

	// Set transform parent and tag
	void SetTransformAndTag(GameObject obj){
		obj.transform.parent = transform;
		obj.tag = tag;
	}

	// Get real position according to the simplified index position such as (0,2,3)
	public Vector3 GetReaPosWithIndexPos(int[] indexPos){
		return new Vector3(indexPos[0]*CellWidth,indexPos[1],indexPos[2]*CellHeight);
	}
}
