import maya.cmds as cmds
import random as rnd
MyWin = 'Lego Blocks'
if cmds.window(MyWin, exists=True):
    cmds.deleteUI(MyWin, window=True)

MyWin = cmds.window(MyWin, menuBar=True, widthHeight=(500,1200))

cmds.menu(label="Basic Options")
cmds.menuItem(label="New Scene", command=('cmds.file(new=True, force=True)'))
cmds.menuItem(label="Delete Selected", command=('cmds.delete()'))


cmds.frameLayout(collapsable=True, label="Standard Block", width=475, height=180)

cmds.columnLayout()
cmds.intSliderGrp('blockHeight',l="Height", f=True, min=1, max=20, value=3)
cmds.intSliderGrp('blockWidth', l="Width (Bumps)", f=True, min=1, max=20, value=2)
cmds.intSliderGrp('blockDepth', l="Depth (Bumps)", f=True, min=1, max=20, value=8)

cmds.colorSliderGrp('blockColour', label="Colour", hsv=(120, 1, 1))
cmds.columnLayout()
cmds.button(label="Create Basic Block", command=('basicBlock()'))
cmds.setParent( '..' )

cmds.setParent( '..' )

cmds.setParent( '..' )

cmds.frameLayout(collapsable=True, label="Hole Block", width=475, height=180)

cmds.columnLayout()
cmds.intSliderGrp('holeblockHeight',l="Height", f=True, min=1, max=20, value=3)
cmds.intSliderGrp('holeblockDepth', l="Depth (Bumps)", f=True, min=1, max=20, value=2)

cmds.colorSliderGrp('holeblockColour', label="Colour", hsv=(300, 100, 100))
cmds.columnLayout()
cmds.button(label="Create Hole Block", command=('holeBlock()'))
cmds.setParent( '..' )

cmds.setParent( '..' )

cmds.setParent( '..' )


cmds.frameLayout(collapsable=True, label="Beam Block", width=475, height=180)

cmds.columnLayout()
cmds.intSliderGrp('beamblockWidth',l="Width", f=True, min=2, max=20, value=2)

cmds.colorSliderGrp('beamblockColour', label="Colour", hsv=(295.385, 1.000, 5.086))
cmds.columnLayout()
cmds.button(label="Create Beam Block", command=('beamBlock()'))
cmds.setParent( '..' )

cmds.setParent( '..' )

cmds.setParent( '..' )


cmds.frameLayout(collapsable=True, label="Smooth Block", width=475, height=180)

cmds.columnLayout()
cmds.intSliderGrp('smoothHeight',l="Height", f=True, min=1, max=20, value=1)
cmds.intSliderGrp('smoothWidth', l="Width (No Bumps)", f=True, min=1, max=20, value=2)
cmds.intSliderGrp('smoothDepth', l="Depth (No Bumps)", f=True, min=1, max=20, value=8)

cmds.colorSliderGrp('smoothColour', label="Colour", hsv=(360, 1, 1))
cmds.columnLayout()
cmds.button(label="Create Smooth Block", command=('smoothBlock()'))
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.setParent( '..' )

cmds.frameLayout(collapsable=True, label="L-Shaped Block", width=475, height=180)

cmds.columnLayout()
cmds.intSliderGrp('lBlockHeight',l="Height", f=True, min=1, max=20, value=3)
cmds.intSliderGrp('lBlockWidth', l="Width (Bumps)", f=True, min=1, max=20, value=2)
cmds.intSliderGrp('lBlockDepth', l="Depth (Bumps)", f=True, min=1, max=20, value=8)

cmds.colorSliderGrp('lBlockColour', label="Colour", hsv=(20, 1, 1))
cmds.columnLayout()
cmds.button(label="Create L-Shaped Block", command=('lShapedBlock()'))
cmds.setParent( '..' )

cmds.setParent( '..' )

cmds.setParent( '..' )


cmds.frameLayout(collapsable=True, label="Sloped Block", width=475, height=180)
cmds.columnLayout() 

