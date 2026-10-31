import math


def get_coordinates() -> tuple:
    while True:
        s = input("Enter new coordinates as floats in format 'x,y,z': ")
        crd = []
        crd = s.split(",")
        if len(crd) == 0:
            print("Invalid syntax")
        valid_c = 0
        invalid_c = 0
        invalid_list = []
        i = 0
        while i < len(crd):
            try:
                float(crd[i])
                valid_c = 1
            except ValueError:
                invalid_c = 1
                invalid_list.append(i)
            i += 1
        if valid_c == 1 and invalid_c == 1:
            for j in invalid_list:
                print(f"Error on parameter '{crd[j]}'"
                      f": could not convert string to float: '{crd[j]}'")
        elif invalid_c and valid_c == 0:
            print("Invalid syntax")
        else:
            crdt = []
            i = 0
            while i < len(crd):
                crdt.append(float(crd[i]))
                i += 1
            return (tuple(crdt))


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first_c = get_coordinates()
    print(f"Got a first tuple: ({first_c[0]}, {first_c[1]}, {first_c[2]})")
    print(f"It includes: X={first_c[0]}, Y={first_c[1]}, Z={first_c[2]}")
    d = math.sqrt(first_c[0]**2 + first_c[1]**2 + first_c[2]**2)
    print(f"Distance to center: {round(d, 4)}\n")
    print("Get a second set of coordinates")
    second_c = get_coordinates()
    d = math.sqrt((first_c[0] - second_c[0])**2 +
                  (first_c[1] - second_c[1])**2 +
                  (first_c[2] - second_c[2])**2)
    print(f"Distance between the 2 sets of coordinates: {round(d, 4)}")
