word = str(input("pls enter word\n"))
new = ""
for i in range(len(word)):
    if word[i] == word[i].upper():
        new = new+(word[i].lower())
    else:
        new = new+(word[i].upper())
print(new)