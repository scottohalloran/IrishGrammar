'''
Pulls a list of conjugated Irish verbs from http://www.teanglan.ie and writes to 
a CSV file.
'''
import csv
import requests
import re
from bs4 import BeautifulSoup

input_file = open('verblist.csv', 'r')
output_file = open('conjugated_verbs.csv','w')
#delete contents of output file if it exists
output_file.write('')
output_file.close()
output_file = open('conjugated_verbs.csv','a')


error_file = open('error.txt','w')
#delete contents of error file if it exists
error_file.write('')
error_file.close()
error_file = open('error.txt','a')
#Read headword and English from input CSV file
csv_input = csv.reader(input_file, delimiter=',')
for verb in csv_input:
	headword = verb[0]
	verb_english = verb[1] 
	verb_type = verb[2]
	verb_class = verb[3]
	verb_conjugation = verb[4]
	#Create string to hold verb conjugation and eventually write to output file
	output_file_string = headword + "," + verb_english+ "," + verb_type + "," + verb_class+ "," + verb_conjugation + ","
	URL = 'https://www.teanglann.ie/en/gram/' + headword
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'html.parser')
################################################################################
# Verbal Noun
################################################################################
	for header in soup.find_all('h3', text=re.compile('VERBAL NOUN')):
	    section = header.parent
	    verbal_noun_resultset = section.find_all(class_='value primary')
	    for verbal_noun in verbal_noun_resultset:
	    	output_file_string += "," + verbal_noun.text
################################################################################
# Verbal Adjective
################################################################################

	for header in soup.find_all('h3', text=re.compile('VERBAL ADJECTIVE')):
	    section = header.parent
	    verbal_adjective_resultset = section.find_all(class_='value primary')
	    for verbal_adjective in verbal_adjective_resultset:
	    	output_file_string += "," + verbal_adjective.text
################################################################################
# Past Tense
################################################################################

	simple_past_array = []
	simple_past = soup.find(id='past')
	if simple_past == None:
		error_file.write(headword + '\n')
		#continue
	else:
		simple_past_elements = simple_past.find_all(class_='block introd')
		for simple_past_element in simple_past_elements:
			element_array = simple_past_element.text.replace('1', '').replace('2', '').replace('3', '').replace('▪', '').strip().split('\n')
			for element in element_array:
				simple_past_array.append(element)
		
		for word in simple_past_array:
			output_file_string += ',' + word
		
################################################################################
# Present Tense
################################################################################

	present_array = []
	present = soup.find(id='present')
	if present == None:
		continue
	else:
		present_elements = present.find_all(class_='block introd')
		for present_element in present_elements:
			element_array = present_element.text.replace('1', '').replace('2', '').replace('3', '').replace('▪', '').strip().split('\n')
			for element in element_array:
				present_array.append(element)
		
		for word in present_array:
			output_file_string += ',' + word
		

################################################################################
# Future Tense
################################################################################

	future_array = []
	future = soup.find(id='future')
	if future == None:
		continue
	else:
		future_elements = future.find_all(class_='block introd')
		for future_element in future_elements:
			element_array = future_element.text.replace('1', '').replace('2', '').replace('3', '').replace('▪', '').strip().split('\n')
			for element in element_array:
				future_array.append(element)
		
		for word in future_array:
			output_file_string += ',' + word
		 

################################################################################
# Conditional Mood
################################################################################

	conditional_array = []
	conditional = soup.find(id='condi')
	if conditional == None:
		continue
	else:
		conditional_elements = conditional.find_all(class_='block introd')
		for conditional_element in conditional_elements:
			element_array = conditional_element.text.replace('1', '').replace('2', '').replace('3', '').replace('▪', '').strip().split('\n')
			for element in element_array:
				conditional_array.append(element)
		
		for word in conditional_array:
			output_file_string += ',' + word
		

################################################################################
# Past Continual Tense
################################################################################

	past_continual_array = []
	past_continual = soup.find(id='pastConti')
	if past_continual == None:
		continue
	else:
		past_continual_elements = past_continual.find_all(class_='block introd')
		for past_continual_element in past_continual_elements:
			element_array = past_continual_element.text.replace('1', '').replace('2', '').replace('3', '').replace('▪', '').strip().split('\n')
			for element in element_array:
				past_continual_array.append(element)
		
		for word in past_continual_array:
			output_file_string += ',' + word
		

################################################################################
# Imperative Mood
################################################################################

	imperative_array = []
	imperative = soup.find(id='imper')
	if imperative == None:
		continue
	else:
		imperative_elements = imperative.find_all(class_='block introd')
		for imperative_element in imperative_elements:
			element_array = imperative_element.text.replace('1', '').replace('2', '').replace('3', '').replace('▪', '').strip().split('\n')
			for element in element_array:
				imperative_array.append(element)
		
		for word in imperative_array:
			output_file_string += ',' + word
		 

################################################################################
# Present Subjunctive Mood
################################################################################

	present_subjunctive_array = []
	present_subjunctive = soup.find(id='subj')
	if present_subjunctive == None:
		continue
	else:
		present_subjunctive_elements = present_subjunctive.find_all(class_='block introd')
		for present_subjunctive_element in present_subjunctive_elements:
			element_array = present_subjunctive_element.text.replace('1', '').replace('2', '').replace('3', '').replace('▪', '').strip().split('\n')
			for element in element_array:
				present_subjunctive_array.append(element)
		
		for word in present_subjunctive_array:
			output_file_string += ',' + word
	output_file_string += "\n"
	output_file.write(output_file_string) 




output_file.close()



