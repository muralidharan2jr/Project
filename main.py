""" Python program which accepts the radius of a circle from the user and computes area."""

import math

radius = float(input("Enter the Radius of the circle : "))

area = math.pi * radius * radius
print("The area of the circle with radius 1.1 is: {0}".format(area))

""" Python program to accept a filename from the user and print the extension of that. """

filename = input("Input the Filename : ")

extension = filename.split(".")

print("The extension of the file is : ", extension[-1] if len(extension) > 1 else "Unknown Extension")


""" Python program to accept a filename from the user and print the extension of that. """

filename = input("Input the Filename : ")

extension = filename.split(".")

print("The extension of the file is : " + repr(extension[-1]))