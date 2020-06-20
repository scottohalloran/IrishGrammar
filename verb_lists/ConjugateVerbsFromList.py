'''
Takes a list of Irish verb infinitives, conjugates them and writes to 
a CSV file.
'''
import csv
input_file = open('Class1Verbs.csv', 'r')
output_file = open('conjugated_files.txt','w')
#delete contents of output file if it exists
output_file.write('')
output_file.close()
output_file = open('conjugated_files.txt','a')
irregular_verb_file = open('irregular_verbs.csv')
defective_verb_file = open('defective_verbs.csv')
verb_stem = ""
verb_ending = ""
simple_past_independent_stem = ""
simple_past_dependent_stem = ""




#############################################################################################################
#Takes the verb's infinitive and creates the verb stem to which tense endings will be added.
#############################################################################################################
def create_stem(infinitive):
	#make infinitive into an array to edit individual elements
	verb_array = list(infinitive)
	if verb_class == 'class1':
		verb_present_independent_stem = infinitive
		verb_present_negative_stem = infinitive
		verb_ending = 'broad'
	elif verb_type == 'v1b':
		verb_stem = infinitive
		verb_ending = 'slender'
	elif verb_type == 'v1bx':
		verb_stem = infinitive
		verb_ending = 'broad'
	#Verb ending needs to be broadened
	#reverse the order of the array 
	#and remove the first slender vowel
	#Reverse back and assign to verb_stem	
	elif verb_type == 'v1c ':
		verb_array.reverse()
		verb_array.remove('i')
		verb_array.reverse()
		verb_stem = ''.join(verb_array)
		#verbal noun and verbal adjective remain slender
		verbal_noun_stem = infinitive
		verbal_adjective_stem = infinitive
		verb_ending = 'broad'	
	#Verb ending needs to be broadened
	#reverse the order of the array 
	#and remove the igh
	#Reverse back and assign to verb_stem	
	elif verb_type == 'v1d':
		verb_array.reverse()
		verb_array.remove('ghi')
		verb_array.reverse()
		verb_stem = ''.join(verb_array)
		#verbal noun remains broad and verbal adjective becomes slender
		verbal_noun_stem = infinitive
		verbal_adjective_stem = infinitive + 'i'
		present_impersonal_stem = infinitive + 'i'
		verb_ending = 'broad'

	elif verb_type == 'v1e':
		verb_array.reverse()
		verb_array.remove('ghi')
		verb_array.reverse()
		verb_stem = ''.join(verb_array)
		#verbal noun remains broad and verbal adjective becomes slender
		verbal_noun_stem = infinitive
		verbal_adjective_stem = infinitive + 'i'
		present_impersonal_stem = infinitive + 'i'
		verb_ending = 'slender'


	elif verb_type == 'v1f':
		verb_array.reverse()
		verb_array.remove('ia')
		verb_array.reverse()
		verb_stem = ''.join(verb_array)
		#verbal noun remains broad and verbal adjective becomes slender
		verbal_noun_stem = verb_stem
		verbal_adjective_stem = infinitive
		present_impersonal_stem = infinitive
		verb_ending = 'broad'	

	elif verb_type == 'v1fx':
		verb_array.reverse()
		verb_array.remove('i')
		verb_array.reverse()
		verb_stem = ''.join(verb_array)
		#verbal noun remains broad and verbal adjective becomes slender
		verbal_noun_stem = verb_stem
		verbal_adjective_stem = verb_stem
		present_impersonal_stem = verb_stem
		verb_ending = 'broad'	

	elif verb_type == 'v1g':
		verb_array.reverse()
		verb_array.remove('i')
		verb_array.reverse()
		verb_stem = ''.join(verb_array)
		#verbal noun remains broad and verbal adjective becomes slender
		verbal_noun_stem = verb_stem
		verbal_adjective_stem = verb_stem
		present_impersonal_stem = verb_stem
		verb_ending = 'broad'

	elif verb_type == 'v1h':
		verb_array.reverse()
		verb_array.remove('i')
		verb_array.reverse()
		verb_stem = ''.join(verb_array)
		#verbal noun remains broad and verbal adjective becomes slender
		verbal_noun_stem = verb_stem
		verbal_adjective_stem = verb_stem
		present_impersonal_stem = verb_stem
		verb_ending = 'broad'	

	elif verb_type == 'v1x':
		verb_array.reverse()
		verb_array.remove('i')
		verb_array.reverse()
		verb_stem = ''.join(verb_array)
		#verbal noun remains broad and verbal adjective becomes slender
		verbal_noun_stem = verb_stem
		verbal_adjective_stem = verb_stem
		present_impersonal_stem = verb_stem
		verb_ending = 'broad'		

	elif verb_type == 'v2a':
		verb_array.reverse()
		verb_array.remove('i')
		verb_array.reverse()
		verb_stem = ''.join(verb_array)
		#verbal noun remains broad and verbal adjective becomes slender
		verbal_noun_stem = verb_stem
		verbal_adjective_stem = verb_stem
		present_impersonal_stem = verb_stem
		verb_ending = 'broad'	

	elif verb_type == 'v2ax':
		verb_array.reverse()
		verb_array.remove('i')
		verb_array.reverse()
		verb_stem = ''.join(verb_array)
		#verbal noun remains broad and verbal adjective becomes slender
		verbal_noun_stem = verb_stem
		verbal_adjective_stem = verb_stem
		present_impersonal_stem = verb_stem
		verb_ending = 'broad'	

	elif verb_type == 'v2c':
		verb_array.reverse()
		verb_array.remove('i')
		verb_array.reverse()
		verb_stem = ''.join(verb_array)
		#verbal noun remains broad and verbal adjective becomes slender
		verbal_noun_stem = verb_stem
		verbal_adjective_stem = verb_stem
		present_impersonal_stem = verb_stem
		verb_ending = 'broad'

	elif verb_type == 'v2d':
		verb_array.reverse()
		verb_array.remove('i')
		verb_array.reverse()
		verb_stem = ''.join(verb_array)
		#verbal noun remains broad and verbal adjective becomes slender
		verbal_noun_stem = verb_stem
		verbal_adjective_stem = verb_stem
		present_impersonal_stem = verb_stem
		verb_ending = 'broad'

	elif verb_type == 'v2d':
		verb_array.reverse()
		verb_array.remove('i')
		verb_array.reverse()
		verb_stem = ''.join(verb_array)
		#verbal noun remains broad and verbal adjective becomes slender
		verbal_noun_stem = verb_stem
		verbal_adjective_stem = verb_stem
		present_impersonal_stem = verb_stem
		verb_ending = 'broad'
