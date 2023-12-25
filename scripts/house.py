from ursina import *



def House(wall_texture = 'white_cube', block_m = 'block', model_glass = '', glass_texture = ''):

	# 1-devor
	block1 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(3, 1.50, 40))

	block2 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(3, 1.50, 39))

	block3 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(3, 1.50, 38))

	block4 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(3, 1.50, 37))

	block5 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(3, 1.50, 41))

	block6 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(3, 1.50, 42))

	block7 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(3, 1.50, 43))


	# 2-devor
	block8 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(4, 1.50, 43))

	block9 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(5, 1.50, 43))

	block10 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(6, 1.50, 43))

	block11 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(7, 1.50, 43))


	# 3devor
	block12 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(7, 1.50, 40))

	block13 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(7, 1.50, 39))

	block14 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(7, 1.50, 38))

	block15 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(7, 1.50, 37))

	block16 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(7, 1.50, 41))

	block17 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(7, 1.50, 42))

	block18 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(7, 1.50, 43))

	# 1.2 - devor 
	block19 = Entity(model= block_m,
			texture = wall_texture,
			collider= 'box',
			position=(3, 2.50, 43))

	block20 = Entity(model= block_m,
			texture = wall_texture,
			collider= 'box',
			position=(3, 2.50, 37))
	# windows
	block21 = Entity(model= model_glass,
			texture = glass_texture,
			collider= 'box',
			position=(3, 2.50, 38))

	block22 = Entity(model= model_glass,
			texture = glass_texture,
			collider= 'box',
			position=(3, 2.50, 39))

	block23 = Entity(model= model_glass,
			texture = glass_texture,
			collider= 'box',
			position=(3, 2.50, 40))

	block24 = Entity(model= model_glass,
			texture = glass_texture,
			collider= 'box',
			position=(3, 2.50, 41))

	block25 = Entity(model= model_glass,
			texture = glass_texture,
			collider= 'box',
			position=(3, 2.50, 42))


	# 2.2 -devor
	# windows
	block26 = Entity(model= model_glass,
			texture = glass_texture,
			collider= 'box',
			position=(4, 2.50, 43))

	block27 = Entity(model= model_glass,
			texture = glass_texture,
			collider= 'box',
			position=(5, 2.50, 43))

	block28 = Entity(model= model_glass,
			texture = glass_texture,
			collider= 'box',
			position=(6, 2.50, 43))


	block29 = Entity(model= model_glass,
			texture = glass_texture,
			collider= 'box',
			position=(4, 3.50, 43))

	block30 = Entity(model= model_glass,
			texture = glass_texture,
			collider= 'box',
			position=(5, 3.50, 43))

	block31 = Entity(model= model_glass,
			texture = glass_texture,
			collider= 'box',
			position=(6, 3.50, 43))


	# 3.2 - devor 
	block29 = Entity(model= block_m,
			texture = wall_texture,
			collider= 'box',
			position=(7, 2.50, 37))

	block30 = Entity(model= block_m,
			texture = wall_texture,
			collider= 'box',
			position=(7, 2.50, 43))
	
	# windows 
	block31 = Entity(model= model_glass,
			texture = glass_texture,
			collider= 'box',
			position=(7, 2.50, 38))

	block32 = Entity(model= model_glass,
			texture = glass_texture,
			collider= 'box',
			position=(7, 2.50, 39))

	block33 = Entity(model= model_glass,
			texture = glass_texture,
			collider= 'box',
			position=(7, 2.50, 40))

	block34 = Entity(model= model_glass,
			texture = glass_texture,
			collider= 'box',
			position=(7, 2.50, 41))

	block35 = Entity(model= model_glass,
			texture = glass_texture,
			collider= 'box',
			position=(7, 2.50, 42))


	# 1.3 - devor
	block36 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(3, 3.50, 40))

	block37 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(3, 3.50, 39))

	block38 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(3, 3.50, 38))

	block39 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(3, 3.50, 37))

	block40 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(3, 3.50, 41))

	block41 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(3, 3.50, 42))

	block42 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(3, 3.50, 43))


	# 3.3 - devor
	block43 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(7, 3.50, 40))

	block44 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(7, 3.50, 39))

	block45 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(7, 3.50, 38))

	block46 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(7, 3.50, 37))

	block47 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(7, 3.50, 41))

	block48 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(7, 3.50, 42))

	block49 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(7, 3.50, 43))


	# 1.4 - devor
	block50 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(3, 4.50, 40))

	block51 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(3, 4.50, 39))

	block52 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(3, 4.50, 38))

	block53 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(3, 4.50, 37))

	block54 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(3, 4.50, 41))

	block55 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(3, 4.50, 42))

	block56 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(3, 4.50, 43))


	# 2.3 - devor
	block57 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(4, 4.50, 40))

	block58 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(4, 4.50, 39))

	block59 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(4, 4.50, 38))

	block60 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(4, 4.50, 37))

	block61 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(4, 4.50, 41))

	block62 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(4, 4.50, 42))

	block63 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(4, 4.50, 43))


	# 2.4 - devor
	block64 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(5, 4.50, 40))

	block65 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(5, 4.50, 39))

	block66 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(5, 4.50, 38))

	block67 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(5, 4.50, 37))

	block68 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(5, 4.50, 41))

	block69 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(5, 4.50, 42))

	block70 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(5, 4.50, 43))


	# 2.5 - devor
	block71 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(6, 4.50, 40))

	block72 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(6, 4.50, 39))

	block73 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(6, 4.50, 38))

	block74 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(6, 4.50, 37))

	block75 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(6, 4.50, 41))

	block76 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(6, 4.50, 42))

	block77 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(6, 4.50, 43))


	# 3.4 - devor
	block78 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(7, 4.50, 40))

	block79 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(7, 4.50, 39))

	block80 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(7, 4.50, 38))

	block81 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(7, 4.50, 37))

	block82 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(7, 4.50, 41))

	block83 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(7, 4.50, 42))

	block84 = Entity(model= block_m,
		texture = wall_texture,
		collider= 'box',
		position=(7, 4.50, 43))