cmds.intSliderGrp('slopedWidth', l="Width (Bumps)", f=True, min=1, max=20, v=4)
cmds.intSliderGrp('slopedDepth', l="Depth (Bumps)", f=True, min=2, max=4, v=2)
cmds.colorSliderGrp('slopedColour', l="Colour", hsv=(12,1,1))

cmds.columnLayout()
cmds.button(label="Create Sloped Block", command=('slopedBlock()'))
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.setParent( '..' )

cmds.frameLayout(collapsable=True, label="Round Block", width=475, height=180)
cmds.columnLayout() 

cmds.intSliderGrp('roundHeight',l="Height", f=True, min=1, max=20, value=1)
cmds.intSliderGrp('roundWidth', l="Width (Bumps)", f=True, min=1, max=7, v=4)
cmds.colorSliderGrp('roundColour', l="Colour", hsv=(220,1,1))

cmds.columnLayout()
cmds.button(label="Create Round Block", command=('roundBlock()'))
cmds.setParent( '..' )
cmds.setParent( '..' )
cmds.setParent( '..' )

cmds.showWindow( MyWin )

def slopedBlock():
    blockHeight = 3
    blockWidth = cmds.intSliderGrp('slopedWidth', q=True, v=True)
    blockDepth = cmds.intSliderGrp('slopedDepth', q=True, v=True)
    rgb = cmds.colorSliderGrp('slopedColour', q=True, rgbValue=True)
    
    nsTmp = "SlopeBlock" + str(rnd.randint(1000,9999))
    cmds.select(clear=True)
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    
    cubeSizeX = blockWidth * 0.8
    cubeSizeZ = blockDepth * 0.8
    cubeSizeY = blockHeight * 0.32
    
    cmds.polyCube(h=cubeSizeY, w=cubeSizeX, d=cubeSizeZ, sz=blockDepth)
    cmds.move((cubeSizeY/2.0), y=True, a=True)

    for i in range(blockWidth):
        cmds.polyCylinder(r=0.25, h=0.20)
        cmds.move((cubeSizeY + 0.10), moveY=True, a=True)
        cmds.move(((i * 0.8) - (cubeSizeX/2.0) + 0.4), moveX=True, a=True)
        cmds.move((0 -(cubeSizeZ/2.0) + 0.4), moveZ=True)

    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color", rgb[0], rgb[1], rgb[2], typ='double3')

    cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    cmds.delete(ch=True)
    
    cmds.hyperShade(assign=(nsTmp+":blckMat"))
    
    cmds.select((nsTmp+":"+nsTmp+".e[1]"), r=True)
    cmds.move(0, -0.8, 0, r=True)
    
    if blockDepth == 4:
        tV = cmds.xform((nsTmp + ":" + nsTmp + ".vtx[8]"), q=True, t=True)
        cmds.select((nsTmp + ":" + nsTmp + ".vtx[6]"), r=True)
        cmds.move(tV[0], tV[1], tV[2], a=True)
        
        tV = cmds.xform((nsTmp + ":" + nsTmp + ".vtx[9]"), q=True, t=True)
        cmds.select((nsTmp + ":" + nsTmp + ".vtx[7]"), r=True)
        cmds.move(tV[0], tV[1], tV[2], a=True)

    if blockDepth >= 3:
        tV = cmds.xform((nsTmp + ":" + nsTmp + ".vtx[6]"), q=True, t=True)
        cmds.select((nsTmp + ":" + nsTmp + ".vtx[4]"), r=True)
        cmds.move(tV[0], tV[1], tV[2], a=True)
        
        tV = cmds.xform((nsTmp + ":" + nsTmp + ".vtx[7]"), q=True, t=True)
        cmds.select((nsTmp + ":" + nsTmp + ".vtx[5]"), r=True)
        cmds.move(tV[0], tV[1], tV[2], a=True)

    cmds.namespace( removeNamespace=":"+nsTmp, mergeNamespaceWithParent = True)
  