#############################################################################################################
# Takes the verb's infinitive and adds the prefixes and endings of the simple past tense.
# If the verb begins with a consonant, the verb stem is made by leniting the initial 
# consonant if possible. If the infinitive begins with a vowel, d' is prefixed. Because f is not 
# pronounced when it is lenited, it is treated as a vowel and has d' prefixed to it.
# The following initial consonants or combinations cannot be lenited:
# l, n, r, sc, sm, sp, st
#############################################################################################################
def create_simple_past_stems(inf):
	simple_past_array = list(inf)
	# Simple past independent stem will be the same as infinitive
	if(
		simple_past_array[0] == 'l'
		or simple_past_array[0] == 'n' 
		or simple_past_array[0] == 'r'
		or simple_past_array[0] == 'v' 
		or simple_past_array[0] == 'z' 
		or simple_past_array[:1] == 'sc' 
		or simple_past_array[:1] == 'sm'
		or simple_past_array[:1] == 'sc' 
		or simple_past_array[:1] == 'sc'
		):
		independent_stem = inf
		negative_stem = inf
		interrogative_stem = inf
	# Simple past stem will be infinitive with d' in front of it
	elif(
		simple_past_array[0] == 'a'
		or simple_past_array[0] == 'e' 
		or simple_past_array[0] == 'i' 
		or simple_past_array[0] == 'o' 
		or simple_past_array[0] == 'u' 
		or simple_past_array[0] == 'á'
		or simple_past_array[0] == 'é' 
		or simple_past_array[0] == 'í' 
		or simple_past_array[0] == 'ó' 
		or simple_past_array[0] == 'ú' 
		):
		independent_stem  = "d\'" + inf
		negative_stem = ''.join(simple_past_array)
		interrogative_stem = ''.join(simple_past_array)
	# Simple past stem will be infinitive with d' in front of it and f lenited
	elif(simple_past_array[0] == 'f'):
		simple_past_array.insert(1,'h')
		negative_stem = "d\'" + ''.join(simple_past_array)
		dependent_stem = ''.join(simple_past_array)
		interrogative_stem = ''.join(simple_past_array)
	# Simple past stem will be infinitive with initial consonant lenited
	else:
		simple_past_array.insert(1,'h')
		independent_stem = ''.join(simple_past_array)
		negative_stem = ''.join(simple_past_array)
		interrogative_stem = ''.join(simple_past_array)
	return independent_stem, dependent_stem, interrogative_stem


