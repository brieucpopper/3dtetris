# 3D Tetris
*2020 — team project @ Lycée Pasteur*

A 3D Tetris game in Python, with the 3D rendering done manually (no 3D engine).

Same rules as Tetris, except pieces can also be rotated along the third dimension, which opens up new combinations. The player moves around in the world and sees the blocks in 3D. All projection calculations are done by hand, so the game is slow to run. Some hot paths are compiled with numba.

Code comments are in French (project predates my switch to English comments).

## Screenshots

![tetris3](https://user-images.githubusercontent.com/102361078/214153735-9b5bb675-1849-45ea-878c-0c3faba7ad3a.png)

![tetris1](https://user-images.githubusercontent.com/102361078/214153747-1f093bfc-5c8c-4f92-b60c-b6d4635c1f12.png)
![rot](https://user-images.githubusercontent.com/102361078/214153759-e2f7e8fc-cc41-4f57-b639-e77830a54013.png)

The geometry we implemented:
![aee](https://user-images.githubusercontent.com/102361078/214153809-dae375b8-c4e5-41da-ad5f-b6b1f80081f4.jpg)

Main challenges were matrix math for 3D projection, getting the geometry right, and speeding up the Python code with numba.

## Run it

Run `Main.py` and follow the instructions. Requires `numpy`, `pygame`, `numba`.
