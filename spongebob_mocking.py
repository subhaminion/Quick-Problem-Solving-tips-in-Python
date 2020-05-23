string = input()

stringList = list(string.split(" "))

string2 = ''

temp = 0

#takes care of the whitespace problem so in every case only either
#the last alphabet character of a word or the first alphabet character of the next word is uppercase

for i in stringList:
    if temp % 2 == 0:
        for j in range (len(i)):
            if j % 2 == 0:
                string2 += i[j].upper()
            if j % 2 != 0:
                string2 += i[j]
        string2 += ' '
        temp += len(i)
        continue
    
    if temp % 2 != 0:
        for j in range (len(i)):
            if j % 2 == 0:
                string2 += i[j].lower()
            if j % 2 != 0:
                string2 += i[j].upper()
        string2 += ' '
        temp += len(i)
        continue
        
print(string2)
