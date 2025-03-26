"""
# Задача 1: Переводчик слов +1

Дан словарь DICTIONARY, в котором ключи — это английские слова, а значения —
их перевод

Напишите функцию 'translate_text', которая принимает на вход предложение без
знаков препинания.
Функция должна переводить предложение на русский язык, используя словарь
DICTIONARY.  Если какого-то слова в словаре не окажется, то вместо перевода
этого слова укажите три точки '...'.

Функция должна переводить слова независимо от их регистра.
Предложение всегда начинается с большой буквы. Переведенное предложение также
должно начинаться с большой буквы.
Используйте для этого строковый метод capitalize().

Например: 'I sit on bed' будет переводиться как 'Я сидеть на кровать'.

Или 'I hear his cat' будет переводиться как 'Я слышать его ...'.
В данном случае слово 'cat' не нашлось в словаре, поэтому оно заменено на
многоточие.

Под блоком if __name__ == '__main__': получите текст от пользователя,
выполните функцию, передав ей нужные аргументы, и распечатайте результат вызова
функции.

Добавьте докстринг (описание функции) и аннотацию типов (указание типов
параметров и возвращаемых значений) для функции.

> Гарантируется что текст содержит только английские буквы в различном регистре
и пробелы.
"""

DICTIONARY = {
    "adult": "взрослый",
    "age": "возраст",
    "baby": "малыш",
    "birth": "рождение",
    "boy": "мальчик",
    "child": "ребенок",
    "childhood": "детство",
    "girl": "девочка",
    "human": "человек",
    "kid": "ребенок",
    "life": "жизнь",
    "man": "мужчина",
    "name": "имя",
    "people": "люди",
    "person": "человек",
    "personality": "личность",
    "surname": "фамилия",
    "teenager": "подросток",
    "woman": "женщина",
    "youth": "молодежь",
    "he": "он",
    "her": "ее",
    "him": "его",
    "his": "его",
    "i": "я",
    "is": "это",
    "it": "оно",
    "my": "мой",
    "our": "наш",
    "she": "она",
    "their": "их",
    "them": "их",
    "they": "они",
    "we": "мы",
    "on": "на",
    "in": "в",
    "arm": "рука",
    "back": "спина",
    "belly": "живот",
    "blood": "кровь",
    "body": "тело",
    "bone": "кость",
    "brain": "мозг",
    "cheek": "щека",
    "chin": "подбородок",
    "ear": "ухо",
    "take": "захватить",
    "elbow": "локоть",
    "eye": "глаз",
    "eyebrow": "бровь",
    "eyelash": "ресница",
    "face": "лицо",
    "finger": "палец",
    "fist": "кулак",
    "foot": "ступня",
    "revenge": "месть",
    "forehead": "лоб",
    "hair": "волосы",
    "hand": "кисть руки",
    "heart": "сердце",
    "heel": "пятка",
    "hip": "бедро",
    "jaw": "челюсть",
    "kidney": "почка",
    "knee": "колено",
    "leg": "нога",
    "lips": "губы",
    "liver": "печень",
    "very": "очень",
    "lung": "легкое",
    "mouth": "рот",
    "muscle": "мышца",
    "nail": "ноготь",
    "neck": "шея",
    "nerve": "нерв",
    "nose": "нос",
    "palm": "ладонь",
    "rib": "ребро",
    "skeleton": "скелет",
    "skin": "кожа",
    "skull": "череп",
    "stomach": "желудок",
    "throat": "горло",
    "thumb": "большой палец",
    "toe": "палец на ноге",
    "tongue": "язык",
    "tooth": "зуб",
    "wrist": "запястье",
    "be": "быть",
    "breathe": "дышать",
    "hear": "слышать",
    "hold": "держать",
    "lie": "лежать",
    "look": "смотреть",
    "see": "видеть",
    "sit": "сидеть",
    "speak": "говорить",
    "love": "любить",
    "touch": "трогать",
    "walk": "ходить",
    "attractive": "привлекательный",
    "bed": "кровать",
}
