from ursina import *


def Tree(tree_texture = '', leaf_texture = '', model_tree = '', model_leaf = '', right = '', up = '', forward = ''):

	# Daraxt poyasi
	block1 = Entity(model= model_tree,
		texture = tree_texture,
		collider= 'box',
		position=(right, up, forward))

	b2 = up + 1
	b3 = up + 2
	b4 = up + 3

	block2 = Entity(model= model_tree,
		texture = tree_texture,
		collider= 'box',
		position=(right, b2, forward))

	block3 = Entity(model= model_tree,
		texture = tree_texture,
		collider= 'box',
		position=(right, b3, forward))

	block4 = Entity(model= model_tree,
		texture = tree_texture,
		collider= 'box',
		position=(right, b4, forward))


	# Daraxt barglari
	ba1 = up + 4

	barg1 = Entity(model= model_leaf,
		texture = leaf_texture,
		collider= 'box',
		position=(right, ba1, forward))

	right2 = right - 1
	up2 = up + 3 

	barg2 = Entity(model= model_leaf,
		texture = leaf_texture,
		collider= 'box',
		position=(right2, up2, forward))

	right3 = right + 1
	
	barg3 = Entity(model = model_leaf,
		texture = leaf_texture,
		collider = 'box',
		position = (right3, up2, forward))

	forward1 = forward + 1

	barg4 = Entity(model= model_leaf,
		texture = leaf_texture,
		collider= 'box',
		position=(right2, up2, forward1))

	forward2 = forward - 1

	barg5 = Entity(model= model_leaf,
		texture = leaf_texture,
		collider= 'box',
		position=(right2, up2, forward2))


	barg6 = Entity(model= model_leaf,
		texture = leaf_texture,
		collider= 'box',
		position=(right3, up2, forward1))


	barg7 = Entity(model= model_leaf,
		texture = leaf_texture,
		collider= 'box',
		position=(right3, up2, forward2)) 

	barg8 = Entity(model= model_leaf,
		texture = leaf_texture,
		collider= 'box',
		position=(right, up2, forward1))


	barg9 = Entity(model= model_leaf,
		texture = leaf_texture,
		collider= 'box',
		position=(right, up2, forward2)) 