# Створення словника для ASCII-символів
ascii_chars = {
    'A': [
        "  A  ",
        " A A ",
        "AAAAA",
        "A   A",
    ],
    'B': [
        "BBBB ",
        "B   B",
        "BBBB ",
        "B   B",
        "BBBB ",
    ],
    'C': [
        " CCC ",
        "C   C",
        "C    ",
        "C   C",
        " CCC ",
    ],
    'D': [
        "DDD  ",
        "D   D",
        "D   D",
        "D   D",
        "DDD  ",
    ],
    'E': [
        "EEEE ",
        "E    ",
        "EEE  ",
        "E    ",
        "EEEE ",
    ],
    'F': [
        "FFFFF",
        "F    ",
        "FFF  ",
        "F    ",
        "F    ",
    ],
    'G': [
        " GGG ",
        "G    ",
        "G  GG",
        "G   G",
        " GGG ",
    ],
    'H': [
        "H   H",
        "H   H",
        "HHHHH",
        "H   H",
        "H   H",
    ],
    'I': [
        "III  ",
        " I   ",
        " I   ",
        " I   ",
        "III  ",
    ],
    'J': [
        "  J  ",
        "  J  ",
        "  J  ",
        "J J  ",
        " JJ  ",
    ],
    'K': [
        "K   K",
        "K  K ",
        "KK   ",
        "K  K ",
        "K   K",
    ],
    'L': [
        "L    ",
        "L    ",
        "L    ",
        "L    ",
        "LLLLL",
    ],
    'M': [
        "M   M",
        "MM MM",
        "M M M",
        "M   M",
        "M   M",
    ],
    'N': [
        "N   N",
        "NN  N",
        "N N N",
        "N  NN",
        "N   N",
    ],
    'O': [
        " OOO ",
        "O   O",
        "O   O",
        "O   O",
        " OOO ",
    ],
    'P': [
        "PPP  ",
        "P   P",
        "PPP  ",
        "P    ",
        "P    ",
    ],
    'Q': [
        " QQQ ",
        "Q   Q",
        "Q   Q",
        "Q Q Q",
        " QQ Q",
    ],
    'R': [
        "RRR  ",
        "R   R",
        "RRR  ",
        "R R  ",
        "R  R ",
    ],
    'S': [
        " SSS ",
        "S    ",
        " SSS ",
        "    S",
        " SSS ",
    ],
    'T': [
        "TTTTT",
        "  T  ",
        "  T  ",
        "  T  ",
        "  T  ",
    ],
    'U': [
        "U   U",
        "U   U",
        "U   U",
        "U   U",
        " UUU ",
    ],
    'V': [
        "V   V",
        "V   V",
        "V   V",
        " V V ",
        "  V  ",
    ],
    'W': [
        "W   W",
        "W   W",
        "W W W",
        "W W W",
        "W   W",
    ],
    'X': [
        "X   X",
        "X   X",
        " X X ",
        "X   X",
        "X   X",
    ],
    'Y': [
        "Y   Y",
        "Y   Y",
        " Y Y ",
        "  Y  ",
        "  Y  ",
    ],
    'Z': [
        "ZZZZZ",
        "   Z ",
        "  Z  ",
        " Z   ",
        "ZZZZZ",
    ],
    ' ': [
        "     ",
        "     ",
        "     ",
        "     ",
        "     ",
    ],
}

# Функція для створення ASCII-арт з тексту
def create_ascii_art(text):
    lines = [""] * len(ascii_chars['A'])

    for char in text:
        char_data = ascii_chars.get(char, ascii_chars[' '])

        for i, line in enumerate(char_data):
            lines[i] += line + "  "

    return "\n".join(lines)

# Запит від користувача
text = input("Введіть текст для перетворення в ASCII-арт: ")

# Створення ASCII-арт
art = create_ascii_art(text)

# Виведення ASCII-арт на екран
print(art)
