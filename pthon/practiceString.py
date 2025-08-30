import datetime

name = input("Enter your name: ")
now = datetime.datetime.now()

print(f"""Good morning {name}

Today is {now.strftime("%A, %d %B %Y")}
Current time is {now.strftime("%I:%M %p")}""")
