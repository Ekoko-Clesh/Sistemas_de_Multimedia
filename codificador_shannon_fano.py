# Formatação para cor no terminal
class Cor:
    RESET = '\033[0m'  # Código para redefinir a cor
    VERMELHO = '\033[91m'  # Código para texto vermelho
    VERDE = '\033[92m'  # Código para texto verde
    AMARELO = '\033[93m'  # Código para texto amarelo
    AZUL = '\033[94m'  # Código para texto azul
    ROXO = '\033[95m'  # Código para texto roxo
    CIANO = '\033[96m'  # Código para texto ciano

# Classe para representar um nó da árvore de Shannon-Fano
class ShannonFanoNode:
    def __init__(self, symbol, frequency):
        self.symbol = symbol  # Símbolo do nó
        self.frequency = frequency  # Frequência do símbolo
        self.bitstring = ""  # Sequência de bits associada ao nó
        self.left = AlgNone  # Nó filho esquerdo
        self.right = None  # Nó filho direito

# Função para calcular as frequências dos caracteres no texto
def calculate_frequency(texto):
    frequencia = {}  # Dicionário para armazenar frequências

    for char in texto:
        if char in frequencia:
            frequencia[char] += 1
        else:
            frequencia[char] = 1

    return frequencia

# Função para ler dados de um arquivo
def read_data():
    texto = ''
    try:
        with open('data.txt','r') as file:
            for c in file.readlines():
                for v in c:
                    texto += v
        return texto
    except FileNotFoundError:
        print("Ficheiro inexistente, forneça nome correto ")

# Função que implementa o algoritmo Shannon-Fano
def shannon_fano(codes):
    if len(codes) == 1:
        return

    codes.sort(key=lambda node: node.frequency, reverse=True)  # Ordena os códigos por frequência (descendente)
    half_total_frequency = sum(node.frequency for node in codes) // 2
    current_frequency = 0
    left_symbols = []
    right_symbols = []
    for node in codes:
        if current_frequency + node.frequency <= half_total_frequency:
            left_symbols.append(node)
            current_frequency += node.frequency
        else:
            right_symbols.append(node)

    for node in left_symbols:
        node.bitstring += "0"
    for node in right_symbols:
        node.bitstring += "1"

    shannon_fano(left_symbols)  # Chamada recursiva para o lado esquerdo
    shannon_fano(right_symbols)  # Chamada recursiva para o lado direito

# Função para comprimir os dados usando o algoritmo Shannon-Fano
def compress_shannon_fano(text):
    symbol_frequencies = calculate_frequency(text)
    symbol_nodes = [ShannonFanoNode(symbol, frequency) for symbol, frequency in symbol_frequencies.items()]
    shannon_fano(symbol_nodes)  # Chama a função shannon_fano para criar a árvore

    symbol_codes = {node.symbol: node.bitstring for node in symbol_nodes}

    compressed_data = "".join(symbol_codes[symbol] for symbol in text)

    return compressed_data, symbol_nodes

# Função para descomprimir os dados usando a árvore Shannon-Fano
def decompress_shannon_fano(compressed_data, symbol_nodes):
    symbol_map = {node.bitstring: node.symbol for node in symbol_nodes}
    current_bitstring = ""
    decompressed_data = ""
    for bit in compressed_data:
        current_bitstring += bit
        if current_bitstring in symbol_map:
            decompressed_data += symbol_map[current_bitstring]
            current_bitstring = ""

    return decompressed_data

# Função para ler dados de um arquivo
def read_data(filename):
    text = ""
    with open(filename + '.txt', 'r') as file:
        for x in file.readlines():
            text += x
    return text

# Função para salvar dados comprimidos em um arquivo
def save_compressed_data(filename, compressed_data):
    with open(filename + '.txt', 'w') as file:
        file.write(compressed_data)
    print(f"Dados Comprimidos salvos com sucesso no ficheiro {filename}.txt")

# Função para salvar dados descomprimidos em um arquivo
def save_decompressed_data(filename, decompressed_data):
    with open(filename + '.txt', 'w') as file:
        file.write(decompressed_data)
    print(f"Dados Descomprimidos salvos com sucesso no ficheiro {filename}.txt")

# Lê o texto original
texto_original = read_data('data')
# Comprime o texto usando Shannon-Fano
compressed_data, shannon_fano_tree = compress_shannon_fano(texto_original)
# Descomprime os dados
decompressed_data = decompress_shannon_fano(compressed_data, shannon_fano_tree)
print("Texto original:\n", texto_original)
save_compressed_data('compressed_data', compressed_data)
save_decompressed_data('decompressed_data', decompressed_data)
