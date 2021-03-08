import requests
from bs4 import BeautifulSoup

class conversation:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        return "질문: " + self.question + "\n답변: " + self.answer + '\n'

def get_subjects():
    subjects = []

    req = requests.get('https://basicenglishspeaking.com/daily-english-conversation-topics/')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    divs = soup.findAll('div', {"class": "tcb-flex-col"})
    for div in divs:
        links = div.findAll('a')

        for link in links:
            subject = link.text
            subjects.append(subject)

    return subjects
#    print(html)

subjects = get_subjects()
print(len(subjects))
print(subjects)

for i in range(1, 11):
    conversations = []

    print('(', i, '/', len(subjects), ')', subjects[i])
    req = requests.get('https://basicenglishspeaking.com/'+subjects[i])
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    qnas = soup.findAll('div', {"class": "sc_player_container1"})

    for qna in qnas:
        if qnas.index(qna) % 2 == 0:
            q = qna.next_sibling
        else:
            a = qna.next_sibling
            c = conversation(q, a)
            conversations.append(c)
    
    for c in conversations:
        print(str(c))


#print(len(conversations))
#for c in conversations:
 #   print(str(c))
