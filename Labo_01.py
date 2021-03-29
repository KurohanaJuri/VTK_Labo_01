import time

import vtk

debuging = False

headRadius = 5.

# Nose
cone = vtk.vtkConeSource()
cone.SetHeight( 3.0 )
cone.SetRadius( 1.0 )
cone.SetResolution(10)

coneMapper = vtk.vtkPolyDataMapper()
coneMapper.SetInputConnection(cone.GetOutputPort())

coneActor = vtk.vtkActor()
coneActor.SetMapper(coneMapper)
coneActor.GetProperty().SetColor(255 / 255, 153 / 255, 51 / 255)

# Head

head = vtk.vtkSphereSource()
head.SetRadius(headRadius)
head.SetThetaResolution(10)
head.SetPhiResolution(10)

headMapper = vtk.vtkPolyDataMapper()
headMapper.SetInputConnection(head.GetOutputPort())

headActor = vtk.vtkActor()
headActor.SetMapper(headMapper)
headActor.GetProperty().SetColor(1, 1, 1)

# Body

body = vtk.vtkSphereSource()
body.SetRadius(7.)
body.SetThetaResolution(10)
body.SetPhiResolution(10)

bodyMapper = vtk.vtkPolyDataMapper()
bodyMapper.SetInputConnection(body.GetOutputPort())

bodyActor = vtk.vtkActor()
bodyActor.SetMapper(bodyMapper)
bodyActor.GetProperty().SetColor(1, 1, 1)

# Eyes

eyeLeft = vtk.vtkSphereSource()
eyeLeft.SetRadius(1.)
eyeLeft.SetThetaResolution(10)
eyeLeft.SetPhiResolution(10)

eyeLeftMapper = vtk.vtkPolyDataMapper()
eyeLeftMapper.SetInputConnection(eyeLeft.GetOutputPort())

eyeLeftActor = vtk.vtkActor()
eyeLeftActor.SetMapper(eyeLeftMapper)
eyeLeftActor.GetProperty().SetColor(0, 0, 0)


eyeRight = vtk.vtkSphereSource()
eyeRight.SetRadius(1.)
eyeRight.SetThetaResolution(10)
eyeRight.SetPhiResolution(10)

eyeRightMapper = vtk.vtkPolyDataMapper()
eyeRightMapper.SetInputConnection(eyeRight.GetOutputPort())

eyeRightActor = vtk.vtkActor()
eyeRightActor.SetMapper(eyeRightMapper)
eyeRightActor.GetProperty().SetColor(0, 0, 0)

# Camera
camera = vtk.vtkCamera()
camera.SetFocalPoint(0, 0, 0)
camera.SetPosition(0, 0, 120)
camera.SetViewUp(0, 1, 0) # maybe not useful


# Renderer
renderer= vtk.vtkRenderer()
renderer.AddActor(coneActor)
renderer.AddActor(headActor)
renderer.AddActor(bodyActor)
renderer.AddActor(eyeLeftActor)
renderer.AddActor(eyeRightActor)
renderer.SetBackground(0.1, 0.2, 0.4)
renderer.SetActiveCamera(camera)

# DEBUGING Add world axes
if debuging :
    axes = vtk.vtkAxesActor()
    renderer.AddActor(axes)

# Renderer Window
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer( renderer )
renWin.SetSize( 500, 500 )

# Interactive mode
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
style = vtk.vtkInteractorStyleTrackballCamera()
iren.SetInteractorStyle(style)


iren.Initialize()
 
# Init 
coneActor.SetPosition(10, 0, 0)
coneActor.RotateZ(-90)

headActor.SetPosition(-15,0,0)

bodyActor.SetPosition(0,0,0)

eyeLeftActor.SetPosition(3,10,4)
eyeLeftActor.SetVisibility(False)

eyeRightActor.SetPosition(-3,10,4)
eyeRightActor.SetVisibility(False)


# animations
def noseMove():
    noseTransform = vtk.vtkTransform()
    coneActor.SetUserTransform(noseTransform)
    
    for i in range(0, 90):
        time.sleep(0.03)
        
        noseTransform.RotateWXYZ(-1, 0, 1, 0)  # -1 deg on the world axis Y
        renWin.Render()
    
    for i in range(0, 90):
        time.sleep(0.03)
        
        noseTransform.RotateWXYZ(1, 0, 0, 1)  # 1 deg on the world axis Z. The coordinates change with the transformation
        renWin.Render()

    factor = 20 # to smooth the animation
    for i in range(0, int(headRadius * factor)):
        time.sleep(0.03)

        noseTransform.Translate(0, -1 / factor, 0)
        renWin.Render()

def moveHeadAlone():
    headTransform = vtk.vtkTransform()
    headActor.SetUserTransform(headTransform)

    for i in range(0, 90):
        time.sleep(0.03)

        headTransform.RotateWXYZ(-1, 0, 0, 1)
        renWin.Render()

    factor = 20 # to smooth the animation
    for i in range(0, int(headRadius * factor)):
        time.sleep(0.03)

        headTransform.Translate(1 / factor, 0, 0)
        renWin.Render()

def setEyesVisibility() :
    eyeRightActor.SetVisibility(True)
    eyeLeftActor.SetVisibility(True)

def updateAll():

    moveHeadAlone()
    noseMove()
    setEyesVisibility()


updateAll()
iren.Start()


