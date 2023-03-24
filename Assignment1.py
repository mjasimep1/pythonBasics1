#1.Write a Python program to sum all the items in a list.

list=[25,5,30,20,10]
y=0
for x in list:
    y=y+x
print("Sum of all the items is: ",y)

#2.Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

list=["Banana","Malayalam","abca","12341","Orange","America"]
convertedList=[]
count=0
for x in list:
    convertedList.append(x.lower())
for item in convertedList:
    if len(item)>2 and item[0]==item[-1]:
        count=count+1
print("Count is: ",count)

#3.Write a Python program to remove duplicates from a list

list=["Banana","Orange","Apple","Grape","Banana"]
newList = []
for x in list:
    if x not in newList:
        newList.append(x)
print("Duplicates removed list: ",newList)


