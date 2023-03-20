import pyperclip
def mfbwn():
    num = int(input("multipled by?"))
    ans = num * numerator
    pyperclip.copy(str(ans)+"/"+str(denomanater))
    print(str(ans)+"/"+str(denomanater)+" has been copied to clipboard")

def mfbf():
    numerator2 = int(input(" what is the second numerator"))
    denomanater2 = int(input("what is the second denomanater"))
    ansnumarater = str(numerator*numerator2)
    ansdenoinater = str(denomanater*denomanater2)
    print(ansnumarater+"/"+ansdenoinater+"has been copied to the clip bored")
    pyperclip.copy(ansnumarater+"/"+ansdenoinater)

def af():
    numerator2 = int(input(" what is the second numerator"))
    denomanater2 = int(input("what is the second denomanater"))
    ansdenomarater = denomanater+denomanater2
    ansnumarater = numerator+numerator2
    pyperclip.copy(str(ansnumarater)+"/"+str(ansdenomarater))
    print(str(ansnumarater+"/"+ansdenomarater)+"has been copied to clip bored")



numerator = int(input(" what is the numerator"))
denomanater = int(input("what is the denomanater"))
qwe = input("what to do 1 for multiplying by whole nums 2 for multiplying fractions \n 3 for adding fractions")
if int(qwe) == 1:
    mfbwn()

elif int(qwe) == 2:
    mfbf()

elif int(qwe) == 3:
    af()

