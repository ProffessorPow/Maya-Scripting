import maya.cmds as cmds


def SequentialRenamer(newName):


    selObjs = cmds.ls(sl=1)

    if len(selObjs) > 0:
        numCount = newName.count("#")
        if numCount > 0:

            numAmount = ("#" * numCount)
            pNewName = newName.partition(numAmount)

            pre = pNewName[0]
            suf = pNewName[2]

            i = 1
            for x in selObjs:
                num = str(i).zfill(numCount)
                finalName = (pre + num + suf)
                cmds.select(x)
                cmds.rename(finalName)
                i += 1

        else:

            cmds.error('Please insert name in the format of "Name_##"_NodeType"')
    else:
        cmds.error("No objects selected")

SequentialRenamer("arm_##_jnt")

