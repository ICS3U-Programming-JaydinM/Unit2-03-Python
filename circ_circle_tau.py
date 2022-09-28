#!/usr/bin/env python3
# Made by: Jaydin Madore
# Made on: 2022-09-28
# This program asks the user for the radius in cm
# then calculates and displays circumference of a circle
import math

import constants


def main():
    # input
    print("calculator for circumference")
    radius = float(input("Enter the radius of your circle in cm: "))
    9
    # process
    circumference = constants.TAU * radius

    # output
    print("")
    print("circumference = {} cm".format(circumference))


if __name__ == "__main__":
    main()
