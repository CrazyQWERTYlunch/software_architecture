from Controller.CircleController import CircleController
from Controller.RectangleController import RectangleController
from Controller.TriangleController import TriangleController

from Model.Circle import Circle
from Model.Rectangle import Rectangle
from Model.Triangle import Triangle

from View.CircleView import CircleView
from View.RectangleView import RectangleView
from View.TriangleView import TriangleView


if __name__ == "__main__":
    circle = Circle(10)
    circle_view = CircleView()
    circle_controller = CircleController(circle_view, circle)
    circle_controller.get_area()
    circle_controller.get_perimeter()

    triangle = Triangle(12, 10, 11)
    triangle_view = TriangleView()
    triangle_controller = TriangleController(triangle_view,triangle)
    triangle_controller.get_area()
    triangle_controller.get_perimeter()

    rectangle = Rectangle(2, 2)
    rectangle_view = RectangleView()
    rectangle_controller = RectangleController(rectangle_view, rectangle)
    rectangle_controller.get_area()
    rectangle_controller.get_perimeter()