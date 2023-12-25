# import modules
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise
from numpy import floor
import os
from scripts.house import * 
from scripts.tree import *
from scripts.cloud import *
from scripts.floor import *
from datetime import time, datetime
from turtle import position, pu



# dedect the time
now = datetime.now().time()
hour = now.hour
year = datetime.now()



# run game
game = Ursina()

# Create a parent entity
root = Entity()



# set date on logs.txt
with open("logs.txt", "a") as f:
					f.write(f"\n\n\nstarted -- {year}:\n")
					f.close()



# Load textures  
grass_texture = load_texture('assets/block_tex/grass.jpg')
stone_texture = load_texture('assets/block_tex/stone.png')
brick_texture = load_texture('assets/block_tex/brick.png')
dirt_texture = load_texture('assets/block_tex/dirt.png')
wood_texture = load_texture('assets/block_tex/wood_block.png')
glass_texture = load_texture('assets/block_tex/glass1.png')
obsidan_texture = load_texture('Assets/block_tex/obsidan.png')
ice_texture = load_texture('assets/block_tex/ice.png')
sand_texture = load_texture('assets/block_tex/sand.png')
white_stone_texture = load_texture('assets/block_tex/white_stone.png')
hand_texture = load_texture("Assets/block_tex/Hand_Texture.png")




# Load Audios
put_sound = Audio('assets/sound/put',loop = False, autoplay = False)
crack_sound = Audio('assets/sound/crack',loop = False, autoplay = False)
glass_sound = Audio('Assets/sound/glass_break', loop = False, autoplay=False)
backmus = Audio('Assets/sound/Minecraft.mp3', loop = True, autoplay=True)
backmus.play()


# default block
block_pick = 4



# sky texture
sky_texture = 'assets/time/day.png'


# dedect the time
pod = "day"

if hour >= 6 and hour < 20:
    print("Day started!")
else:
	print("Night started!")
	pod = "night"
	grass_texture = load_texture('assets/night_tex/grass.jpg')
	stone_texture = load_texture('assets/night_tex/stone.png')
	brick_texture = load_texture('assets/night_tex/brick.png')
	dirt_texture = load_texture('assets/night_tex/dirt.png')
	wood_texture = load_texture('assets/night_tex/wood_block.png')
	glass_texture = load_texture('assets/night_tex/glass1.png')
	obsidan_texture = load_texture('Assets/night_tex/obsidan.png')
	ice_texture = load_texture('assets/night_tex/ice.png')
	sand_texture = load_texture('assets/night_tex/sand.png')
	white_stone_texture = load_texture('assets/night_tex/white_stone.png')

	sky_texture = 'assets/time/night.png'	

Sky(texture=sky_texture, parent=root)



# window settings
window.entity_counter.enabled = False
window.collider_counter.enabled = False
window.fullscreen = True
window.exit_button.enabled = False
window.fps_counter.enabled = False
window.cog_button.enabled = False
window.title = 'TINY-craft 1.4.0 version'

# Text
text_display = Text(text='You holding Dirt!', y=.45, z=.5, origin=(0,0), scale=1)


# choose blocks
def update():
	global block_pick

	if held_keys['1']: 
		block_pick = 1
		text_display.text = 'You holding Grass!'
	if held_keys['2']: 
		block_pick = 2
		text_display.text = 'You holding Stone!'
	if held_keys['3']: 
		block_pick = 3
		text_display.text = 'You holding Brick!'
	if held_keys['4']: 
		block_pick = 4
		text_display.text = 'You holding Dirt!'
	if held_keys['5']: 
		block_pick = 5
		text_display.text = 'You holding Wood!'
	if held_keys['6']: 
		block_pick = 6
		text_display.text = 'You holding Glass!'
	if held_keys['7']: 
		block_pick = 7
		text_display.text = 'You holding Obsidan!'
	if held_keys['8']: 
		block_pick = 8
		text_display.text = 'You holding Ice!'
	if held_keys['9']: 
		block_pick = 9
		text_display.text = 'You holding Sand!'
	if held_keys['0']: 
		block_pick = 10
		text_display.text = 'You holding White stone!'

	if held_keys["left mouse"] or held_keys["right mouse"]:
		hand.active()
	else:
		hand.passive()

	# display fps
	if held_keys['f']:
		window.fps_counter.enabled = True
	elif not held_keys['f']:
		window.fps_counter.enabled = False

	# respawn
	if held_keys['r']:
		player = FirstPersonController(x=25,z=25,y=25)

	# stop backmus
	if held_keys['m']:
		backmus.stop()
	
	# unfulscreen
	if held_keys['g']:
		window.fullscreen = False
	
	# for exit
	if held_keys['escape']:
		exit()
	
	




