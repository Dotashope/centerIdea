
import wikipedia
import re

topic = input("Request the center idea for(be precise): ")
result = wikipedia.search(topic, results=1)



text = wikipedia.page(result[0]).content

sentences = re.split('[.!?]', text)

middleIndex = int((len(sentences) - 1)/2)

print (sentences[middleIndex])


#from bs4 import BeautifulSoup
#import requests
#page = requests.get(link)
#link = wikipedia.page(result[0]).url
#soup = BeautifulSoup(page.content,'html.parser')

#list(soup.children)
#print(page.status_code)

#print(page.content)

#print(soup.prettify())

#print(soup.find_all('p'))

#print('\n\n')
#print(soup.find_all('p')[0].get_text)