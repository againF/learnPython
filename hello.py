# with open('hello.py','r') as file:
#     print(file.read())

# with open('hello.py','r') as file:
#     for line in file:
#         print(line.strip())

def zeroError():
    try:
        return 1/0
    except ZeroDivisionError:
        print("Zero Division Error")
    else:
        print("No error")
    finally:
        print("This is the end of the program")
zeroError()

from math import sqrt
print(sqrt(4))