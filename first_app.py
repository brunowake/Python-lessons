import random

print("Enter your name: ")
nome = input()
print("Hello, "+nome)
pontos = 0;
while 0 == 0:
    entrada = input()
    if entrada == "!exit":
        print("Bye!")
        break
    elif entrada != "scissors" and entrada != "paper" and entrada != "rock" and entrada != "!rating":
        print("Invalid input")
    elif entrada=="!rating":
        cont = 1
    else:
        n = random.random() * 2

        if n <= 1:
            n="scissors"
        elif n>1 and n<= 2:
            n="paper"
        else:
            n="rock"

        if entrada == n:
            print("There is a draw "+'('+n+')')
        elif (entrada == "paper" and n=="scissors") or (entrada == "rock" and n=="paper") or (entrada=="scissors" and n=="rock"):
            print("Sorry, but computer chose "+ n)
        else:
            print("Well done. Computer chose "+ n +" and failed")
            print(pontos)
            pontos = pontos + 50