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
    print(codigo)

codificador('ABCCCCCCCDA')