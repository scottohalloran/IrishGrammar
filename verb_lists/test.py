infinitive = 'achtáil'
simple_past_array = list(infinitive)
	# Simple past independent stem will be the same as infinitive
if(
	simple_past_array[0] == 'l'
	or simple_past_array[0] == 'n' 
	or simple_past_array[0] == 'r' 
	or simple_past_array[:1] == 'sc' 
	or simple_past_array[:1] == 'sm'
	or simple_past_array[:1] == 'sc' 
	or simple_past_array[:1] == 'sc'
	):
	simple_past_independent_stem = infinitive
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
	simple_past_independent_stem = 'd\'' + infinitive
# Simple past stem will be infinitive with d' in front of it and f lenited
elif(simple_past_array[0] == 'f'):
	simple_past_array.insert(1,'h')
	simple_past_independent_stem = 'd\'' + ''.join(simple_past_array)

print(simple_past_independent_stem)
