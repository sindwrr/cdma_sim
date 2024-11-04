import numpy as np


# генерирует коды Уолша
def gen_walsh(n):
    if n < 0:
        raise Exception("Размер матрицы не может быть меньше 2^0=1")
    if n == 0:
        return np.array([[1]])
    H = gen_walsh(n - 1)
    return np.block([[H, H], [H, -H]])


# переводит слово в бинарное представление по ASCII
def word_to_binary(word):
    return [int(bit) for char in word for bit in format(ord(char), "08b")]


# переводит бинарное представление обратно в слово
def binary_to_word(binary_seq):
    chars = [binary_seq[i : i + 8] for i in range(0, len(binary_seq), 8)]
    return "".join(chr(int("".join(map(str, bits)), 2)) for bits in chars)


# кодирует сигнал для каждой базовой станции
def encode_signal(binary_message, code):
    return [bit * code for bit in binary_message]


# суммирует все сигналы в один
def sum_signals(spread_signals):
    return np.sum(spread_signals, axis=0)


# декодирует сигнал
def decode_signal(received_signal, code):
    return np.array(
        [
            np.sign(np.dot(received_signal[i], code))
            for i in range(len(received_signal))
        ]
    )
