################################################################################
# Present Subjunctive Mood
################################################################################

	present_subjunctive_array = []
	past = soup.find(id='present_subjunctive')
	if present_subjunctive == None:
		error_file.write(headword + '\n')
		#continue
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