def smoothBlock():
    blockHeight = cmds.intSliderGrp('smoothHeight', q=True, v=True)
    blockWidth = cmds.intSliderGrp('smoothWidth', q=True, v=True)
    blockDepth = cmds.intSliderGrp('smoothDepth', q=True, v=True)
    
    rgb = cmds.colorSliderGrp('smoothColour', q=True, rgbValue=True)
    nsTmp = "Block" + str(rnd.randint(1000,9999))
    
    cmds.select(clear=True)
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    
    cubeSizeX = blockWidth * 0.8
    cubeSizeZ = blockDepth * 0.8
    cubeSizeY = blockHeight * 0.32
    
    print(cubeSizeX, "\n", cubeSizeY, "\n", cubeSizeZ, "\n", rgb, "\n", nsTmp, "\n\n\n")

    cmds.polyCube(h=cubeSizeY, w=cubeSizeX, d=cubeSizeZ)

    print(cubeSizeX, "\n", cubeSizeY, "\n", cubeSizeZ, "\n", rgb, "\n", nsTmp, "\n\n\n")

    cmds.move((cubeSizeY/2.0), moveY=True)

    print(cubeSizeX, "\n", cubeSizeY, "\n", cubeSizeZ, "\n", rgb, "\n", nsTmp, "\n\n\n")

    # This commented part is the temporary solution of moving a single, tiny stud so it can be united
    # cmds.polyCylinder(r=0.01, h=0.01)
    # cmds.move((cubeSizeY - 0.1), moveY=True, a=True)
    # cmds.move(((0.1 * 0.8) - (cubeSizeX/2.0) + 0.4), moveX=True, a=True)
    # cmds.move(((0.1 * 0.8) - (cubeSizeZ/2.0) + 0.4), moveZ=True, a=True)
    

    
    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')

    print(cubeSizeX, "\n", cubeSizeY, "\n", cubeSizeZ, "\n", rgb, "\n", nsTmp, "\n\n\n")

    # The rename from Polyunite
    # cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    # cmds.delete(ch=True)
    cmds.select(nsTmp+':pCube1', r=True)
    cmds.rename(nsTmp)
    try:
        cmds.hyperShade(assign=(nsTmp+":blckMat"))
    except:
        pass
    cmds.namespace(removeNamespace=":"+nsTmp,mergeNamespaceWithParent=True)
    print('here')

def roundBlock():
    blockHeight = cmds.intSliderGrp('roundHeight', q=True, v=True)
    blockWidth = cmds.intSliderGrp('roundWidth', q=True, v=True)
    
    rgb = cmds.colorSliderGrp('roundColour', q=True, rgbValue=True)
    nsTmp = "RoundBlock" + str(rnd.randint(1000,9999))
    
    cmds.select(clear=True)
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    
    cubeSizeR = blockWidth * 0.8
    cubeSizeY = blockHeight * 0.32
    
    cmds.polyCylinder(n=nsTmp, h=cubeSizeY, r=cubeSizeR/1.75)
    
    cmds.move((cubeSizeY/2.0), moveY=True)
    for i in range(blockWidth):
        for j in range(blockWidth):
            if (i == 0 or i == blockWidth-1) and (j == 0 or j == blockWidth-1):                    
                print("skipping this cylinder ", i, "+", j)
            else:
                cmds.polyCylinder(r=0.25, h=0.20)
                cmds.move((cubeSizeY + 0.10), moveY=True, a=True)
                cmds.move(((i * 0.8) - (cubeSizeR/2.0) + 0.4), moveX=True, a=True)
                cmds.move(((j * 0.8) - (cubeSizeR/2.0) + 0.4), moveZ=True, a=True)

    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')


    if blockWidth > 2:
        cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
        cmds.delete(ch=True)

    else:
        # cmds.select(nsTmp+':pCylinder1', r=True)
        cmds.select(nsTmp+':'+nsTmp, r=True)
        cmds.rename(nsTmp)
        
    try:
        cmds.hyperShade(assign=(nsTmp+":blckMat"))
    except:
        pass

    cmds.namespace(removeNamespace=":"+nsTmp,mergeNamespaceWithParent=True)
    
