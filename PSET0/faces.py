def main():
    val = input("")
    convert(val)

def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    print(text)

main()
