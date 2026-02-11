#Using lambda with sorted()

students = [("Emil", 74), ("Bekarys", 100), ("Linus", 82)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True) #lambda  x:x[1] tells to sort elements by value, and reverse=true will sort it in descending order
print(sorted_students)
