import FreeCAD, Part, Drawing, math, ImportGui

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_tank"


def clear_doc():
    # Clear the active document deleting all the objects
    for obj in DOC.Objects:
        DOC.removeObject(obj.Name)


def setview():
    # Rearrange View
    FreeCAD.Gui.SendMsgToActiveView("ViewFit")
    FreeCAD.Gui.activeDocument().activeView().viewAxometric()


if DOC is None:
    FreeCAD.newDocument(DOC_NAME)
    FreeCAD.setActiveDocument(DOC_NAME)
    DOC = FreeCAD.activeDocument()
else:
    clear_doc()

# EPS= tolerance to use to cut the parts
EPS = 0.10
EPS_C = EPS * -0.5

# tank
tank = Part.makeBox(53, 53, 100)

# box_1 for chamber
box_1 = Part.makeBox(25, 25, 100)
box_1_vector = FreeCAD.Vector(14, 14, 0)
box_1.translate(box_1_vector)

# cut tank by box_1
tank = tank.cut(box_1)

# box_2
box_2 = Part.makeBox(53, 53, 94)

# box_3
box_3 = Part.makeBox(31, 31, 94)
box_3_vector = FreeCAD.Vector(11, 11, 0)
box_3.translate(box_3_vector)

# cut box_2 by box_3
box_2 = box_2.cut(box_3)

# tank cut by box_2
box_2_vector = FreeCAD.Vector(0, 0, 3)
box_2.translate(box_2_vector)
tank = tank.cut(box_2)

# cylinder
cylinder = Part.makeCylinder(2.5, 100)

# tank cut by cylinder for hole 1
cylinder_vector = FreeCAD.Vector(5.5, 5.5, 0)
cylinder.translate(cylinder_vector)
tank = tank.cut(cylinder)

# tank cut by cylinder for hole 2
cylinder_vector = FreeCAD.Vector(42, 0, 0)
cylinder.translate(cylinder_vector)
tank = tank.cut(cylinder)

# tank cut by cylinder for hole 3
cylinder_vector = FreeCAD.Vector(0, 42, 0)
cylinder.translate(cylinder_vector)
tank = tank.cut(cylinder)

# tank cut by cylinder for hole 4
cylinder_vector = FreeCAD.Vector(-42, 0, 0)
cylinder.translate(cylinder_vector)
tank = tank.cut(cylinder)

# tank cut by cylinder for hole 5
cylinder_output = Part.makeCylinder(2.5, 40)
cylinder_output_vector = FreeCAD.Vector(26.5, 26.5, 8.5)
cylinder_output.translate(cylinder_output_vector)
cylinder_output.rotate(FreeCAD.Vector(26.5, 26.5, 8.5),FreeCAD.Vector(0, 1, 0), 90)
tank = tank.cut(cylinder_output)

# box_4
box_4 = Part.makeBox(29, 29, 2)

# box_5
box_5 = Part.makeBox(27, 27, 2)
box_5_vector = FreeCAD.Vector(1, 1, 0)
box_5.translate(box_5_vector)

# box_4 cut by box_5
box_4 = box_4.cut(box_5)

# tank cut by box_4 for top support
box_4_vector = FreeCAD.Vector(12, 12, 0)
box_4.translate(box_4_vector)
tank = tank.cut(box_4)

# tank cut by box_4 for bottom support
box_4_vector = FreeCAD.Vector(0, 0, 98)
box_4.translate(box_4_vector)
tank = tank.cut(box_4)

Part.show(tank)

DOC.recompute()

__objs__ = []

__objs__.append(FreeCAD.getDocument("part_tank").getObject("Shape"))

step_file = u"path/to/part_tank.step"

ImportGui.export(__objs__, step_file)

setview()