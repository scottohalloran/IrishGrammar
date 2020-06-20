from django.shortcuts import render
from verbs.models import Verb
from pages.views import home
from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms

# Create your views here.
def verbs(request):
	"""main verb page"""
	verblist = []
	allVerbs = Verb.objects.all()
	for verb in allVerbs:
		verblist.append(verb.infinitive)
	return render(request, "verbs.html", {"verblist":verblist})

def verbconjugator(request):
	result=request.GET['verbs']
	checkboxSimplePast = forms.CheckboxInput
	checkboxPresent = forms.CheckboxInput
	checkboxFuture = forms.CheckboxInput
	checkboxConditional = forms.CheckboxInput
	checkboxHabitualPast = forms.CheckboxInput
	checkboxImperative = forms.CheckboxInput
	checkboxPresentSubjunctive = forms.CheckboxInput
	conjugatedVerb = Verb.objects.get(infinitive=result)
	return render(request, "verbconjugator.html",{'verbs':conjugatedVerb})