class Voxel(Button):
	# Add a dictionary to store information about voxels
	voxels = {}

	def __init__(self, position = (0,0,0), texture = grass_texture):
		super().__init__(
			parent = scene,
			position = position,
			model = 'cube',
			origin_y = 0.5,
			texture = texture,
			color = color.color(0,0,random.uniform(0.85 ,1)))
		

		
		# Define the file path
		log_path = "scripts/logs.txt"

		# Check if the file exists
		if not os.path.exists(log_path):
			# Create the file and its directory if it doesn't exist
			os.makedirs(os.path.dirname(log_path), exist_ok=True)
			

		
		# Store voxel information in the dictionary
		self.voxels[id(self)] = {
			"position": self.position,
			"texture": self.texture,}
		


	# make blocks
	def input(self,key):
		if self.hovered:
			# Block placement
			if key == 'left mouse down':
				global now_texture
				put_sound.play()

				if block_pick == 1: 
					voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
					now_texture = 'Grass'
				if block_pick == 2: 
					voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
					now_texture = 'Stone'
				if block_pick == 3:
					voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
					now_texture = 'Brick'
				if block_pick == 4: 
					voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
					now_texture = 'Dirt'
				if block_pick == 5: 
					voxel = Voxel(position = self.position + mouse.normal, texture = wood_texture)
					now_texture = 'Wood'
				if block_pick == 6: 
					voxel = Voxel(position = self.position + mouse.normal, texture = glass_texture)
					now_texture = 'Glass'
				if block_pick == 7: 
					voxel = Voxel(position = self.position + mouse.normal, texture = obsidan_texture)
					now_texture = 'Obsidan'
				if block_pick == 8: 
					voxel = Voxel(position = self.position + mouse.normal, texture = ice_texture)
					now_texture = 'Ice'
				if block_pick == 9: 
					voxel = Voxel(position = self.position + mouse.normal, texture = sand_texture)
					now_texture = 'Sand'
				if block_pick == 10: 
					voxel = Voxel(position = self.position + mouse.normal, texture = white_stone_texture)
					now_texture = 'white_stone'
				
				# Block placement information
				block_position = self.position + mouse.normal
            	
				# Write block placement information to file
				with open("logs.txt", "a") as f:
					f.write(f"Placed block at {block_position} with {now_texture}\n")
					f.close()
				



			# remove blocks
			if key == 'right mouse down':

			 	# dedect the glass sound
				crack_sound.play()

				# Block removal information
				block_info = self.voxels.pop(id(self))

				# Write block removal information to file
				with open("logs.txt", "a") as f:
					f.write(f"Removed block at {block_info['position']} with {block_info['texture']}\n")  # block_info['texture'] || UnboundLocalError: local variable 'now_texture' referenced before assignment
					f.close()
				destroy(self)


# Hand
class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = "Assets/Models/Arm",
            texture = hand_texture,
            scale = 0.2,
            rotation = Vec3(150, -10, 0),
            position = Vec2(0.4, -0.6)
        )
    
    def active(self):
        self.position = Vec2(0.3, -0.5)

    def passive(self):
        self.position = Vec2(0.4, -0.6)
