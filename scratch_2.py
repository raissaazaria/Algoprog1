flag = True

while (flag):
    temp= int(input("Enter temperature value: "))
    if (-58 < temp < 41 ):
        flag = False
    else :
        print("Enter a valid value:")