def lShapedBlock():
    blockHeight = cmds.intSliderGrp('lBlockHeight', q=True, v=True)
    blockWidth = cmds.intSliderGrp('lBlockWidth', q=True, v=True)
    blockDepth = cmds.intSliderGrp('lBlockDepth', q=True, v=True)
    
    rgb = cmds.colorSliderGrp('lBlockColour', q=True, rgbValue=True)
    nsTmp = "LBlock" + str(rnd.randint(1000,9999))
    
    cmds.select(clear=True)
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    
    cubeSizeX = blockWidth * 0.8
    cubeSizeZ = blockDepth * 0.8
    cubeSizeY = blockHeight * 0.32
    
    cmds.polyCube(h=cubeSizeY, w=cubeSizeX, d=0.8)
    cmds.move((cubeSizeY/2.0), moveY=True)
    cmds.move((cubeSizeZ/2.0 - 0.4), moveZ=True)
    cmds.move(-(cubeSizeX/2.0 - 0.4), moveX=True)
    cmds.polyCube(h=cubeSizeY, w=0.8, d=cubeSizeZ)    
    cmds.move((cubeSizeY/2.0), moveY=True)
    
    for i in range(blockWidth):
        cmds.polyCylinder(r=0.25, h=0.20)
        cmds.move((cubeSizeY + 0.10), moveY=True, a=True)
        cmds.move(((i * -0.8)), moveX=True, a=True)        
        cmds.move(((blockDepth * 0.8) - (cubeSizeZ/2.0) - 0.4), moveZ=True, a=True)
    for j in range(blockDepth):
        cmds.polyCylinder(r=0.25, h=0.20)
        cmds.move((cubeSizeY + 0.10), moveY=True, a=True)
        cmds.move(((j * 0.8) - (cubeSizeZ/2.0) + 0.4), moveZ=True, a=True)

    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')

    cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    cmds.delete(ch=True)

    cmds.hyperShade(assign=(nsTmp+":blckMat"))
    cmds.namespace(removeNamespace=":"+nsTmp,mergeNamespaceWithParent=True)

def basicBlock():
    blockHeight = cmds.intSliderGrp('blockHeight', q=True, v=True)
    blockWidth = cmds.intSliderGrp('blockWidth', q=True, v=True)
    blockDepth = cmds.intSliderGrp('blockDepth', q=True, v=True)
    
    rgb = cmds.colorSliderGrp('blockColour', q=True, rgbValue=True)
    nsTmp = "Block" + str(rnd.randint(1000,9999))
    
    cmds.select(clear=True)
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    
    cubeSizeX = blockWidth * 0.8
    cubeSizeZ = blockDepth * 0.8
    cubeSizeY = blockHeight * 0.32
    
    cmds.polyCube(h=cubeSizeY, w=cubeSizeX, d=cubeSizeZ)
    
    cmds.move((cubeSizeY/2.0), moveY=True)
    for i in range(blockWidth):
        for j in range(blockDepth):
            cmds.polyCylinder(r=0.25, h=0.20)
            cmds.move((cubeSizeY + 0.10), moveY=True, a=True)
            cmds.move(((i * 0.8) - (cubeSizeX/2.0) + 0.4), moveX=True, a=True)
            cmds.move(((j * 0.8) - (cubeSizeZ/2.0) + 0.4), moveZ=True, a=True)

    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')

    cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    cmds.delete(ch=True)

    cmds.hyperShade(assign=(nsTmp+":blckMat"))
    cmds.namespace(removeNamespace=":"+nsTmp,mergeNamespaceWithParent=True)

