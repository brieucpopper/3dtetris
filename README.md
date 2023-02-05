# 3D Tetris
<h2>A 3D tetris game in python with the 3D rendering done manually</h2>

This game was invented for the purpose of a team project I led with two other schoolmates. The game is basically a Tetris but you can use the third dimension to rotate pieces and therefore create new combination and strategies.
The player can move around in the world and see the blocks in 3D. All calculations to render frames are done manually (and therefore the game is very laggy and slow to run)
<br>
The project was not initially worked on with git, but the code is supposed to be readable and is commented (but in french)




# Some examples from the game

![tetris3](https://user-images.githubusercontent.com/102361078/214153735-9b5bb675-1849-45ea-878c-0c3faba7ad3a.png)


![tetris1](https://user-images.githubusercontent.com/102361078/214153747-1f093bfc-5c8c-4f92-b60c-b6d4635c1f12.png)
![rot](https://user-images.githubusercontent.com/102361078/214153759-e2f7e8fc-cc41-4f57-b639-e77830a54013.png)


This geometry was implemented :
![aee](https://user-images.githubusercontent.com/102361078/214153809-dae375b8-c4e5-41da-ad5f-b6b1f80081f4.jpg)


Interesting challenges were:
</br>
-learning to use matrix operations for 3d</br>
-figuring out the geometry</br>
-trying to speed up our python program by compiling some parts of it

and many more...


# Running the game
To start the game simply run the Main.py file and follow the instructions given (with pygame installed)

The player can move around, and also interact with pieces (play tetris, and rotate pieces in the third dimension)<br>
You need to install numba, numpy, pygame (python modules).
