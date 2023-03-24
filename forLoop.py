
films=["money.mp4","memories.mp4","big B.mp4"]
for x in films:
    print(x[0:-4])

for x in range(5):
    print(x)

#Assignment

i=int(input("Enter the number for multiply: "))
j=int(input("Length of the multiplication: "))
for x in range(j):
    y=x+1
    print(y ," x ", i ," = ",i*y )

i=int(input("Enter the number for multiply: "))
j=int(input("Length of the from: "))
k=int(input("to: "))
for x in range(j,k+1):
    print(x ," x ", i ," = ",i*x )