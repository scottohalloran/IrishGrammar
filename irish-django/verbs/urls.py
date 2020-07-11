#urls.py for verbs app
from django.urls import path
from . import views

urlpatterns = [
	path('verbs/', views.verbs, name='verbs'),
	path('verb_upload/', views.verb_upload, name='verb_upload'),
	path('verbconjugator/', views.verbconjugator, name='verbconjugator'),
	

 ]
