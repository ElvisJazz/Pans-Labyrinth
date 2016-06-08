using System;
using System.Collections;

[Serializable]
public class MazeMessageFromServer: BaseMessage{
	public int row;
	public int column;
	public MazeCell[] maze_array;
}