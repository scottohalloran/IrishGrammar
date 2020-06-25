import requests
from bs4 import BeautifulSoup

URL = 'https://www.teanglann.ie/en/gram/achomharc'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

past = soup.find(id='past')
past_elements = past.find_all(class_='block introd')
for past_element in past_elements:
	element = past_element.text.replace('1', '').replace('2', '').replace('3', '').replace('▪', '').strip()
	print(element)

present = soup.find(id='present')
present_elements = present.find_all(class_='block introd')
for present_element in present_elements:
	element = present_element.text.replace('1', '').replace('2', '').replace('3', '').replace('▪', '').strip()
	print(element)

future = soup.find(id='future')
future_elements = future.find_all(class_='block introd')
for future_element in future_elements:
	element = future_element.text.replace('1', '').replace('2', '').replace('3', '').replace('▪', '').strip()
	print(element)

conditional = soup.find(id='condi')
conditional_elements = conditional.find_all(class_='block introd')
for conditional_element in conditional_elements:
	element = conditional_element.text.replace('1', '').replace('2', '').replace('3', '').replace('▪', '').strip()
	print(element)

past_continual = soup.find(id='pastConti')
past_continual_elements = past_continual.find_all(class_='block introd')
for past_continual_element in past_continual_elements:
	element = past_continual_element.text.replace('1', '').replace('2', '').replace('3', '').replace('▪', '').strip()
	print(element)

imperative = soup.find(id='imper')
imperative_elements = imperative.find_all(class_='block introd')
for imperative_element in imperative_elements:
	element = imperative_element.text.replace('1', '').replace('2', '').replace('3', '').replace('▪', '').strip()
	print(element)

present_subjunctive = soup.find(id='subj')
present_subjunctive_elements = present_subjunctive.find_all(class_='block introd')
for present_subjunctive_element in present_subjunctive_elements:
	element = present_subjunctive_element.text.replace('1', '').replace('2', '').replace('3', '').replace('▪', '').strip()
	print(element)