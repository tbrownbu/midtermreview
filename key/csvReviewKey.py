import csv
# 1) Open 'csvFile.csv' and read through the contents. Wait for user input inbetween each employee. Print with the following output:
'''

Employee Name: John Smith
Years of service: 2 years
Current pay: $100,000

'''

infile = open('csvFile.csv','r')
reader = csv.reader(infile, delimiter=',')

next(reader)

for row in reader:
    name = row[0]
    years = row[1] + ' years'
    pay = format(int(row[2]),',')

    print('Employee name:',name)
    print('Years of service:', years)
    print('Current pay:', '$' + pay)
    #input()

infile.close()

# 2) create a new csv file called wacoRestaurants.csv using the dictionary. Make a header "Restaurant,Rating"
restaurants = {
    "Shorty's": 4.6,
    "Hawk's": 3.9,
    "Schlotzsky's": 3.8,
    "The Mix Cafe": 4.5,
    "Fuego": 4.6,
    "Slow Rise": 4.5,
    "Twisted Root": 3.9,
    "In-n-out": 3.7,
    "Torchy's": 4.6
}

outfile = open('wacoRestaurants.csv', 'w',newline='')
writer = csv.writer(outfile, delimiter=',')

header = ['Restaurant','Rating']
writer.writerow(header)

for key in restaurants:
    writer.writerow([key,restaurants[key]])

outfile.close()

# 3) using the csv file you just created, read through it and print out restaurants if they have a rating below a 4.0
# Create a new dictionary with the name as the key and rating as the value. Print the dictionary

infile = open('wacoRestaurants.csv','r')
reader = csv.reader(infile, delimiter=',')

next(reader)

newDict = {}

for row in reader:
    if float(row[1]) < 4.0:
        newDict[row[0]] = row[1]

print(newDict)

infile.close()    

# 4) using 'csvFile.csv,' read through the file and tally up the total salary of all employees and print out the total and average

infile = open('csvFile.csv','r')
reader = csv.reader(infile, delimiter=',')

next(reader)

total = 0
employees = 0

for row in reader:
    total += float(row[2])
    employees += 1

average = total/employees

print('Total Salary:', format(float(total), ',.2f'))
print('Average Salary:', format(average,',.2f'))
