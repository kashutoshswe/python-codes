import webbrowser
site = input("Enter site Name with .com or .in within double quotes      ")
site2 = 'https://www.'+site
print(site2)
webbrowser.open(site2)


