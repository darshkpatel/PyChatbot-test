import random


#Greetings Shown When program first run
greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']



#List Of Questions , Add more by adding q-n and a-n
q1 = 'how are'
a1 = [' I am Okay, how are you ?',"how are you ?"]

q2 = 'who are'
a2 = ['who are what ?',"well you dont know that?"]

q3 = 'no'
a3 = ['no what ?',"are you telling a computer no ?","Hey ! u said no to me ?"]

q3 = 'yes'
a3 = ['are you sure u spell it Y.e.s ?',"yes what ?","hmm .. say else ?"]


#Responses to print when the question is not in library
error = ['ok.', 'hmmm i see', 'well , tell me about something new']

while True:
        userInput = raw_input(">>> ")
        a = userInput.lower()
        print a
        if a in greetings:
                random_greeting = random.choice(greetings)
                print(random_greeting)
        elif q1 in a:
                random_response = random.choice(a1)
                print(random_response)
        elif q2 in a:
                random_response = random.choice(a2)
                print(random_response)
        elif q3 in a:
                random_response = random.choice(a3)
                print(random_response)
        else:
                random_reply = random.choice(error)
                print(random_reply)
