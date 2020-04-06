import  requests
from bs4 import BeautifulSoup
import pyttsx3

def synonym(urword):    #gives synonyms of the word 

    web = requests.get("https://www.thesaurus.com/browse/" + urword + "?s=t")
    soup = BeautifulSoup(web.text, 'html.parser')
    common = soup.find_all('a', attrs={'class':'css-18rr30y etbu2a31'})
    some = soup.find_all('a', attrs={'class':'css-7854fb etbu2a31'})
    uncommon = soup.find_all('a', attrs={'class':'css-4ypury etbu2a31'})

    for word in range(len(common)):
        print(common[word].text, "\n")

    for word in range(len(some)):
        print(some[word].text, "\n")

    for word in range(len(uncommon)):
        print(uncommon[word].text, "\n")

def definition(urword):   #gives definitions of the word 

    web = requests.get("https://www.lexico.com/en/definition/" + urword)
    soup = BeautifulSoup(web.text, 'html.parser')
    defin = soup.find_all('span', attrs={'class':'ind'})

    for word in range(len(defin)):
        print(str(word + 1) + ". " + defin[word].text, "\n")

def origin(urword):     #gives origin of the word 

    web = requests.get("https://www.lexico.com/en/definition/" + urword)
    soup = BeautifulSoup(web.text, 'html.parser')
    origin = soup.find_all('div', attrs={'class':'senseInnerWrapper'})

    print(origin[len(origin)-1].text, "\n")

def pronounciation(urword):     #gives pronunciation of the word 
 
    pro = pyttsx3.init()
    pro.say(urword)

    pro.runAndWait()
