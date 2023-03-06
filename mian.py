
import pyperclip, cal
numerator = int(input(" what is the numerator"))
denomanater = int(input("what is the denomanater"))
num = int(input("multipled by?"))
ans = num * numerator
pyperclip.copy(str(ans)+"/"+str(denomanater))
print(str(ans)+"/"+str(denomanater)+" has been copied to clipboard")
