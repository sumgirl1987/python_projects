from math import ceil


def square(side):
    area = side * side
    if side != int(side):
        return ceil(area)
    else:
        return area


side = float(input("Введите сторону квадрата: ").replace(',', '.'))
print(f"Площадь квадрата: {square(side)}")
