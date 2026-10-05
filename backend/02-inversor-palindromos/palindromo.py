def palindromo_o_no(frase):
    # limpio el texto
    texto_lmp = frase.lower().replace(" ", "")
    # leo la cadena de forma inversa
    texto_invertido = texto_lmp[::-1]

    if texto_lmp == texto_invertido:
        print("ES un palindromo")
    else:
        print("NO es un palindromo")

texto = input("Ingresa una palabra o frase: ")
palindromo_o_no(texto)

# tambien podia hacer lo de leer la cadena con un for para mas paso a paso pero q ladilla mi broti