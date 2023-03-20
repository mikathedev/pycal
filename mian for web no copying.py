def mfbwn():
    num = int(input("multipled by?"))
    ans = num * numerator
    
    print(str(ans)+"/"+str(denomanater))

def mfbf():
    numerator2 = int(input(" what is the second numerator"))
    denomanater2 = int(input("what is the second denomanater"))
    ansnumarater = str(numerator*numerator2)
    ansdenoinater = str(denomanater*denomanater2)
    print(ansnumarater+"/"+ansdenoinater)
    

def af():
    numerator2 = int(input(" what is the second numerator"))
    denomanater2 = int(input("what is the second denomanater"))
    if denomanater == denomanater2:
        ansdenoanater = denomanater

    else:
        ansdenoanater = denomanater*denomanater2
    ansnumarater = numerator+numerator2
    
    print(str(ansnumarater)+"/"+str(ansdenoanater))



numerator = int(input(" what is the numerator"))
denomanater = int(input("what is the denomanater"))
qwe = input("what to do 1 for multiplying by whole nums 2 for multiplying fractions \n 3 for adding fractions")
if int(qwe) == 1:
    mfbwn()

elif int(qwe) == 2:
    mfbf()

elif int(qwe) == 3:
    af()
