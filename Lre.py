def codificador(cod_input):
    codigo = ""
    i = 0
    caracter = ""
    while i < len(cod_input):
        cont = 1
        while i < len(cod_input)-1 and cod_input[i] == cod_input[i+1]:
            cont +=1
            i += 1
            caracter = cod_input[i]
        if cont > 1:
            codigo += "!" +str(cont) + caracter
        else:
            codigo += cod_input[i]
        i += 1
    return codigo


def decodificador(codigo_input):
    decodificado = ""
    i = 0
    while i < len(codigo_input):
        if codigo_input[i] == "!":
            cont = ""
            i += 1
            while i < len(codigo_input) and codigo_input[i].isdigit():
                cont += codigo_input[i]
                i += 1
            caracter = codigo_input[i]
            decodificado += caracter * int(cont)
        else:
            decodificado += codigo_input[i]
        i += 1
    return decodificado

codigo = "ABCCCCCCCDA"
print("Código ", codigo)
print("Código codificado:", codificador(codigo))
codigo_decodificado = decodificador(codigo)
print("Código Decodificado:", codigo_decodificado)