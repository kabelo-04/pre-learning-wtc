greeting = input("Greeting: ").lower().strip()
cleaned = ""

for char in greeting:
    if char not in ".,?!":
        cleaned += char

if cleaned.startswith("hello"):
    print("$0")
elif cleaned.startswith("h"):
    print("$20")
else:
    print("$100")