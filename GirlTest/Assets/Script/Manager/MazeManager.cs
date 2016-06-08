using UnityEngine;
using System.Collections;

public class MazeManager{
	
	// Create maze
	public static void CreateMaze(MazeMessageFromServer wm){
		GameObject mazeSpwaner = GameObject.Find ("MazeSpawner");
		if (mazeSpwaner != null) {
			MazeSpawner mazeController = mazeSpwaner.GetComponent<MazeSpawner> ();
			mazeController.MazeArray = TransferTo2dArray(wm.maze_array, wm.row, wm.column);
			mazeController.Build ();
		}
	}

	// Transfer  1d array to 2d array 
	public static MazeCell[,] TransferTo2dArray(MazeCell[] array, int row, int column){
		MazeCell[,] mazeArray = new MazeCell[row, column];
		int k = 0;
		for (int i = 0; i < row; i++) {
			for (int j = 0; j < column; j++) {
				mazeArray[i,j] = array[k];
				k++;
			}
		}
		return mazeArray;
	}
}