def holeBlock():
    holeblockHeight = cmds.intSliderGrp('holeblockHeight', q=True, v=True)
    holeblockWidth = 1
    holeblockDepth = cmds.intSliderGrp('holeblockDepth', q=True, v=True)
    
    rgb = cmds.colorSliderGrp('holeblockColour', q=True, rgbValue=True)
    nsTmp = "holeBlock" + str(rnd.randint(1000,9999))
    
    cmds.select(clear=True)
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    
    cubeSizeX = holeblockWidth * 0.8
    cubeSizeZ = holeblockDepth * 0.8
    cubeSizeY = holeblockHeight * 0.32
    
    brick = cmds.polyCube(h=cubeSizeY, w=cubeSizeX, d=cubeSizeZ)[0]

    # This function runs a loop with the boolStud function to create all the studs with hole on the top.
    # Everything is handled inside, so it just leaves you with a line of properly booled studs
    cmds.move((cubeSizeY/2.0), moveY=True)
    for i in range(holeblockWidth):
        for j in range(holeblockDepth):
            boolStud(cubeSizeY, cubeSizeX, cubeSizeZ, i, j)

    brickbool = brick
    # Originally tried this from a function, but for some reason Maya doesn't like that very much
    # So everything is now done here in the loop
    # Create cylinder -> bool through brick -> create next cylinder -> bool -> repeat
    for i in range(holeblockDepth-1):

        piercerCylinder = cmds.polyCylinder(r=0.25, h=2, sx=12, n='pierce')[0]
        cmds.move(cubeSizeY/2, moveY=True, a=True)
        cmds.move((-cubeSizeZ/2 + (i+1) * 0.8), moveZ=True, a=True)
        cmds.rotate(90, rotateZ=True, a=True)
        
        brick = cmds.polyCBoolOp(brick, piercerCylinder, op=2, ch=False)[0]

        bigCylinder1 = cmds.polyCylinder(r=0.3, h=1.35, sx=12, n='pierce1')[0]
        cmds.move(cubeSizeY/2, moveY=True, a=True)
        cmds.move(1, moveX=True, a=True)
        cmds.move((-cubeSizeZ/2 + (i+1) * 0.8), moveZ=True, a=True)
        cmds.rotate(90, rotateZ=True, a=True)
        brick = cmds.polyBoolOp(brick, bigCylinder1, op=2, ch=False)[0]

        bigCylinder2 = cmds.polyCylinder(r=0.3, h=1.35, sx=12, n='pierce2')[0]
        cmds.move(cubeSizeY/2, moveY=True, a=True)
        cmds.move(-1, moveX=True, a=True)
        cmds.move((-cubeSizeZ/2 + (i+1) * 0.8), moveZ=True, a=True)
        cmds.rotate(90, rotateZ=True, a=True)
        
        brick = cmds.polyBoolOp(brick, bigCylinder2, op=2, ch=False)[0]

            
    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')

    cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    cmds.delete(ch=True)

    cmds.hyperShade(assign=(nsTmp+":blckMat"))
    cmds.namespace(removeNamespace=":"+nsTmp,mergeNamespaceWithParent=True)

# Used to create studs with holes in them
def boolStud(cubeSizeY, cubeSizeX, cubeSizeZ, i, j):
        outerStud = cmds.polyCylinder(r=0.25, h=0.20)[0]
        cmds.move((cubeSizeY + 0.10), moveY=True, a=True)
        cmds.move(((i * 0.8) - (cubeSizeX/2.0) + 0.4), moveX=True, a=True)
        cmds.move(((j * 0.8) - (cubeSizeZ/2.0) + 0.4), moveZ=True, a=True)
        innerStud = cmds.polyCylinder(r=0.19, h=0.22)[0]
        cmds.move((cubeSizeY + 0.10), moveY=True, a=True)
        cmds.move(((i * 0.8) - (cubeSizeX/2.0) + 0.4), moveX=True, a=True)
        cmds.move(((j * 0.8) - (cubeSizeZ/2.0) + 0.4), moveZ=True, a=True)
        cmds.polyBoolOp(outerStud, innerStud, op=2, n='stud' + str(rnd.randint(1000,9999)))[0]

