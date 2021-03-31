#  Chau Ying Kot, Adrian Mayo Cartes
import time
import vtk

debuging = False

headRadius = 5.
sleepTime = 0.01

# Nose
nose = vtk.vtkConeSource()
nose.SetHeight( 3.0 )
nose.SetRadius( 1.0 )
nose.SetResolution(100)

noseMapper = vtk.vtkPolyDataMapper()
noseMapper.SetInputConnection(nose.GetOutputPort())

noseActor = vtk.vtkActor()
noseActor.SetMapper(noseMapper)
noseActor.GetProperty().SetColor(255 / 255, 153 / 255, 51 / 255)

# Head
head = vtk.vtkSphereSource()
head.SetRadius(headRadius)
head.SetThetaResolution(100)
head.SetPhiResolution(100)

headMapper = vtk.vtkPolyDataMapper()
headMapper.SetInputConnection(head.GetOutputPort())

headActor = vtk.vtkActor()
headActor.SetMapper(headMapper)
headActor.GetProperty().SetColor(1, 1, 1)

# Body
body = vtk.vtkSphereSource()
body.SetRadius(7.)
body.SetThetaResolution(100)
body.SetPhiResolution(100)

bodyMapper = vtk.vtkPolyDataMapper()
bodyMapper.SetInputConnection(body.GetOutputPort())

bodyActor = vtk.vtkActor()
bodyActor.SetMapper(bodyMapper)
bodyActor.GetProperty().SetColor(1, 1, 1)

# Eyes
eyeLeft = vtk.vtkSphereSource()
eyeLeft.SetRadius(1.)
eyeLeft.SetThetaResolution(100)
eyeLeft.SetPhiResolution(100)

eyeLeftMapper = vtk.vtkPolyDataMapper()
eyeLeftMapper.SetInputConnection(eyeLeft.GetOutputPort())

eyeLeftActor = vtk.vtkActor()
eyeLeftActor.SetMapper(eyeLeftMapper)
eyeLeftActor.GetProperty().SetColor(0, 0, 0)


eyeRight = vtk.vtkSphereSource()
eyeRight.SetRadius(1.)
eyeRight.SetThetaResolution(100)
eyeRight.SetPhiResolution(100)

eyeRightMapper = vtk.vtkPolyDataMapper()
eyeRightMapper.SetInputConnection(eyeRight.GetOutputPort())

eyeRightActor = vtk.vtkActor()
eyeRightActor.SetMapper(eyeRightMapper)
eyeRightActor.GetProperty().SetColor(0, 0, 0)

# Camera
camera = vtk.vtkCamera()
camera.SetFocalPoint(0, 0, 0)
camera.SetPosition(0, 0, 120)

# Renderer
renderer= vtk.vtkRenderer()
renderer.AddActor(noseActor)
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
 
# Init position
noseActor.SetPosition(10, 0, 0)
noseActor.RotateZ(-90)

headActor.SetPosition(-15,0,0)

bodyActor.SetPosition(0,0,0)

eyeLeftActor.SetPosition(3,11,4)
eyeLeftActor.SetVisibility(False)

eyeRightActor.SetPosition(-3,11,4)
eyeRightActor.SetVisibility(False)


# Animations
def noseMove():
    noseTransform = vtk.vtkTransform()
    noseActor.SetUserTransform(noseTransform)
    
    for i in range(0, 90):
        time.sleep(sleepTime)
        
        noseTransform.RotateWXYZ(-1, 0, 1, 0)  # -1 deg on the world axis Y
        renWin.Render()
    
    for i in range(0, 90):
        time.sleep(sleepTime)
        
        noseTransform.RotateWXYZ(1, 0, 0, 1)  # 1 deg on the world axis Z. The coordinates change with the transformation
        renWin.Render()

    factor = 20 # to smooth the animation
    for i in range(0, int(headRadius * factor)+ 10):
        time.sleep(sleepTime)

        noseTransform.Translate(0, -1 / factor, 0)
        renWin.Render()

def moveHead():
    headTransform = vtk.vtkTransform()
    headActor.SetUserTransform(headTransform)

    for i in range(0, 90):
        time.sleep(sleepTime)

        headTransform.RotateWXYZ(-1, 0, 0, 1)
        renWin.Render()

    factor = 20 # to smooth the animation
    for i in range(0, int(headRadius * factor)):
        time.sleep(sleepTime)

        headTransform.Translate(1 / factor, 0, 0)
        renWin.Render()

def setEyesVisibility() :
    eyeRightActor.SetVisibility(True)
    eyeLeftActor.SetVisibility(True)

def rollCamera(angle, sign = 1) :
    move = 1 * sign
    for i in range(0, angle):
        time.sleep(sleepTime)

        camera.Roll(move)
        renWin.Render()

def azimuthCamera(angle, sign = 1) :
    
    move = 1 * sign
    for i in range(0, angle):
        time.sleep(sleepTime)

        camera.Azimuth(move)
        renWin.Render() 

def elevationCamera(angle, sign= 1) :
    move = 1 * sign
    for i in range(0, angle):
        time.sleep(sleepTime)

        camera.Elevation(move)
        renWin.Render() 

def updateAll():

    moveHead()
    noseMove()
    setEyesVisibility()
    rollCamera(360, -1)
    azimuthCamera(360)
    elevationCamera(90)
    elevationCamera(90, -1)


updateAll()
iren.Start()


