mylist = [[1, 2, 3], [710, 920, 800], [10, 20, 30], [100, -200, 300], [500, 600, 700]]
print(max(mylist))
highest_sum = 0
highest_list = None
for x in mylist:
    current_sum = sum(x)
if current_sum > highest_sum:
    highest_sum = current_sum
    highest_list = x
print(highest_list)


list4 = ["Banana", "Orange", "Banana", "Apple", "Grape", "Banana"]
list6=[1,2,3,4,2,3,5,6,3,2,4,5,3,4,6]
print(list(set(list4)))

dict = {"name": "John", "place": "Ernakulam", "age": "32", "id": "B234"}
list1=list(dict.keys())
print(list1)
print("Dictionary key’s element by index 1 is: ", list1[1])