b=10
try:
    c=10/b
    print("try completed")
except:
    print("Cant devided by zero")
print("Program completed")

b=0
try:
    c=10/b
    print("try completed")
except ZeroDivisionError:
    print("Cant devided by zero")
print("Program completed")