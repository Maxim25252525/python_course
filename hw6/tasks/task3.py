"""
# Задача 3: Тофсла и Вифсла +1

Тофсла и Вифсла - два маленьких и забавных существа, говорящих на странном
труднопонимаемом языке. Они повсюду таскают с собой огромный чемодан,
содержимое которого никому не показывают.

Муми-тролль просит вас помочь ему наладить общение с Тофслой и Вифслой.

Напишите функцию 'decrypt', которая принимает на вход текст и дешифрует все
слова в нем на понятный язык (у всех слов уберите окончание '-сла'). Верните из
функции расшифрованный текст.

Напишите функцию 'encrypt', которая принимает на вход текст и шифрует все слова
в нем на язык Тофслы и Вифслы (ко всем словам добавьте окончание '-сла').
Верните из функции зашифрованный текст.

Например, текст: 'Сегоднясла мысла пойдемсла всла гостисла' будет расшифрован
как 'Сегодня мы пойдем в гости'. И наоборот.

Для получения дополнительного балла за задание (+1) нужно учесть, что в конце
предложений может встретиться один из следующих знаков препинания: !?.,;:".
Метод isalpha() может помочь определить, является ли символ буквой.

Например, текст: 'Приветсла! Каксла деласла?' будет расшифрован как 'Привет!
Как дела?'. И наоборот.

> Подсказка: посмотрите, какие аргументы можно передать функции replace.

Под блоком if __name__ == '__main__':
1. Получите текст - пользовательский ввод с клавиатуры.
2. Выполните функцию-дешифратор, передав ей данный текст.
3. Распечатайте результат вызова функции.
4. С распознанным текстом вызовите функцию-шифровальщик, передав результат
вызова функции-дешифратора.
5. Распечатайте результат вызова функции.
6. Проверьте, что изначальный текст и текст после обработки функций идентичен.
Можно проверить с помощью assert-выражения.
Например: assert result1 == result2

Добавьте докстринг (описание функции) и аннотацию типов (указание типов
параметров и возвращаемых значений) для функций.
"""


def decrypt(text: str) -> str:
    """
    Расшифровывает текст на понятный язык.

    Args:
        text: расшифровываемый текст

    Returns:
        Расшифрованный текст
    """

    words = text.split()
    for i, word in enumerate(words):
        if word[-1].isalpha() is False:
            words[i] = word[:-4] + word[-1]
        else:
            words[i] = word[:-3]

    return " ".join(words)


def encrypt(text: str) -> str:
    """
    Шифрует текст на язык Тофслы и Вифслы

    Args:
        text: зашифровываемый текст

    Returns:
        Зашифрованный текст
    """

    words = text.split()
    for i, word in enumerate(words):
        if word[-1].isalpha() is False:
            words[i] = word.replace(word[-1], f"сла{word[-1]}")
        else:
            words[i] = word + "сла"

    return " ".join(words)


if __name__ == "__main__":
    my_text = input("Введите текст: ")
    decrypted_text = decrypt(my_text)
    print(decrypted_text)
    encrypted_text = encrypt(decrypted_text)
    print(encrypted_text)
    assert my_text == encrypted_text
