#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Nov 2019
# This is program triangle calcualtre with 2 funcitons


def area(base, height):
    # This'll calcilate the area of a triangle

    # process
    area = (base * height) / 2

    # output
    print("\nThe area is " + str(area) + " units squared.")


def main():
    # This is asks for the base and hieght, then it  runs area()

    # variables
    base = 0
    height = 0

    # Welcomes user
    print("Hi, this is TRIANGLE AREA CALCULATOR.")
    input("Press Enter to continue.\n")

    while True:
        try:
            base = int(input("What is the base: "))
            height = int(input("What is the height: "))

            # runs area()
            area(base, height)
            break
        except ValueError:
            print("Invalid input. Try again.\n")


if __name__ == "__main__":
    main()
