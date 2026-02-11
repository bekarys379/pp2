#Using lambda with filter()

numbers=[1,2,3,4,5,6,7]

even_numbers=list(filter(lambda x:x%2==0, numbers)) #filter() only keeps the even numbers by checking them through lambda function

print(even_numbers)