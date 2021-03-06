import math


def area_of_a_triangle(side_a, side_b, side_c):
    parameter_of_triangle = (side_a + side_b + side_c) / 2
    area = math.sqrt(
        (
            parameter_of_triangle
            * (parameter_of_triangle - side_a)
            * (parameter_of_triangle - side_b)
            * (parameter_of_triangle - side_c)
        )
    )
    return area


def main():
    print(area_of_a_triangle(3, 4, 5))


if __name__ == "__main__":
    main()
