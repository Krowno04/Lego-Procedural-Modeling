import maya.cmds as cmds

def showPoints(iPoints):
    for cPoint in iPoints: cmds.spaceLocator(p=(cPoint))

cmds.file( force=True, new=True )

def factorial(nValue):
    fValue = 1.0
    for i in range(1, nValue): fValue *= float(i)
    
    return fValue

def binomialCoeff(nValue, kValue):
    # n! / k! * (n-k)!
    if(kValue == 0): return 1.0
    return factorial(nValue) / (factorial(kValue) * factorial(nValue - kValue))

def calculateBezier2D(iPointU, uValue):
    
    cPointCount = len(iPointU)
    nValue = cPointCount - 1
    
    cCoord = [0.0, 0.0, 0.0]
    cOneMinusU = (1.0 - uValue)
    
    for i in range(0, cPointCount):
        cBinCoeff = binomialCoeff(nValue, i)
        cPreSum = cBinCoeff * (cOneMinusU ** (nValue - i)) * (uValue ** i)
        
        cCoord[0] += iPointU[i][0] * cPreSum
        cCoord[1] += iPointU[i][1] * cPreSum
        cCoord[2] += iPointU[i][2] * cPreSum

    return cCoord

def createCurve():
    r, c = 5, 3
    cPointsU = [[0 for x in range(c)] for y in range(r)]
    
    # U Points (5)
    cPointsU[0] = [0.0, 0.0, -10.0]
    cPointsU[1] = [0.0, 10.0, -5.0]
    cPointsU[2] = [0.0, 0.0, 0.0]
    cPointsU[3] = [0.0, 10.0, 10.0]
    cPointsU[4] = [0.0, 0.0, 20.0]
    
    showPoints(cPointsU)
    
    cStepRange = 100 # StepSize = 1/cStepRange

    for u in range(0, cStepRange):
        uValue = u / float(cStepRange)
        cTmpPoint = calculateBezier2D(cPointsU, uValue)
        
        cmds.polySphere(r=0.1)
        cmds.move(cTmpPoint [0], cTmpPoint[1], cTmpPoint[2], a=True)

def calculateBezier3D(iPointUV, uCount, vCount, uValue, vValue):
    
    nValue = uCount - 1
    mValue = vCount - 1
    cCoord = [0.0, 0.0, 0.0]
    cOneMinusU = 1.0 - uValue
    cOneMinusV = 1.0 - vValue

    for i in range(0, uCount):
        for j in range(0, vCount):
            binCoeffU = binomialCoeff(nValue, i)
            binCoeffV = binomialCoeff(mValue, j)
            
            cPreSumU = binCoeffU * (cOneMinusU ** (nValue - i)) * (uValue ** i)
            cPreSumV = binCoeffV * (cOneMinusV ** (mValue - j)) * (vValue ** j)
            
            kValue = (i * (nValue + 1)) + j
            
            cCoord[0] += cPreSumU * cPreSumV * iPointUV[kValue][0]
            cCoord[1] += cPreSumU * cPreSumV * iPointUV[kValue][1]
            cCoord[2] += cPreSumU * cPreSumV * iPointUV[kValue][2]

    return cCoord

def createSurface():
    r, c = 25, 3
    cPointsUV = [[0 for x in range(c)] for y in range(r)]
    
    showPoints(cPointsUV)
    
    cStepRange = 50
    stepSize = 1.0/cStepRange
    
    for u in range(0, cStepRange):
        for v in range(0, cStepRange):
            
            uValue = float(u) / float(cStepRange)
            vValue = float(v) / float(cStepRange)
            
            uStep = uValue + stepSize
            vStep = vValue + stepSize
            
            refPoint00 = calculateBezier3D(cPointsUV, 5, 5, uValue, vValue)
            refPoint01 = calculateBezier3D(cPointsUV, 5, 5, uValue, vStep)
            refPoint10 = calculateBezier3D(cPointsUV, 5, 5, uStep, vValue)
            refPoint11 = calculateBezier3D(cPointsUV, 5, 5, uStep, vStep)
            
            cmds.polyCreateFacet(p=[refPoint00, refPoint01, refPoint11, refPoint10])


    # UV Points (5 x 5)
    # Paste Point code from Brightspace here
    -10.0 	0.0 	-10.0
    -10.0 	10.0	-5.0
    -10.0 	0.0	0.0
    -10.0	10.0	10.0
    -10.0	0.0	20.0

    -5.0 	0.0 	-5.0
    -5.0 	10.0	0.0
    -5.0 	0.0	-5.0
    -5.0	10.0	5.0
    -5.0	0.0	15.0

    0.0 	0.0 	0.0
    0.0 	10.0	-15.0
    0.0 	0.0	-10.0
    0.0	10.0	0.0
    0.0	0.0	10.0

    5.0 	0.0 	-5.0
    5.0 	10.0	0.0
    5.0 	0.0	-5.0
    5.0	10.0	5.0
    5.0	0.0	15.0

    10.0 	0.0 	-10.0
    10.0 	10.0	-5.0
    10.0 	0.0	0.0
    10.0	10.0	10.0
    10.0	0.0	20.0



