import  requests
from bs4 import BeautifulSoup
import pyttsx3

def synonym():    #gives synonyms of the word 
    urword = input("Type the word that you want to find synonyms for: " + "\n")

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

def definition():   #gives definitions of the word 
    urword = input("Type the word that you want to find the definition for: " + "\n")

    web = requests.get("https://www.lexico.com/en/definition/" + urword)
    soup = BeautifulSoup(web.text, 'html.parser')
    defin = soup.find_all('span', attrs={'class':'ind'})

    for word in range(len(defin)):
        print(str(word + 1) + ". " + defin[word].text, "\n")

def origin():     #gives origin of the word 
    urword = input("Type the word that you want to find the origin of language for: " + "\n")

    web = requests.get("https://www.lexico.com/en/definition/" + urword)
    soup = BeautifulSoup(web.text, 'html.parser')
    origin = soup.find_all('div', attrs={'class':'senseInnerWrapper'})

    print(origin[len(origin)-1].text, "\n")

def pronounciation():     #gives pronunciation of the word 
    urword = input("Type the word that you want to pronunciate: ")

    pro = pyttsx3.init()
    pro.say(urword)

    pro.runAndWait()

dec = input("What do you want to know about the word(synonyms, definition, origin, pronunciation): ")
if dec == "synonyms":
    synonym()
if dec == "definitions":
    definition()
if dec == "origin":
    origin()
if dec == "pronunciation":
    pronounciation()
else:
    print("Rerun the program and type: synonyms, definition, origin, pronunciation")

