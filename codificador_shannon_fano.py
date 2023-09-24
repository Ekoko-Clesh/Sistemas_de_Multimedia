# Formatação para cor no terminal
class Cor:
    RESET = '\033[0m'
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    ROXO = '\033[95m'
    CIANO = '\033[96m'



def calcular_frequencia(texto):
    frequencia = {}

    for char in texto:
        if char in frequencia:
            frequencia[char] += 1
        else:
            frequencia[char] = 1

    return frequencia

def shannon_fano(frequencies):
    if len(frequencies) == 1:
        return {frequencies[0][0]: "0"}
    soma_freq = 0
    frequencies = sorted(frequencies, key=lambda x: x[1], reverse=True) # Ordena os caracteres consoante as frequencias (Modo descendente)
    for freq in frequencies:
        soma_freq += freq[1]
    total_frequency = soma_freq

    half_frequency = total_frequency / 2
    group1, group2 = [], []
    group1_freq, group2_freq = 0, 0
    for char, freq in frequencies:
        if group1_freq + freq <= half_frequency:
            group1.append((char, freq))
            group1_freq += freq
        else:
            group2.append((char, freq))
            group2_freq += freq

    encoding = {} # variavel para armazenar os códigos
    for char, code in shannon_fano(group1).items(): # recursão para iterar os ítens da lista group 1
        encoding[char] = "0" + code
    for char, code in shannon_fano(group2).items(): # recursão para iterar os ítens da lista group 2
        encoding[char] = "1" + code

    return encoding


def read_data():
    texto = ''
    try:
        with open('data.txt','r') as file:
            for c in file.readlines():
                for v in c:
                    texto += v
        return texto
    except FileNotFoundError:
        print("Ficheiro inexistente, forneça nome correcto ")

texto = read_data()
print(f"{Cor.VERMELHO}INFORMAÇÃO : {texto} {Cor.RESET}")
char_frequencies = calcular_frequencia(texto)
frequencies = list(char_frequencies.items())
encoding_table = shannon_fano(frequencies)
print(f'{Cor.VERDE}Símbolo\t\tFrequência\t\t\tCódigo\t\t\tBit(s){Cor.RESET}')
for value in encoding_table:
    print(value,'\t\t\t', char_frequencies[value], '\t\t\t\t\t',encoding_table[value], '\t\t\t', len(encoding_table[value]))