hand = Hand()



# terrain settings
# Do not touch it or there will be bugs with house and trees
# default is 2, 300, 30, 8, 60 
noise = PerlinNoise(octaves=2, seed=300)
freq = 30
amp = 8

# floor
terrain_width = 60
for i in range(terrain_width*terrain_width):
	voxel = Voxel(position = (i))
	voxel.x = floor(i/terrain_width)
	voxel.z = floor(i%terrain_width)
	voxel.y = floor(noise([voxel.x/freq, voxel.z/freq]) * amp)
	


# player
player = FirstPersonController(x=25,z=25,y=25)


# day n night again
if pod == "day":
	House_wall = 'Assets/block_tex/brick'
	House_window = 'Assets/block_tex/glass1.png'

	Tree_wood = 'Assets/block_tex/wood'
	Tree_leaf = 'Assets/block_tex/leaf'
	Tree_brinch = 'Assets/block_tex/birch_log'
	Tree_leaf2 = 'Assets/block_tex/leaf2'

	Cloud_texture = 'Assets/block_tex/cloud'
if pod == "night":
	House_wall = 'Assets/night_tex/brick'
	House_window = 'Assets/night_tex/glass1.png'

	Tree_wood = 'Assets/night_tex/wood'
	Tree_leaf = 'Assets/night_tex/leaf'
	Tree_brinch = 'Assets/night_tex/birch_log'
	Tree_leaf2 = 'Assets/night_tex/leaf2'

	Cloud_texture = 'Assets/night_tex/cloud'



# import House
House(wall_texture = House_wall, block_m = 'cube', model_glass = 'cube', glass_texture = House_window)


# import Cloud script 
# Cloud(cloud_texture = Cloud_texture, model_cloud = 'cube')

# import floor script 
# gfloor(floor_texture = 'Assets/block_tex/hasker', model_floor = 'cube')


# import trees
Tree(tree_texture = Tree_wood,
	leaf_texture = Tree_leaf, 
	model_tree = 'cube', 
	model_leaf = 'cube',
	right = 30, 
	up = 0.50, 
	forward = 25)

Tree(tree_texture = Tree_brinch,
	leaf_texture = Tree_leaf2, 
	model_tree = 'cube', 
	model_leaf = 'cube',
	right = 9, 
	up = 1.50, 
	forward = 15)

Tree(tree_texture = Tree_wood,
	leaf_texture = Tree_leaf, 
	model_tree = 'cube', 
	model_leaf = 'cube',
	right = 17, 
	up = 0.50, 
	forward = 26)

Tree(tree_texture = Tree_brinch,
	leaf_texture = Tree_leaf2, 
	model_tree = 'cube', 
	model_leaf = 'cube',
	right = 8, 
	up = -2.50, 
	forward = 5)

Tree(tree_texture = Tree_wood,
	leaf_texture = Tree_leaf, 
	model_tree = 'cube', 
	model_leaf = 'cube',
	right = 52, 
	up = 3.50, 
	forward = 3)

Tree(tree_texture = Tree_wood,
	leaf_texture = Tree_leaf, 
	model_tree = 'cube', 
	model_leaf = 'cube',
	right = 53, 
	up = 0.50, 
	forward = 22)

Tree(tree_texture = Tree_brinch,
	leaf_texture = Tree_leaf2, 
	model_tree = 'cube', 
	model_leaf = 'cube',
	right = 11, 
	up = -0.50, 
	forward = 39)

Tree(tree_texture = Tree_wood,
	leaf_texture = Tree_leaf, 
	model_tree = 'cube', 
	model_leaf = 'cube',
	right = 34, 
	up = 0.50, 
	forward = 45)

Tree(tree_texture = Tree_brinch,
	leaf_texture = Tree_leaf2, 
	model_tree = 'cube', 
	model_leaf = 'cube',
	right = 46, 
	up = -1.50, 
	forward = 56)

 
 
# run game
game.run()