import vtk

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

headT = vtk.vtkTransform()
headT.Translate(-10, 0, -10)

headTF = vtk.vtkTransformFilter()
headTF.SetInputConnection(head.GetOutputPort())
headTF.SetTransform(headT)

headMapper = vtk.vtkPolyDataMapper()
headMapper.SetInputConnection(headTF.GetOutputPort())

headActor = vtk.vtkActor()
headActor.SetMapper(headMapper)
headActor.GetProperty().SetColor(1, 1, 1)
headActor.SetPosition([-20, 0, 0])


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
bodyActor.SetPosition([0,0,0])

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
eyeLeftActor.SetPosition([5, 5, 0])


eyeRight = vtk.vtkSphereSource()
eyeRight.SetRadius(2.)
eyeRight.SetThetaResolution(10)
eyeRight.SetPhiResolution(10)

eyeRightMapper = vtk.vtkPolyDataMapper()
eyeRightMapper.SetInputConnection(eyeRight.GetOutputPort())

eyeRightActor = vtk.vtkActor()
eyeRightActor.SetMapper(eyeRightMapper)
eyeRightActor.GetProperty().SetColor(0, 0, 0)
eyeRightActor.SetPosition([-5,-5,0])

# Renderer
ren1= vtk.vtkRenderer()
ren1.AddActor(coneActor)
ren1.AddActor(headActor)
ren1.AddActor(bodyActor)
ren1.AddActor(eyeLeftActor)
ren1.AddActor(eyeLeftActor)
ren1.SetBackground(0.1, 0.2, 0.4)

# Renderer Window
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer( ren1 )
renWin.SetSize( 300, 300 )

# Interactive mode
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
style = vtk.vtkInteractorStyleTrackballCamera()
iren.SetInteractorStyle(style)

iren.Initialize()
iren.Start()

for i in range(0, 360):
    time.sleep(0.03)

    renWin.Render()
    headTF.SetTransform(headT)

