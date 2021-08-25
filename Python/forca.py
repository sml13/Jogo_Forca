import random


def StartRightWords(secretKeyword):
    return ["_" for Character in secretKeyword]


def PlayGame():

    PrintTheWelcomeMsg()

    secretKeyword = LoadKeyWord()

    GoodChars = StartRightWords(secretKeyword)

    PlayerHanged = False
    PlayerWon = False
    WrongTry = 0
    print(GoodChars)
    while(not PlayerHanged and not PlayerWon):

        PlayerTry = AskUserTry()

        if(PlayerTry in secretKeyword):
            recordRightTry(PlayerTry, GoodChars, secretKeyword)

        else:
            WrongTry += 1

        PlayerHanged = WrongTry == 6
        PlayerWon = "_" not in GoodChars
        print(GoodChars)

    if(PlayerWon):
        print("Você ganhou")
    else:
        print("Você perdeu")
    print("Fim do jogo")


def PrintTheWelcomeMsg():
    print("Este é o jogo da Forca")
    print("Para ganhar, você deverá acertar a palavra secreta.")
    print("Cada erro lhe custará uma chance, você pode errar no máximo 6 vezes")
    print("Boa sorte e bom jogo.")


def AskUserTry():
    PlayerTry = input("Qual a letra ?")
    PlayerTry = PlayerTry.strip().upper()
    return PlayerTry


def recordRightTry(PlayerTry, GoodChars, secretKeyword):
    index = 0
    for Character in secretKeyword:
        if (PlayerTry.upper() == Character.upper()):
            GoodChars[index] = Character
        index += 1


def LoadKeyWord():

    File = open("Python\words.txt", "r")
    WordsInDoc = []
    for line in File:
        line = line.strip()
        WordsInDoc.append(line)

    File.close()

    Num = random.randrange(0, len(WordsInDoc))

    secretKeyword = WordsInDoc[Num].upper()
    return secretKeyword


if(__name__ == "__main__"):
    PlayGame()
