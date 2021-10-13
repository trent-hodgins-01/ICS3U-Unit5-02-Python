# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 10/13/2021
# This is the triangle area calculator program
# The user enters in the base and height in cm
# The program displays the area


def calculate_area(base, height):
    # calculate area

    area = 0

    # process
    area = (base * height) / 2

    # output
    print("\nArea is {0} cm²".format(area))


def main():
    # this function gets length and width

    # input
    base_as_string = input("Enter in base(cm): ")
    height_as_string = input("Enter in height(cm): ")

    try:
        base = int(base_as_string)
        height = int(height_as_string)

        # call functions
        calculate_area(base, height)
        print("\nDone.")

    except Exception:
        print("\nInvalid input")


if __name__ == "__main__":
    main()