def beamBlock():
    beamblockWidth = cmds.intSliderGrp('beamblockWidth', q=True, v=True)
    
    rgb = cmds.colorSliderGrp('beamblockColour', q=True, rgbValue=True)
    nsTmp = "Block" + str(rnd.randint(1000,9999))
    
    cmds.select(clear=True)
    cmds.namespace(add=nsTmp)
    cmds.namespace(set=nsTmp)
    
    beamSizeW = beamblockWidth * 0.8
    beamSizeH = 0.9
    beamSizeR = 0.35
    
    brick = cmds.polyCylinder(r=beamSizeR, h=beamSizeH, sx=12,)[0]
    cmds.move(beamSizeH/2, moveY=True, a=True)

    cylinder = cmds.polyCylinder(r=beamSizeR*0.7, h=beamSizeH*1.5, sx=12)[0]
    cmds.move(beamSizeH/2, moveY=True, a=True)    
    brick = cmds.polyBoolOp(brick, cylinder, op=2, ch=False)[0]

    for i in range(beamblockWidth-1):
        cylinder = cmds.polyCylinder(r=beamSizeR, h=beamSizeH, sx=12)[0]
        cmds.move((i+1)*0.8, moveZ=True, a=True)
        cmds.move(beamSizeH/2, moveY=True, a=True)

        cylinder1 = cmds.polyCylinder(r=beamSizeR*0.7, h=beamSizeH*1.5, sx=12)[0]
        cmds.move((i+1)*0.8, moveZ=True, a=True)
        cmds.move(beamSizeH/2, moveY=True, a=True)    
        cylinder = cmds.polyBoolOp(cylinder, cylinder1, op=2, ch=False)[0]


    for j in range(beamblockWidth-1):
        cube1 = cmds.polyCube(h=0.9, w=0.1, d=1.95/2.4)[0]
        cmds.move(beamSizeH/2, moveY=True, a=True)
        cmds.move(beamSizeR-0.05, moveX=True, a=True)
        cmds.move(((j+1)*0.8)-0.8+beamSizeR+0.02, moveZ=True, a=True)

        cube2 = cmds.polyCube(h=0.9, w=0.1, d=1.95/2.4)[0]
        cmds.move(beamSizeH/2, moveY=True, a=True)
        cmds.move(-beamSizeR+0.05, moveX=True, a=True)
        cmds.move(((j+1)*0.8)-0.8+beamSizeR+0.02, moveZ=True, a=True)

        brickUnited = cmds.polyUnite(cube1, cube2, n='brickUnited')[0]

        cube3 = cmds.polyCube(h=0.1, w=0.5, d=0.31)[0]
        cmds.move(beamSizeH/2, moveY=True, a=True)
        cmds.move(((j+1)*0.8)-0.8+beamSizeR+0.05, moveZ=True, a=True)

        brickUnited = cmds.polyUnite(brickUnited, cube3, n='brickUnited')[0]

        brick = cmds.polyUnite(brick, brickUnited, n=nsTmp, ch=False)[0]
   
    #Originally used this tiny cube to make sure the polyUnite worked.
    #Just leaving this in 'cause it's funny
    #Google "Coconut TF2" to see what this is a reference to lol
    #coconut = cmds.polyCube(h=0.01, w=0.01, d=0.01)[0]

    myShader = cmds.shadingNode('lambert', asShader=True, name="blckMat")
    cmds.setAttr(nsTmp+":blckMat.color",rgb[0],rgb[1],rgb[2], typ='double3')

    cmds.polyUnite((nsTmp+":*"), n=nsTmp, ch=False)
    cmds.delete(ch=True)

    cmds.hyperShade(assign=(nsTmp+":blckMat"))
    cmds.namespace(removeNamespace=":"+nsTmp,mergeNamespaceWithParent=True)