""" Lesson 10 exercises """

''' Exercises to read a text file and print out each line
stock_filename = 'Lesson6_Data - Stocks.txt'

with open(stock_filename) as file_object:
	# Stores the data in the text file in a list
	lines = file_object.readlines()
	
	# Print each line of the stock file
for line in lines:
	print(line.rstrip())
	


# Exercise to write to a file	
program_output_filename = 'Blue.Sean.Assignment-report-6.txt'

with open(program_output_filename, 'w') as file_object:
	file_object.write("I love Python!")

	
# Exercise to append to a file

program_output_filename = 'Blue.Sean.Assignment-report-6.txt'

with open(program_output_filename, 'a') as file_object:
	file_object.write("Last day of week five of the Python course!\n")
	file_object.write("This is for exercise 10 practice.\n")


# Exercis to practice exception handling for reading a file

stock_filename = 'Lesson61_Data - Stocks.txt'

try:
	with open(stock_filename) as file_object:
		# Stores the data in the text file in a list
		lines = file_object.readlines()
	
	# Print each line of the stock file
	for line in lines:
		print(line.rstrip())
		
except FileNotFoundError:
	msg = "Sorry, the file " + stock_filename + " does not exists."
	print(msg)
	


filePath = "someFile.txt"

fileObject = open(filePath, "a")

languageList = ['C#', 'Java', 'Ruby', 'PHP']
for language in languageList:
   print (language)
   fileObject.write(language)

fileObject.close()


filenames = ['audi.txt', 'ford.txt']

for filename in filenames:
    
    try:
        with open(filename) as f:
            contents = f.read()

    except FileNotFoundError:
        pass

    else:
        print(contents)
'''


filePath = "numFile.txt"

fileObject = open(filePath, "r")

for line in fileObject:
    lineSegments = line.split(',')
    for segment in lineSegments:
        print (segment)



