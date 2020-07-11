from django.shortcuts import render
from verbs.models import Verb
from pages.views import home
from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
#To pull from CSV file
import csv, io

# Create your views here.
def verbs(request):
	"""main verb page"""
	verblist = []
	allVerbs = Verb.objects.all()
	for verb in allVerbs:
		verblist.append(verb.headword)
	return render(request, "verbs.html", {"verblist":verblist})

def verbconjugator(request):
	result=request.GET['verb']
	checkboxSimplePast = forms.CheckboxInput
	checkboxPresent = forms.CheckboxInput
	checkboxFuture = forms.CheckboxInput
	checkboxConditional = forms.CheckboxInput
	checkboxHabitualPast = forms.CheckboxInput
	checkboxImperative = forms.CheckboxInput
	checkboxPresentSubjunctive = forms.CheckboxInput
	conjugatedVerb = Verb.objects.get(headword=result)
	return render(request, "verbconjugator.html",{'verb':conjugatedVerb})

def verb_upload(request):    
	# declaring template
	template = "verb_upload.html"
	data = Verb.objects.all()
	# prompt is a context variable that can have different values depending on their context
	prompt = {
	'order': 'Upload CSV of conjugated verbs',
	'verbs': data    
	      }
	# GET request returns the value of the data with the specified key.
	if request.method == "GET":
		return render(request, template, prompt)    
	csv_file = request.FILES['file']    
	# let's check if it is a csv file
	if not csv_file.name.endswith('.csv'):
		messages.error(request, 'THIS IS NOT A CSV FILE')    
	data_set = csv_file.read().decode('UTF-8')   
	# setup a stream which is when we loop through each line we are able to handle a data in a stream
	io_string = io.StringIO(data_set)
	next(io_string)
	for column in csv.reader(io_string, delimiter=',', quotechar="|"):
			_, created = Verb.objects.update_or_create(
					headword = column[0],
					english = column[1],
					verbType = column[2],
					verbClass = column[3],
					verbConjugation = column[4],
					verbalNoun = column[5],
					verbalAdjective = column[6],
					simplePast1stPersonSingInd = column[7],
					simplePast1stPersonSingInter = column[8],
					simplePast1stPersonSingNeg = column[9],
					simplePast2ndPersonSingInd = column[10],
					simplePast2ndPersonSingInter = column[11],
					simplePast2ndPersonSingNeg = column[12],
					simplePast3rdPersonSingInd = column[13],
					simplePast3rdPersonSingInter = column[14],
					simplePast3rdPersonSingNeg = column[15],
					simplePast3rdPersonSingFemInd = column[16],
					simplePast3rdPersonSingFemInter = column[17],
					simplePast3rdPersonSingFemNeg = column[18],
					simplePast1stPersonPlInd = column[19],
					simplePast1stPersonPlInter = column[20],
					simplePast1stPersonPlNeg = column[21],
					simplePast1stPersonPlIndAlt = column[22],
					simplePast1stPersonPlInterAlt = column[23],
					simplePast1stPersonPlNegAlt = column[24],
					simplePast2ndPersonPlInd = column[25],
					simplePast2ndPersonPlInter = column[26],
					simplePast2ndPersonPlNeg = column[27],
					simplePast3rdPersonPlInd = column[28],
					simplePast3rdPersonPlInter = column[29],
					simplePast3rdPersonPlNeg = column[30],
					simplePast3rdPersonPlIndAlt = column[31],
					simplePast3rdPersonPlInterAlt = column[32],
					simplePast3rdPersonPlNegAlt  = column[33],
					simplePastImpersonalPos = column[34],
					simplePastImpersonalInter = column[35],
					simplePastImpersonalNeg = column[36],
					present1stPersonSingInd = column[37],
					present1stPersonSingInter = column[38],
					present1stPersonSingNeg = column[39],
					present2ndPersonSingInd = column[40],
					present2ndPersonSingInter = column[41],
					present2ndPersonSingNeg = column[42],
					present3rdPersonSingInd = column[43],
					present3rdPersonSingInter = column[44],
					present3rdPersonSingNeg = column[45],
					present3rdPersonSingFemInd = column[46],
					present3rdPersonSingFemInter = column[47],
					present3rdPersonSingFemNeg = column[48],
					present1stPersonPlIndAlt = column[49],
					present1stPersonPlInterAlt = column[50],
					present1stPersonPlNegAlt = column[51],
					present1stPersonPlInd = column[52],
					present1stPersonPlInter = column[53],
					present1stPersonPlNeg = column[54],
					present2ndPersonPlInd = column[55],
					present2ndPersonPlInter = column[56],
					present2ndPersonPlNeg = column[57],
					present3rdPersonPlInd = column[58],
					present3rdPersonPlInter = column[59],
					present3rdPersonPlNeg = column[60],
					presentImpersonalPos = column[61],
					presentImpersonalInter = column[62],
					presentImpersonalNeg = column[63],
					future1stPersonSingInd = column[64],
					future1stPersonSingInter = column[65],
					future1stPersonSingNeg = column[66],
					future2ndPersonSingInd = column[67],
					future2ndPersonSingInter = column[68],
					future2ndPersonSingNeg = column[69],
					future3rdPersonSingInd = column[70],
					future3rdPersonSingInter = column[71],
					future3rdPersonSingNeg = column[72],
					future3rdPersonSingFemInd = column[73],
					future3rdPersonSingFemInter = column[74],
					future3rdPersonSingFemNeg = column[75],
					future1stPersonPlIndAlt = column[76],
					future1stPersonPlInterAlt = column[77],
					future1stPersonPlNegAlt = column[78],
					future1stPersonPlInd = column[79],
					future1stPersonPlInter = column[80],
					future1stPersonPlNeg = column[81],
					future2ndPersonPlInd = column[82],
					future2ndPersonPlInter = column[83],
					future2ndPersonPlNeg = column[84],
					future3rdPersonPlInd = column[85],
					future3rdPersonPlInter = column[86],
					future3rdPersonPlNeg = column[87],
					futureImpersonalPos = column[88],
					futureImpersonalInter = column[89],
					futureImpersonalNeg = column[90],
					conditional1stPersonSingInd = column[91],
					conditional1stPersonSingInter = column[92],
					conditional1stPersonSingNeg = column[93],
					conditional2ndPersonSingInd = column[94],
					conditional2ndPersonSingInter = column[95],
					conditional2ndPersonSingNeg = column[96],
					conditional3rdPersonSingInd = column[97],
					conditional3rdPersonSingInter = column[98],
					conditional3rdPersonSingNeg = column[99],
					conditional3rdPersonSingFemInd = column[100],
					conditional3rdPersonSingFemInter = column[101],
					conditional3rdPersonSingFemNeg = column[102],
					conditional1stPersonPlIndAlt = column[103],
					conditional1stPersonPlInterAlt = column[104],
					conditional1stPersonPlNegAlt = column[105],
					conditional1stPersonPlInd = column[106],
					conditional1stPersonPlInter = column[107],
					conditional1stPersonPlNeg = column[108],
					conditional2ndPersonPlInd = column[109],
					conditional2ndPersonPlInter = column[110],
					conditional2ndPersonPlNeg = column[111],
					conditional3rdPersonPlIndAlt = column[112],
					conditional3rdPersonPlInterAlt = column[113],
					conditional3rdPersonPlNegAlt = column[114],
					conditional3rdPersonPlInd = column[115],
					conditional3rdPersonPlInter = column[116],
					conditional3rdPersonPlNeg = column[117],
					conditionalImpersonalPos = column[118],
					conditionalImpersonalInter = column[119],
					conditionalImpersonalNeg = column[120],
					habitualPast1stPersonSingInd = column[121],
					habitualPast1stPersonSingInter = column[122],
					habitualPast1stPersonSingNeg = column[123],
					habitualPast2ndPersonSingInd = column[124],
					habitualPast2ndPersonSingInter = column[125],
					habitualPast2ndPersonSingNeg = column[126],
					habitualPast3rdPersonSingInd = column[127],
					habitualPast3rdPersonSingInter = column[128],
					habitualPast3rdPersonSingNeg = column[129],
					habitualPast3rdPersonSingFemInd = column[130],
					habitualPast3rdPersonSingFemInter = column[131],
					habitualPast3rdPersonSingFemNeg = column[132],
					habitualPast1stPersonPlIndAlt = column[133],
					habitualPast1stPersonPlInterAlt = column[134],
					habitualPast1stPersonPlNegAlt = column[135],
					habitualPast1stPersonPlInd = column[136],
					habitualPast1stPersonPlInter = column[137],
					habitualPast1stPersonPlNeg = column[138],
					habitualPast2ndPersonPlInd = column[139],
					habitualPast2ndPersonPlInter = column[140],
					habitualPast2ndPersonPlNeg = column[141],
					habitualPast3rdPersonPlIndAlt = column[142],
					habitualPast3rdPersonPlInterAlt = column[143],
					habitualPast3rdPersonPlNegAlt = column[144],
					habitualPast3rdPersonPlInd = column[145],
					habitualPast3rdPersonPlInter = column[146],
					habitualPast3rdPersonPlNeg = column[147],
					habitualPastImpersonalPos = column[148],
					habitualPastImpersonalInter = column[149],
					habitualPastImpersonalNeg = column[150],
					imperative1stPersonSingInd = column[151],
					imperative1stPersonSingNeg = column[152],
					imperative2ndPersonSingInd = column[153],
					imperative2ndPersonSingNeg = column[154],
					imperative3rdPersonSingInd = column[155],
					imperative3rdPersonSingNeg = column[156],
					imperative3rdPersonSingFemInd = column[157],
					imperative3rdPersonSingFemNeg = column[158],
					imperative1stPersonPlInd = column[159],
					imperative1stPersonPlNeg = column[160],
					imperative1stPersonPlIndAlt = column[161],
					imperative1stPersonPlNegAlt = column[162],
					imperative2ndPersonPlInd = column[163],
					imperative2ndPersonPlNeg = column[164],
					imperative3rdPersonPlInd = column[165],
					imperative3rdPersonPlNeg = column[166],
					imperative3rdPersonPlIndAlt = column[167],
					imperative3rdPersonPlNegAlt = column[168],
					imperativeImpersonalPos = column[169],
					imperativeImpersonalNeg = column[170],
					presentSubjunctive1stPersonSingInd = column[171],
					presentSubjunctive1stPersonSingNeg = column[172],
					presentSubjunctive2ndPersonSingInd = column[173],
					presentSubjunctive2ndPersonSingNeg = column[174],
					presentSubjunctive3rdPersonSingInd = column[175],
					presentSubjunctive3rdPersonSingNeg = column[176],
					presentSubjunctive3rdPersonSingFemInd = column[177],
					presentSubjunctive3rdPersonSingFemNeg = column[178],
					presentSubjunctive1stPersonPlInd = column[179],
					presentSubjunctive1stPersonPlNeg = column[180],
					presentSubjunctive1stPersonPlIndAlt  = column[181],
					presentSubjunctive1stPersonPlNegAlt  = column[182],
					presentSubjunctive2ndPersonPlInd = column[183],
					presentSubjunctive2ndPersonPlNeg = column[184],
					presentSubjunctive3rdPersonPlInd = column[185],
					presentSubjunctive3rdPersonPlNeg = column[186],
					presentSubjunctiveImpersonalPos = column[187],
					presentSubjunctiveImpersonalNeg = column[188]

				)
	context= {}
	return render(request,template,context)







