'''
Pulls a list of conjugated Irish verbs from http://www.teanglan.ie and writes to 
a CSV file.
'''
import sys
import csv
import requests
import re
from bs4 import BeautifulSoup

input_noun = sys.argv[1]
input_english = '' 
for english in sys.argv[2:]:
	input_english += english 
	input_english += ' '

output_file = open('declined_noun.csv','w')
#delete contents of output file if it exists
output_file.write('')
output_file.close()
output_file = open('declined_noun.csv','w')


error_file = open('noun_error.txt','w')
#delete contents of error file if it exists
error_file.write('')
error_file.close()
error_file = open('noun_error.txt','a')

#Create string to hold noun and eventually write to output file
output_file_string = input_noun + "\t" + input_english + "\t"
URL = 'https://www.teanglann.ie/en/gram/' + input_noun
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

		 

################################################################################
# Parse Noun
################################################################################

noun_array = []
noun_gender = ''
noun_declension = ''
noun_description = soup.find('div', class_='header')
descriptions = noun_description.find_all(class_='value')
for description in descriptions :
	if description.text == 'MASCULINE':
		noun_gender = 'm'
	elif description.text == 'FEMININE':
		noun_gender = 'f'
	elif description.text == '1st DECLENSION':
		noun_declension = '1'
	elif description.text == '2nd DECLENSION':
		noun_declension = '2'
	elif description.text == '3rd DECLENSION':
		noun_declension = '3'
	elif description.text == '4th DECLENSION':
		noun_declension = '4'
	print("description  is " + str(description))
noun_parts = soup.find('div', class_='content')
parts = noun_parts.find_all(class_='line')
for part in parts:
	noun_array.append(part.text)
output_file_string += noun_gender
output_file_string += '\t'
output_file_string += noun_declension
output_file_string += '\t'
output_file_string += noun_array[0]
output_file_string += '\t'
output_file_string += noun_array[2]
output_file_string += '\t'
#if the noun has a plural
if len(noun_array) > 4:
	output_file_string += noun_array[4]
	output_file_string += '\t'
	output_file_string += noun_array[6]
#print(noun_parts)
'''
		present_subjunctive_elements = present_subjunctive.find_all(class_='block introd')
		for present_subjunctive_element in present_subjunctive_elements:
			element_array = present_subjunctive_element.text.replace('1', '').replace('2', '').replace('3', '').replace('▪', '').strip().split('\n')
			for element in element_array:
				present_subjunctive_array.append(element)
		
		for word in present_subjunctive_array:
			output_file_string += ',' + word
			'''
output_file_string += "\n"
output_file.write(output_file_string) 




output_file.close()



