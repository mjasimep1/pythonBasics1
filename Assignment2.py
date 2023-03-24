# 1.Write a Python program to check if all dictionaries in a list are empty or not.

with_data_list = [{7058: 'sravan', 7059: 'jyothika'}, {"name": 'harsha', "place": 'clct'}, {}]
empty_list = [{}, {}, {}, {}]
i = 0;
for x in empty_list:
    if not x:
        i = i + 1
if i == len(empty_list):
    print("All dictionaries in the list are empty")
else:
    print("All dictionaries in the list are not empty")

# 2.Write a Python program to extend a list without append.

master_list = ["Banana", "Apple", "Orange"]
list_for_add = master_list + ["grape"]
master_list.extend(["Tomato"])
print("Extended list without append: ", master_list)

# 3.Write a Python program to find the list in a list of lists whose sum of elements is the highest

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [12, 14, 20], [2, 3, 4]]
#print(max(list_of_lists))
newList = []
for x in list_of_lists:
    newList.append(sum(x))
    if max(newList) == (sum(x)):
        list_of_lists = x
print("Lists whose sum of elements is the highest: ", list_of_lists)

# 4.Write a Python program to access dictionary key’s element by index

dict = {"name": "John", "place": "Ernakulam", "age": "32", "id": "B234"}
key_list = []
for key in dict.keys():
    key_list.append(key)
print("Dictionary key’s element by index 1 is: ", key_list[2])

key_list1=list(dict.keys())
print("Second method for getting the key from dict by using index: ",key_list1[1])

# 5.Write a Python program to remove duplicates from a list - Instead of creating a new list, try to find a solution within the list itself.

master_list = ["Banana", "Orange", "Banana", "Apple", "Grape", "Banana"]
repeated_list=[1,2,3,4,2,3,5,6,3,2,4,5,3,4,6]
#print(list(set(list)))
for x in set(repeated_list):
    for i in range(1, repeated_list.count(x)):
        repeated_list.remove(x)
print("Duplication removed list: ",repeated_list)


