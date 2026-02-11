class player:     
    speed=5          #we create properties for our class after declaring it
    weight=50

p1=player() #We call the class 'player' and create new object named 'p1'

print(p1.speed) #prints '5'
print(p1.weight) #prints '50'

#As we saw, it does holds the general values from the class

p2=player() 
p2.speed=30
p2.weight=60 #We create a new object for the same class, but we can give it different property values from the class

print(p2.speed) #prints 30
print(p2.weight) #prints 60