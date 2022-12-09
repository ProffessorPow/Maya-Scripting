import maya.cmds as cmds


def RecolorNURBSCircle(color):


    objCount = cmds.ls(sl=1)
    nameLs = cmds.ls(s=1)
    y = 1
    for x in objCount:
        cmds.setAttr(nameLs[y] + ".overrideEnabled", 1)
        cmds.setAttr(nameLs[y] + ".overrideColor", color)
        y += 1


RecolorNURBSCircle(25)

