import csv
# 1) Open 'csvFile.csv' and read through the contents. Wait for user input inbetween each employee. Print with the following output:
'''


infile = open('csvFile.csv', 'r')
reader = csv.reader(infile, delimiter=',')

next(reader)

for record in reader:
    name = record[0]
    years = record[1]
    pay = format(int(record[2]),',')
    print("Employee name: ",name)
    print("Years of service: ", years)
    print("Curent pay: ","$"+pay)
    print()

infile.close()

Employee Name: John Smith
Years of service: 2 years
Current pay: $100,000

'''

# 2) create a new csv file called 'wacoRestaurants.csv' using the dictionary. Make a header "Restaurant,Rating"

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

#what is newline? What does the delimiter do? newline=''
outfile = open('wacoRestaurants.csv','w')
writer=csv.writer(outfile,delimiter=',')
header=['Restaurant','Rating']
writer.writerow(header)


for rec in restaurants:
    writer.writerow([rec,restaurants[rec]])
#why are they in brackets above^^^

outfile.close()

# 3) using the csv file you just created, read through it and print out restaurants if they have a rating below a 4.0. 
# Create a new dictionary with the name as the key and rating as the value

infile = open('wacoRestaurants.csv','r')
reader=csv.reader(infile,delimiter=',')
readfile = infile.read()

mydict = {}

for rec in reader:
    if float(rec[1]) < 4.0:
        mydict[rec[0]] = rec[1]

print(mydict)

infile.close()


# 4) using 'csvFile.csv,' read through the file and tally up the total salary of all employees and print out the total and average
