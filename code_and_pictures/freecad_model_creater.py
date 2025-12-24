import math
import sys

# FreeCAD Installation Directory paths (First line is for all users and other is just you path) [You just need this to work]
sys.path.append(r"C:\Program Files\FreeCAD 0.20\\bin")
sys.path.append(r"~\AppData\Local\Programs\FreeCAD 0.20\bin")

# Then we can import the FreeCAD without getting any issues
import FreeCAD
import FreeCADGui
from FreeCAD import Base
import Part



class CreateFreecadModel:
    def __init__(self) -> None:
        # Ellipse center (x, y, z)
        self.center_one = FreeCAD.Vector(0, 0, 40)
        self.center_two = FreeCAD.Vector(0, 0, 50)
        self.center_three = FreeCAD.Vector(0, 0, 80)
        self.center_four = FreeCAD.Vector(0, 0, 90)

        # Ellipse Major and minor radii
        self.maj_rad_one = int
        self.min_rad_one = int
        self.maj_rad_two = int
        self.min_rad_two = int
        self.maj_rad_three = int
        self.min_rad_three = int
        self.maj_rad_four = int
        self.min_rad_four = int

    def first_model(self):
        # Creating a new document
        doc = App.newDocument("Vcavity")
        
    


doc = App.newDocument("Vcavity")





# Extrude a closed edge (e.g. circle), will optionally produce a closed face (e.g. an open ended cylinder)
# or if the parameter "solid" is "true" will produce a solid (e.g. a closed solid cylinder)
# Extrude a closed Wire (e.g. a Draft Wire), will optionally produce a shell (several joined faces) or if the parameter "solid" is "true" will produce a solid
# Ellipse centers (x,y,z)
cent1 = FreeCAD.Vector(0, 0, 40)
cent2 = FreeCAD.Vector(0, 0, 50)
cent3 = FreeCAD.Vector(0, 0, 80)
cent4 = FreeCAD.Vector(0, 0, 90)


# Ellipse Major and minor radii

majRad1 = 10

minRad1 = 5

majRad2 = 7

minRad2 = 5

majRad3 = 10

minRad3 = 10

majRad4 = 15

minRad4 = 15

eli = Part.Ellipse(cent1, majRad1, minRad1)

# eli.toShape turns it into an edge

eliShape = eli.toShape()

# wires can be fused/lofted

w1 = Part.Wire(eliShape)

eli2 = Part.Ellipse(cent2, majRad2, minRad2)

eliShape2 = eli2.toShape()

w2 = Part.Wire(eliShape2)

eli3 = Part.Ellipse(cent3, majRad3, minRad3)

eliShape3 = eli3.toShape()

w3 = Part.Wire(eliShape3)

eli4 = Part.Ellipse(cent4, majRad4, minRad4)

eliShape4 = eli4.toShape()

w4 = Part.Wire(eliShape4)

#This creates a conic shape between the ellipses

#True = solid, False = hollow

first_object = Part.makeLoft([w1, w2, w3, w4], False)

#Need this to show the part

Part.show(first_object)

### important VVV

obj = doc.addObject("Part::Feature", "Compound")

obj.Shape = first_object

App.ActiveDocument.recompute()

obj.Shape.exportStep("first_object.step")

### important ^^^
# The bottom code is needed to show up on FreeCAD
# Gui.activeDocument().activeView().viewAxometric()
# Gui.SendMsgToActiveView("ViewFit")
doc = App.activeDocument()
ellipsoid = doc.addObject("Part::Ellipsoid", "myEllipsoid")

# radius 1 is the radius of ellipsoid in z direction
# radius 2 is the radius of ellipsoid in x direction
# radius 3 is the radius of ellipsoid in y direction

ellipsoid.Radius1 = 15

ellipsoid.Radius2 = 20

ellipsoid.Radius3 = 10

ellipsoid.Placement = App.Placement(App.Vector(0, -30, 40), App.Rotation(15, 0, 20))

doc.recompute()

ellipsoid.Shape.exportStep("ellipsoid.step")

#Ellipse centers (x,y,z)

cent10 = FreeCAD.Vector(-10, 80, 40)

cent20 = FreeCAD.Vector(-10,80,50)

cent30 = FreeCAD.Vector(-10,80,80)

cent40 = FreeCAD.Vector(-10,80,90)

#Ellipse Major and minor radii

majRad10 = 10

minRad10 = 10

majRad20 = 8.5

minRad20 = 8.5

majRad30 = 10

minRad30 = 10

majRad40 = 15

minRad40 = 15

eli = Part.Ellipse(cent10, majRad10, minRad10)

#eli.toShape turns it into an edge

eliShape = eli.toShape()

# wires can be fused/lofted

w10 = Part.Wire(eliShape)

eli20 = Part.Ellipse(cent20, majRad20, minRad20)

eliShape20 = eli20.toShape()

w20 = Part.Wire(eliShape20)

eli30 = Part.Ellipse(cent30, majRad30, minRad30)

eliShape30 = eli30.toShape()

w30 = Part.Wire(eliShape30)

eli40 = Part.Ellipse(cent40, majRad40, minRad40)

eliShape40 = eli40.toShape()

w40 = Part.Wire(eliShape40)

#This creates a conic shape between the ellipses

#True = solid, False = hollow

L = Part.makeLoft([w10, w20, w30, w40], False)

#Need this to show the part

Part.show(L)

obj = App.ActiveDocument.addObject("Part::Feature", "Compound")

obj.Shape = L

App.ActiveDocument.recompute()

obj.Shape.exportStep("ellipse.step")

#The bottom code is needed to show up on FreeCAD

# Gui.activeDocument().activeView().viewAxometric()

# Gui.SendMsgToActiveView("ViewFit")