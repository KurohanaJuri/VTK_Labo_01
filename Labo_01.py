import vtk
import time

debuging = True

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
head.SetRadius(5.)
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
eyeLeft.SetRadius(2.)
eyeLeft.SetThetaResolution(10)
eyeLeft.SetPhiResolution(10)

eyeLeftMapper = vtk.vtkPolyDataMapper()
eyeLeftMapper.SetInputConnection(eyeLeft.GetOutputPort())

eyeLeftActor = vtk.vtkActor()
eyeLeftActor.SetMapper(eyeLeftMapper)
eyeLeftActor.GetProperty().SetColor(0, 0, 0)


eyeRight = vtk.vtkSphereSource()
eyeRight.SetRadius(2.)
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
camera.SetPosition(0, 0, 20)
camera.SetViewUp(0, 1, 0) # maybe not useful


# Renderer
renderer= vtk.vtkRenderer()
renderer.AddActor(coneActor)
renderer.AddActor(headActor)
renderer.AddActor(bodyActor)
renderer.AddActor(eyeLeftActor)
renderer.AddActor(eyeLeftActor)
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
coneActor.SetPosition(5, 0, 0)
coneActor.RotateZ(-90)

headActor.SetPosition(50,50,0)

bodyActor.SetPosition(50,50,0)

eyeLeftActor.SetPosition(50,50,0)

eyeRightActor.SetPosition(50,50,0)


def updateAll():

    noseTransform = vtk.vtkTransform()
    coneActor.SetUserTransform(noseTransform)

    def noseMove():
        noseTransform.RotateWXYZ(-1, 0, 1, 0) # -1 deg on the world axis Y

    
    for i in range(0, 90):
        time.sleep(0.03)
        
        noseMove()
        renWin.Render()

updateAll()
iren.Start()


