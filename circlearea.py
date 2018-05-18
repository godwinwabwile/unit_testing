from math import pi

def circlearea(radius):
  if type(radius) not in [int; float]:
    raise TypeError("Radius must be a number")
  if radius < 0:
    raise ValueError("Radius has to be a positive number")

  return pi*radius**2
