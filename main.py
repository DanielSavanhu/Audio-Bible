import pyttsx3

engine = pyttsx3.init()

def read(search, book):
    engine = pyttsx3.init()

    for u in book:
        if u[0:len(search) ].rstrip() == search:
            print(u)
            engine.say(u)
            engine.runAndWait()


while True:
    search = input('Please enter verse:\n e.g Genesis 1:20, Genesis, Genesis 5\n ')
    search.lstrip().rstrip()
    scripture = search.split(' ')[0].rstrip()
    text = str(open('Bible/' + scripture + '.txt', 'rt').read())
    book = text.split('\n')
    read(search, book)
    print(book)
