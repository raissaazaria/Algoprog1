# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

x1 = float(input("Enter x1 value:"))
x2 = float(input("Enter x2 value:"))
y1 = float(input("Enter y1 value:"))
y2 = float(input("Enter y2 value:"))


slope=  "[:.5f]".format((y2-y1)/(x2-x1))
print("The slope for the line that connects two points (",x1, "," , y1 , ") and (",x2, ",", y2, ") is" , slope)
