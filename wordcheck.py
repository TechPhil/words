import re
file = open("words_alpha.txt","r")
words=file.readlines()

badLetters = r"[gkmqvwxz]"
longestWord=[]
maxLength=0

for line in words:
    line=line.strip()
    if re.search(badLetters, line, re.IGNORECASE):
##        print(line+" - Has Bad Letters")
        continue
    elif len(line)<maxLength:
##        print(line+" - Too short!")
        continue
    else:
        if len(line)==maxLength:
            longestWord.append(line)
            print(line+" - OK! - Same length as previous longest.")
            print("Current longest words - ")
            print(longestWord)
        else:
            longestWord.clear()
            print(line+" - OK! - NEW LONGEST")
            longestWord.append(line)
            maxLength=len(line)
