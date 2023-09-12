def codificador(ci):
    codigo = ""
    cod_input = str(ci)
    i = 0
    while i < len(cod_input):
        cont = 1
        while i < len(cod_input)-1 and cod_input[i] == cod_input[i+1]:
            cont +=1
            i += 1
        if cont > 1:
            codigo += "!" +str(cont)
        else:
            codigo += cod_input[i]
        i += 1
    return codigo

retorno = codificador(10400000000234)
print(retorno)