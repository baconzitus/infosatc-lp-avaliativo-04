def conferir(nome_normal,nome_invertido):
    if nome_invertido == nome_normal[::-1]: #da pra usar --in-- no lugar do ==
        return True
    else:
        return False

nome_normal= input("nome normal:")
nome_invertido=input("nome ivertido:")

verdade = conferir(nome_normal,nome_invertido)
print("verdadeiro:",verdade)