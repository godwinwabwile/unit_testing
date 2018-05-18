import unittest
from circlearea import circleArea
from math import pi


class TestCircleArea(unittest.TestCase):
  def test_Area(self):
    #test areas with radius >=0
    assertAlmostEqual(circleArea(1),pi)
    assertAlmostEqual(circleArea(0),0)
    assertAlmostEqual(circleArea(2.5),pi*2.5**2)

  def test_values(self):
    assertRaises(ValueError, circleArea, -1)
  def test_types(self):
    assertRaises(TypeError, circleArea, True)
    assertRaises(TypeError, circleArea, 3+5j)
    assertRaises(TypeError, circleArea, "radius")

if __name__ == '__main__':
unittest.main()
  
