# coding=utf-8
from __future__ import print_function
from _plotly_future_ import orca_defaults
import time
import vtk


def main():
    colors = vtk.vtkNamedColors()
    cone = vtk.vtkConeSource()
    cone.SetHeight(3.0)
    cone.SetRadius(1.0)
    cone.SetResolution(10)
    coneMapper = vtk.vtkPolyDataMapper()
    coneMapper.SetInputConnection(cone.GetOutputPort())

    #
    # Create an actor
    coneActor = vtk.vtkActor()
    coneActor.SetMapper(coneMapper)
    coneActor.GetProperty().SetColor(colors.GetColor3d("Peacock"))
    coneActor.GetProperty().SetDiffuse(0.7)
    coneActor.GetProperty().SetSpecular(0.4)
    coneActor.GetProperty().SetSpecularPower(20)


    # second actor.
    property = vtk.vtkProperty()
    property.SetColor(colors.GetColor3d("Tomato"))
    property.SetDiffuse(0.7)
    property.SetSpecular(0.4)
    property.SetSpecularPower(20)

    coneActor2 = vtk.vtkActor()
    coneActor2.SetMapper(coneMapper)
    # coneActor2.GetProperty().SetColor(colors.GetColor3d("Peacock"))
    coneActor2.SetProperty(property)
    coneActor2.SetPosition(0, 2, 0)


    ren1 = vtk.vtkRenderer()
    ren1.AddActor(coneActor)
    ren1.AddActor(coneActor2)
    ren1.SetBackground(colors.GetColor3d("Black"))


    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(ren1)
    renWin.SetSize(720, 680)
    renWin.SetStereoCapableWindow(1)

    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)


    ren1.GetActiveCamera().Elevation(30)
    ren1.ResetCamera()
    for i in range(0, 3600):
        time.sleep(0.03)

        renWin.Render()
        ren1.GetActiveCamera().Azimuth(1)

    iren.Start()


if __name__ == "__main__":
    main()
