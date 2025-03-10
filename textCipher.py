import random
import string
def generateRandomLetters(length):
    random_string=''.join(random.choices(string.ascii_letters+string.digits,k=length))
    return random_string
def encode(code):
    words=code.split(" ")
    for i in range(len(words)):
        if(len(words[i])<3):
            words[i]=words[i][::-1]+" "
        else:
            prefix=generateRandomLetters(3)
            suffix=generateRandomLetters(3)
            words[i]=prefix+words[i][1:len(words[i])] +words[i][0]+suffix+" " 
    message=""
    for i in range(len(words)):
        message+=words[i]
    return message
def decode(code):
    words=code.split(" ")
    for i in range(len(words)):
        if(len(words[i])<3):
            words[i]=words[i][::-1]+" "
        else:
            words[i]=words[i][-4]+words[i][3:-4]+" "
    message=""
    for i in range(len(words)):
        message+=words[i]
    return message
y="yes"   
while(y=="yes") :
    code=input("Enter your message to encode or decode: ")
    function=input("write 'E' if you want to encode and 'D' if you want to decode: ")


    if(function.upper()=="E"):
         print("Encoded message is :", encode(code))
    elif(function.upper()=="D"):
        print("Decoded message is :", decode(code))
    else:
        print("select a correct option")
    y=input('Do you want to use this on any other message (yes/no): ').strip().lower()
    

 
