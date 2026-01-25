import emoji

def main():
    emoji_name= input("Inputs: ")
    print(f"Output: {emoji.emojize(emoji_name, language='alias')}")

main()