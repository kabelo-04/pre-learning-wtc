def main():
    user_input = input("Enter your sentence: ")
    convert(user_input)

def convert(str):
    str = str.replace(":)", "🙂").replace(":(", "🙁")
    print(str)

main()
