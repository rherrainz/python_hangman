import random

words_list = [
    "pollo",
    "gato",
    "perro",
    "caballo",
    "elefante",
    "jirafa",
    "cocodrilo",
    "tigre",
    "leon",
    "oso",
    "ballena",
    "delfin",
    "tiburon",
    "pulpo",
    "medusa",
    "pato",
    "aguila",
    "halcon",
    "loro",
    "pajaro",
    "gallina",
    "pavo",
    "cisne",
    "pato",
    "ganso",
    "paloma",
    "cuervo",
    "buitre",
    "zorro",
    "lobo",
    "oso",
    "mapache",
    "ardilla",
    "conejo",
    "ciervo",
    "oso",
]

hangman = [
    r"""  
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    r"""  
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    r"""  
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """  
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    """  
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """  
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]


def randomize_word(words):
    word = words[random.randint(0, len(words) - 1)]
    word = word.upper()
    return word


word = randomize_word(words_list)


def mock_word(word):
    mock = ""
    for i in range(len(word)):
        mock += "_"
    return mock


mock = mock_word(word)

tries = 5

print("Adivina el animal: ")

while tries > 0:
    print("Ingrese una letra: ")
    letter = input().upper()
    if letter in word:
        print("La letra esta en la palabra")
        for i in range(len(word)):
            if word[i] == letter:
                mock = mock[:i] + letter + mock[i + 1:]
        print(hangman[tries])
        print(mock)
        print("Fallos restantes: ", tries)
        if mock == word:
            print("Ganaste!")
            break

    else:
        print("La letra no esta en la palabra")
        print(hangman[tries])
        print(mock)
        tries -= 1
        print("Fallos restantes: ", tries)

if tries == 0:
    print("Perdiste!")
    print(hangman[tries])
    print("La palabra era: ", word)
