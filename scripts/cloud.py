from ursina import *

def Cloud(cloud_texture = '', model_cloud = 'block'):
    # First cloud
    ############################################################## 
    ##############################################################

    for a in range(11, 60):
        line1 = Entity(model= model_cloud,
            texture = cloud_texture,
            collider= 'box',
            position=(3, 30, a)) 

    for b in range(4, 10):
        for c in range(10, 63):
            line2 = Entity(model= model_cloud,
                texture = cloud_texture,
                collider= 'box',
                position=(b, 30, c)) 
            
    for d in range(10, 13):
        for e in range(21, 43):
                line2 = Entity(model= model_cloud,
                    texture = cloud_texture,
                    collider= 'box',
                    position=(d, 30, e))
    
    for f in range(18, 48):
        line3 = Entity(model= model_cloud,
            texture = cloud_texture,
            collider= 'box',
            position=(13, 30, f)) 
        
    for g in range(17, 46):
        line4 = Entity(model= model_cloud,
            texture = cloud_texture,
            collider= 'box',
            position=(14, 30, g))
        
    for h in range(15, 19):
        for i in range(7, 48):
                line5 = Entity(model= model_cloud,
                    texture = cloud_texture,
                    collider= 'box',
                    position=(h, 30, i))
    
    line6 = Entity(model= model_cloud,
                    texture = cloud_texture,
                    collider= 'box',
                    position=(16, 30, 48))
    
    line7 = Entity(model= model_cloud,
                    texture = cloud_texture,
                    collider= 'box',
                    position=(17, 30, 48))

    for j in range(19, 25):
        for k in range(12, 56):
                line8 = Entity(model= model_cloud,
                    texture = cloud_texture,
                    collider= 'box',
                    position=(j, 30, k))
    for l in range(15, 48):
        line9 = Entity(model= model_cloud,
                        texture = cloud_texture,
                        collider= 'box',
                        position=(25, 30, l))
        


    # Second cloud
    ############################################################## 
    ##############################################################

    for m in range(17, 45):
        line10 = Entity(model= model_cloud,
                        texture = cloud_texture,
                        collider= 'box',
                        position=(36, 30, m))
    
    for n in range(15, 47):
        line11 = Entity(model= model_cloud,
                        texture = cloud_texture,
                        collider= 'box',
                        position=(37, 30, n))
        
    for o in range(37, 42):
        for p in range(11, 51):
                line12 = Entity(model= model_cloud,
                    texture = cloud_texture,
                    collider= 'box',
                    position=(o, 30, p))
                
    for q in range(42, 49):
        for r in range(7, 58):
                line13 = Entity(model= model_cloud,
                    texture = cloud_texture,
                    collider= 'box',
                    position=(q, 30, r))
                
    for s in range(49, 54):
        for t in range(9, 56):
                line14 = Entity(model= model_cloud,
                    texture = cloud_texture,
                    collider= 'box',
                    position=(s, 30, t))
    
    for u in range(13, 48):
        line15 = Entity(model= model_cloud,
                        texture = cloud_texture,
                        collider= 'box',
                        position=(54, 30, u))
    
    for v in range(15, 45):
        line16 = Entity(model= model_cloud,
                        texture = cloud_texture,
                        collider= 'box',
                        position=(55, 30, v))
    
    for w in range(17, 41):
        line17 = Entity(model= model_cloud,
                        texture = cloud_texture,
                        collider= 'box',
                        position=(56, 30, w))
        

    # Third cloud
    ############################################################## 
    ##############################################################
    
    for ab in range(80, 130):
        line18 = Entity(model= model_cloud,
            texture = cloud_texture,
            collider= 'box',
            position=(9, 30, ab))
        
    for ac in range(82, 136):
        line19 = Entity(model= model_cloud,
            texture = cloud_texture,
            collider= 'box',
            position=(10, 30, ac))
    
    for ad in range(83, 136):
        line20 = Entity(model= model_cloud,
            texture = cloud_texture,
            collider= 'box',
            position=(11, 30, ad))
    
    for ae in range(78, 132):
        for af in range(12, 15):
            line21 = Entity(model= model_cloud,
                texture = cloud_texture,
                collider= 'box',
                position=(af, 30, ae))
     
    line22 = Entity(model= model_cloud,
                texture = cloud_texture,
                collider= 'box',
                position=(13, 30, 77))
    
    for ag in range(89, 148):
            line23 = Entity(model= model_cloud,
                texture = cloud_texture,
                collider= 'box',
                position=(15, 30, ag))
        
    for ah in range(16, 19):
        for ai in range(91, 142):
            line24 = Entity(model= model_cloud,
                texture = cloud_texture,
                collider= 'box',
                position=(ah, 30, ai))
        
    for aj in range(19, 24):
        for ak in range(82, 145):
            line25 = Entity(model= model_cloud,
                texture = cloud_texture,
                collider= 'box',
                position=(aj, 30, ak))
        
    for al in range(87, 89):
            line26 = Entity(model= model_cloud,
                texture = cloud_texture,
                collider= 'box',
                position=(17, 30, al))
            
    for am in range(93, 137):
            line27 = Entity(model= model_cloud,
                texture = cloud_texture,
                collider= 'box',
                position=(24, 30, am))
        
    for an in range(25, 31):
        for ao in range(81, 147):
            line28 = Entity(model= model_cloud,
                texture = cloud_texture,
                collider= 'box',
                position=(an, 30, ao))
    
    for ap in range(94, 140):
            line29 = Entity(model= model_cloud,
                texture = cloud_texture,
                collider= 'box',
                position=(31, 30, ap))
            
    for aq in range(32, 39):
        for ar in range(77, 149):
            line30 = Entity(model= model_cloud,
                texture = cloud_texture,
                collider= 'box',
                position=(aq, 30, ar))


    # Fourth cloud
    ############################################################## 
    ##############################################################

    for at in range(8, 68):
        for au in range(-40, -1):
            line30 = Entity(model= model_cloud,
                texture = cloud_texture,
                collider= 'box',
                position=(at, 30, au))
            
    # Fifth cloud
    ############################################################## 
    ##############################################################

    for av in range(-40, -5):
        for aw in range(-10, 68):
            line31 = Entity(model= model_cloud,
                texture = cloud_texture,
                collider= 'box',
                position=(av, 30, aw))
            
    # sixth cloud
    ############################################################## 
    ##############################################################

    for ax in range(80, 103):
        for ay in range(-12, 64):
            line32 = Entity(model= model_cloud,
                texture = cloud_texture,
                collider= 'box',
                position=(ax, 30, ay))

