import webbrowser
print("What address are you trying to find?")
address = input()
address = address.replace(" ", "+")

webbrowser.open('https://www.google.com/maps/place/' + address)