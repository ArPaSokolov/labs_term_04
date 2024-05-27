from collections import defaultdict # автоматически создает и инициализирует значение по умолчанию для отсутствующих ключей в словаре
from math import ceil, log2


class Node:
    def __init__(self, label,frequency=0):
        self.label = label
        self.frequency = frequency
        self.left = None
        self.right = None
        self.code = ""

    def __repr__(self):
        return f"{self.label}: {self.frequency}"


def codewords_making(node, code=""):
    if node.left is not None:
        node.left.code = code + "0"
        codewords_making(node.left, code + "0")
    if node.right is not None:
        node.right.code = code + "1"
        codewords_making(node.right, code + "1")


def encoding(text, codes):
    encoded_text = ""
    for ch in text:
        encoded_text += codes[ch]
    return encoded_text


def Shannon_formula(frequencies, text_length):
    shannon = 0
    for char, prob in frequencies.items():
        shannon += (prob / text_length) * log2(prob / text_length)
    return round(-1 * shannon, 6)


# Задание 1 статический анализ
freq_uniq = defaultdict(int) # частоты уникальных символов
freq_pair = defaultdict(int) # частоты пар символов
text = ""
with open("input.txt", "r") as file:
    text = file.read()
for ch in text:
    freq_uniq[ch] += 1
for i in range(0, len(text) - 1):
    freq_pair[text[i] + text[i + 1]] += 1

# Задание 2 кодировка Хаффмана
nodes = []
for k, v in freq_uniq.items():
    nodes.append(Node(k, v))
nodes.sort(key=lambda x: x.frequency) # сортируется по возрастанию частот
end_nodes = nodes.copy()
while len(nodes) != 1:
    left = nodes.pop(0)
    right = nodes.pop(0)
    node = Node(left.label + right.label, left.frequency + right.frequency)
    node.left = left
    node.right = right
    nodes.insert(0, node)
    nodes.sort(key=lambda x: x.frequency)
codewords_making(nodes[0])
codes = dict()
for node in end_nodes:
    codes[node.label] = node.code
encoded = encoding(text, codes)
freq_uniq_list = []
freq_pair_list = []
for i in freq_uniq.keys():
    freq_uniq_list.append([i, freq_uniq[i]])
for i in freq_pair.keys():
    freq_pair_list.append([i, freq_pair[i]])
print("Кол-во символов в исходном тексте: ", len(text))
print("Кол-во уникальных символов: ", len(freq_uniq_list))
with open('static.txt', 'w') as file:
    file.write("Символы и их частоты: " + str(sorted(freq_uniq_list, key=lambda frequency: frequency[1])))
    file.write("\n\n")
    file.write("Пары символов и их частоты: " + str(sorted(freq_pair_list, key=lambda frequency: frequency[1])))
    file.close()
with open('huffman_coding.txt', 'w') as file:
    file.write("Символы и их коды Хаффмана: " + str(codes))
    file.write("\n\n")
    file.write("Закодированная строка: " + encoded)
    file.close()
print("Длина закодированного текста (алгоритм Хаффмана):", len(encoded))
print("Длина при равномерном (шестибитовом) кодировании:", 6 * len(text))
print("Степень сжатия по сравнению с равномерным (шестибитовым) кодированием:",
      round(100 - (len(encoded) / (6 * len(text))) * 100, 6), "%")
print("Формула Шеннона (метод Хаффмана):", Shannon_formula(freq_uniq, len(text)), "бит")

# Задание 3 кодировка LZW
LZW_dict = dict()
i = 0
for char in codes:
    LZW_dict[char] = i
    i += 1
dictionary_size = len(LZW_dict)
init_bits = ceil(log2(dictionary_size))
string = ""
LZW_encoded = []
for char in text:
    new_string = string + char
    if new_string in LZW_dict:
        string = new_string
    else:
        LZW_encoded.append(LZW_dict[string])
        LZW_dict[new_string] = dictionary_size
        dictionary_size += 1
        string = char
if string in LZW_dict:
    LZW_encoded.append(LZW_dict[string])
LZW_encoded_res = ""
for seq in LZW_encoded:
    bits = 0
    if seq == 0:
        bits = init_bits
    elif ceil(log2(seq)) < init_bits:
        bits = init_bits
    else:
        bits = ceil(log2(seq))
    LZW_encoded_res += format(seq, f'0{bits}b')
with open('LZW_coding.txt', 'w') as file:
    file.write("Словарь: " + str(LZW_dict))
    file.write("\n\n")
    file.write("Закодированная строка (битовая): " + LZW_encoded_res)
    file.write("\n\n")
    file.write("Закодированная строка (кодовая): " + str(LZW_encoded))
    file.close()
print()
print("Длина закодированного текста (метод LZW): ", len(LZW_encoded_res))
print("Степень сжатия по сравнению с равномерным (шестибитовым) кодированием:",
      round(100 - (len(LZW_encoded_res) / (6 * len(text))) * 100, 6), "%")
print("Степень сжатия по сравнению с кодами Хаффмана:",
      round(100 - (len(LZW_encoded_res) / len(encoded)) * 100, 6), "%")