'''
Read through input_file and determine what conjugation the verb is. If it is irregular read 
verb's conjugation from irregular_verb_file and write to output_file. If it is regular, conjugate it 
according to what conjugation it belongs and whether it is broad or slender.
'''
csv_input = csv.reader(input_file, delimiter=',')
for verb in csv_input:
	infinitive = verb[0]
	verb_english = verb[1] 
	verb_type = verb[2]
	verb_conjugation = verb[3]
	simple_past_independent_stem = ""
	simple_past_negative_stem = ""
	simple_past_interrogative_stem = ""
	output_file_string = ""
	simple_past_independent_stem, simple_past_dependent_stem, simple_past_interrogative_stem  = create_simple_past_stems(infinitive)
infinitive text,
english text,
verbalAdjective text,
verbalNoun text,
simplePast1stPersonSingIndep = simple_past_independent_stem + " mé"
simplePast1stPersonSingInter = simple_past_interrogative_stem + " mé"
ePast1stPersonSingNeg = simple_past_negative_stem + " mé"
simplePast2ndPersonSingPos = simple_past_independent_stem + " tú"
simplePast2ndPersonSingInter = simple_past_interrogative_stem + " tú"
simplePast2ndPersonSingNeg = simple_past_negative_stem + " tú"
simplePast3rdPersonSingPos = simple_past_independent_stem + " sé, sí"
simplePast3rdPersonSingInter = simple_past_interrogative_stem + " sé, sí"
simplePast3rdPersonSingNeg = simple_past_negative_stem + " sé, sí"
simplePast1stPersonPlPos = simple_past_independent_stem + "amar"
simplePast1stPersonPlInter = simple_past_interrogative_stem + "amar"
simplePast1stPersonPlNeg = simple_past_negative_stem + "amar"
simplePast2ndPersonPlPos text,
simplePast2ndPersonPlInter text,
simplePast2ndPersonPlNeg text,
simplePast3rdPersonPlPos text,
simplePast3rdPersonPlInter text,
simplePast3rdPersonPlNeg text,
simplePastImpersonalPos text,
simplePastImpersonalInter text,
simplePastImpersonalNeg text,
	output_file_string += infinitive 
	output_file_string += "," + verb_english
	output_file_string += "," + verbalAdjective
	output_file_string += "," + verbalNoun
	output_file_string += " independent stem is " + simple_past_independent_stem
	output_file_string += " negative stem is " + simple_past_dependent_stem
	output_file_string += " interrogative stem is " + simple_past_interrogative_stem
	output_file_string += "\n"
	#array to write to output_file
	output_file.write(output_file_string) 

output_file.close()




