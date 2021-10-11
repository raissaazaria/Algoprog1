# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
g = 9,8
F = int(input("Input force value: "))
m = int(input("Input mass value:"))

sinTh = float(F/m/g)

Th = math.asin(sinTh)
Th = math.degrees(Th)

print("The angle of the ramp is:", Th )
print("%.2f" %Th)

