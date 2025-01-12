import FreeCAD, Part, Mesh, math

DOC = FreeCAD.activeDocument()

DOC_NAME = "part_disc_cathode_d30"


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

cylinder_1 = Part.makeCylinder(130, 3)

cylinder_2 = Part.makeCylinder(4, 3)

cylinder_1 = cylinder_1.cut(cylinder_2)

# holes for fixing the disc cathode on the bottom support
degre = 7.5
for i in range(int(360/degre)):
    radius = 125
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(2.5, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# cutting for passing the screw for fixing the disc anode
degres = [60, 180, 300]
for degre in degres:
    radius = 130
    alpha=(degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(9, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

# holes for fixing the cathodes on the disc cathode
degre = 90
for i in range(int(360/degre)):
    radius = 10.5
    alpha=(i*degre*math.pi)/180
    hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
    hole = Part.makeCylinder(4, 3)
    hole.translate(hole_vector)
    cylinder_1 = cylinder_1.cut(hole)

degre = 30
for i in range(int(360/degre)):
    for n in range(2, 12):
        radius = 10.5 * n
        alpha=(i*degre*math.pi)/180
        hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
        hole = Part.makeCylinder(4, 3)
        hole.translate(hole_vector)
        cylinder_1 = cylinder_1.cut(hole)

depart = 15
for i in range(0, 12):
    for n in range(4, 12):
        radius = 10.5 * n
        degre = depart + 30 * i
        alpha=(degre*math.pi)/180
        hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
        hole = Part.makeCylinder(4, 3)
        hole.translate(hole_vector)
        cylinder_1 = cylinder_1.cut(hole)

depart = 7.5
for i in range(0, 24):
    for n in range(8, 12):
        radius = 10.5 * n
        degre = depart + 15 * i
        alpha=(degre*math.pi)/180
        hole_vector = FreeCAD.Vector(radius*math.cos(alpha), radius*math.sin(alpha), 0)
        hole = Part.makeCylinder(4, 3)
        hole.translate(hole_vector)
        cylinder_1 = cylinder_1.cut(hole)

Part.show(cylinder_1)

DOC.recompute()

__objs__=[]

__objs__.append(FreeCAD.getDocument("part_disc_cathode_d30").getObject("Shape"))

stl_file = u"part_disc_cathode_d30.stl"

Mesh.export(__objs__, stl_file)

setview()
        