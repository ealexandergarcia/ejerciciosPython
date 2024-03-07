word = input("Ingrese palabra: ")
word = word.replace(" ","")
wordR = word[::-1]

if word == wordR:
    print("Es palindromo")
else:
    print("No es palindromo")
