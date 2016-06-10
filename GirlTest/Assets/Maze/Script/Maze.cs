using System;
using System.Collections;

//Class for representing concrete maze cell.
[Serializable]
public struct MazeCell{
	public bool is_visited;
	public bool wall_right;
	public bool wall_front;
	public bool wall_left;
	public bool wall_back;
	public bool is_enemy_spawner;
}
