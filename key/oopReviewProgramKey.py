import oopReviewClassKey as o
# 1) create a class called 'Pet' and give it the following attributes. The user should assign the values of the attributes. Make sure the attributes are hidden
'''
type (string) ex: 'dog'
weight (string) ex: '24.7 lbs'
limbs (int) ex: 4
age (float) ex: 2.5
name (string) ex: 'Dug'
'''

# 2) in your class, create get methods for each of the attributes



# 3) Create 3 different instances of your class. These can be whatever you would like them to be, as long as they are different.
dog = o.Pet('dog','26 lbs', 4, .10, 'Dug')
cat = o.Pet('cat', '12.6 lbs', 4, 3, 'George')
bird = o.Pet('bird', '1.2 lbs', 2, 6, 'Polly')


# 4) Create a dictionary called 'pets' that has the pet name as the key, and the rest of the attributes as the values in a list
pets = {}
pets[dog.getName()] = [dog.getType(),dog.getWeight(),dog.getLimbs(),dog.getAge()]
pets[cat.getName()] = [cat.getType(),cat.getWeight(),cat.getLimbs(),cat.getAge()]
pets[bird.getName()] = [bird.getType(),bird.getWeight(),bird.getLimbs(),bird.getAge()]

# 5) Create a new method of your class called 'move.' This should have the user assign a value and the method will multiply it by the limbs attribute.
# create a get attribute for this method.



# 6) print out the distance each of your pets move
dog.move(5)
print(dog.getMove())
cat.move(2)
print(cat.getMove())
bird.move(10)
print(bird.getMove())

# 7) create a csv file called 'pets.csv' with the following format. Use the dictionary
'''
name,type,weight,limbs,age
'''

outfile = open('pets.csv','w')

outfile.write('name,type,weight,limbs,age\n')

for key in pets:
    outfile.write(key + ',')
    outfile.write(pets[key][0] + ',')
    outfile.write(pets[key][1] + ',')
    outfile.write(str(pets[key][2]) + ',')
    outfile.write(str(pets[key][3]) + '\n')

outfile.close()