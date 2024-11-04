from defs import *


def main():
    print("\n===== Симулятор CDMA =====")
    print("\nВведите слова для 4-х станций, которые вы хотите передать:")

    # пользователь вводит слова
    init_words = dict()
    init_words["A"] = input("A: ")
    init_words["B"] = input("B: ")
    init_words["C"] = input("C: ")
    init_words["D"] = input("D: ")

    # переводим слова в бинарное представление с битами вида -1 и 1
    binary_messages = {
        station: np.array(word_to_binary(word)) * 2 - 1
        for station, word in init_words.items()
    }

    # генерируем коды Уолша для 4-х станций
    walsh_codes = gen_walsh(3)[: len(init_words)]

    # кодируем сигналы станций
    encoded_signals = [
        np.array(encode_signal(binary_messages[station], walsh_codes[i]))
        for i, station in enumerate(init_words)
    ]

    # суммируем сигналы в один
    signal_sum = sum_signals(encoded_signals)

    # декодируем сигналы
    decoded_signals = [
        decode_signal(signal_sum, walsh_codes[i])
        for i in range(len(init_words))
    ]

    # переводим сигналы обратно в слова
    decoded_words = {
        station: binary_to_word((decoded_signals[i] + 1) // 2)
        for i, station in enumerate(init_words)
    }

    print(
        "\nКодирование и декодирование сигналов прошло успешно! Вот что услышал приемник:"
    )
    for station, word in decoded_words.items():
        print(f"{station}: {word}")

    # вывод этапов процесса
    ans = input("\nВы хотите увидеть информацию для отладки? [y/n]: ")
    while True:
        if ans in "yY":
            print("\nСлова в бинарном представлении:")
            for station, word in binary_messages.items():
                print(f'{station} ("{init_words[station]}"): {word}')

            print("\nСгенерированные коды станций:")
            for station, code in zip(binary_messages.keys(), walsh_codes):
                print(f"{station}: {code}")

            print("\nЗакодированные сигналы:")
            for station, signal in zip(binary_messages.keys(), encoded_signals):
                print(f"{station}: {signal}\n")

            print(f"Сумма сигналов:\n{signal_sum}")

            print("\nДекодированные сигналы:")
            for station, signal in zip(binary_messages.keys(), decoded_signals):
                print(f"{station}: {signal}")

            print("\nДекодированные слова:")
            for station, word in decoded_words.items():
                print(f"{station}: {word}")

            break
        elif ans in "nN":
            print("Хорошо, всего доброго!")
            break
        else:
            ans = input("Неверный ввод, попробуйте еще раз: ")

    print("\n===== Работа симулятора окончена. =====\n")


if __name__ == "__main__":
    main()
