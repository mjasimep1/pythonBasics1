for i in range(10):
    print(i + 1)

'''age, name = 36, 'vivek'
txt = "My name is John, and I am {}"
#print(txt.format(age))
print(f"My name is John, and I am {age}")'''


def function1(age, name):
    print("My name is {1}, and I am {0}".format(age, name))
function1(20, 'vivek')

i=25
j="this is test {} sample"
print(j.format(i))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


