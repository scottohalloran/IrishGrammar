'''
Pulls a list of conjugated Irish verbs from http://www.teanglan.ie and writes to 
a CSV file.
'''
import sys
import csv
import requests
import gspread
from bs4 import BeautifulSoup
#Connect to Google Sheets and open Worksheet
gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1p64P57jLJdIFkOicnGyzK4MJZiLplyVIfZLD6U6QHdo')
worksheet = sh.sheet1

#Enter the Irish and English separated by semicolons
input_adjective = sys.argv[1:]
input_adjective_string =''
for word in input_adjective:
	input_adjective_string += word
	input_adjective_string += ' '
input_adjective_array = input_adjective_string.split(',,')

#Anything to the left of the input double comma is considered the Irish
adjective_masculine_nominative = input_adjective_array[0]
adjective_english = input_adjective_array[1]
output_file = open('declined_adjective.csv','w')
#delete contents of output file if it exists
output_file.write('')
output_file.close()
output_file = open('declined_adjective.csv','w')


error_file = open('adjective_error.txt','w')
#delete contents of error file if it exists
error_file.write('')
error_file.close()
error_file = open('adjective_error.txt','a')

#Create string to hold adjective and eventually write to output file
output_file_string = ''


URL = 'https://www.teanglann.ie/en/gram/' + adjective_masculine_nominative
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')


################################################################################
# Parse adjective
################################################################################

adjective_array = []
adjective_gender = ''
adjective_declension = ''
adjective_description = soup.find('div', class_='header')
descriptions = adjective_description.find_all(class_='value')
for description in descriptions :
	if description.text == '1st DECLENSION':
		adjective_declension = '1'
	elif description.text == '2nd DECLENSION':
		adjective_declension = '2'
	elif description.text == '3rd DECLENSION':
		adjective_declension = '3'
adjective_parts = soup.find('div', class_='content')
parts = adjective_parts.find_all(class_='line')
for part in parts:
	adjective_array.append(part.text)
output_file_string += adjective_gender
output_file_string += '\t'
output_file_string += adjective_declension
output_file_string += '\t'
for adjective in adjective_array:
	output_file_string += adjective
	output_file_string += '\t'

#print(adjective_parts)
			
output_file_string += "\n"
output_file.write(output_file_string) 


output_file.close()



