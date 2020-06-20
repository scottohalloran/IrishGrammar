#urls.py for verbs app
from django.urls import path
from . import views

urlpatterns = [
	path('', views.verbs, name='verbs'),
	path('verbconjugator', views.verbconjugator, name='verbconjugator'),
 ]
