fruits = ["apple", "banana", "grape", "orange"]

fruits[2]

print(len(fruits))

fruits.append("pear")
print(fruits)
fruits.pop()
print(fruits)

#.pop() empty removes last item, index can also be inserted.

nested_list = [1, 2, 3, 4, [5, 6, 7]]
print(nested_list[4][0])





#TASK

task_list = []
task_list.extend(["Clean Car", "Make Dinner", "Turn Washing Machine On"])
print(task_list)
task_list.pop()
print(task_list)
print(len(task_list))

#.extend allows multiple appends at once