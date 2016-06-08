using System;
using System.Collections;

//Class for representing concrete maze cell.
[Serializable]
public struct MazeCell{
	public bool isVisited;
	public bool wallRight;
	public bool wallFront;
	public bool wallLeft;
	public bool wallBack;
	public bool isEnemySpawner;
}
