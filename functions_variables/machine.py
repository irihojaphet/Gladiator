emoticon = "😊"

def main():
    global emoticon

    say("is anyone there?")
    emoticon = "😎"
    say("Oh, hi!")

def say(phrase):
    print(phrase, emoticon)


main()