import time

import vtk

""" class vtkTimerCallback():
    def __init__(self, steps, actor, iren):
        self.timer_count = 0
        self.steps = steps
        self.actor = actor
        self.iren = iren
        self.timerId = None

    def execute(self, obj, event):
        step = 0
        while step < self.steps:
            print(self.timer_count)
            self.actor.SetPosition(self.timer_count / 100.0, self.timer_count / 100.0, 0)
            iren = obj
            iren.GetRenderWindow().Render()
            self.timer_count += 1
            step += 1
        if self.timerId:
            iren.DestroyTimer(self.timerId)

    def moveHead():
        step = 0
        while step < self.steps:

 """

# Camera
camera = vtk.vtkCamera()
camera.SetFocalPoint(0, 0, 0)
camera.SetPosition(0, 0, 20)
camera.SetViewUp(0, 1, 0) # maybe not useful

# Renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.1, 0.2, 0.4)
renderer.SetActiveCamera(camera)

# Add world axes
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
renderer.AddActor(coneActor)

# Head

# head = vtk.vtkSphereSource()
# head.SetRadius(5.)
# head.SetThetaResolution(10)
# head.SetPhiResolution(10)

# headT = vtk.vtkTransform()
# headT.RotateX(60)
# headT.Translate(-10, 0, -10)

# headTF = vtk.vtkTransformFilter()
# headTF.SetInputConnection(head.GetOutputPort())
# headTF.SetTransform(headT)

# headMapper = vtk.vtkPolyDataMapper()
# headMapper.SetInputConnection(headTF.GetOutputPort())

# headActor = vtk.vtkActor()
# headActor.SetMapper(headMapper)
# headActor.GetProperty().SetColor(1, 1, 1)
# headActor.SetPosition([-20, 0, 0])
# renderer.AddActor(headActor)


# # Body

# body = vtk.vtkSphereSource()
# body.SetRadius(7.)
# body.SetThetaResolution(10)
# body.SetPhiResolution(10)

# bodyMapper = vtk.vtkPolyDataMapper()
# bodyMapper.SetInputConnection(body.GetOutputPort())

# bodyActor = vtk.vtkActor()
# bodyActor.SetMapper(bodyMapper)
# bodyActor.GetProperty().SetColor(1, 1, 1)
# bodyActor.SetPosition([0,0,0])

# renderer.AddActor(bodyActor)

# # Eyes

# eyeLeft = vtk.vtkSphereSource()
# eyeLeft.SetRadius(2.)
# eyeLeft.SetThetaResolution(10)
# eyeLeft.SetPhiResolution(10)

# eyeLeftMapper = vtk.vtkPolyDataMapper()
# eyeLeftMapper.SetInputConnection(eyeLeft.GetOutputPort())

# eyeLeftActor = vtk.vtkActor()
# eyeLeftActor.SetMapper(eyeLeftMapper)
# eyeLeftActor.GetProperty().SetColor(0, 0, 0)
# eyeLeftActor.SetPosition([5, 5, 0])


# eyeRight = vtk.vtkSphereSource()
# eyeRight.SetRadius(2.)
# eyeRight.SetThetaResolution(10)
# eyeRight.SetPhiResolution(10)

# eyeRightMapper = vtk.vtkPolyDataMapper()
# eyeRightMapper.SetInputConnection(eyeRight.GetOutputPort())

# eyeRightActor = vtk.vtkActor()
# eyeRightActor.SetMapper(eyeRightMapper)
# eyeRightActor.GetProperty().SetColor(0, 0, 0)
# eyeRightActor.SetPosition([-5, -5, 0])

# renderer.AddActor(eyeLeftActor)
# renderer.AddActor(eyeLeftActor)


iren.Initialize()
""" 
cb = vtkTimerCallback(200, headActor, iren)
iren.AddObserver('TimerEvent', cb.execute)
cb.timerId = iren.CreateRepeatingTimer(500) """

# for i in range(0,10):
#     time.sleep(0.50)

#     renWin.Render()
#     headT.Translate(1,1,0)
#     headT.RotateZ(1)



iren.Start()

