import random

state = {
    "1": " ",
    "2": " ",
    "3": " ",
    "4": " ",
    "5": " ",
    "6": " ",
    "7": " ",
    "8": " ",
    "9": " ",
    "botFigure": "",
    "playerFigure": ""
}


def whichFigure():
    while True:
        figure = input("Выберите X или 0: ")

        if "x" == figure.lower():
            state["botFigure"] = "0"
            state["playerFigure"] = "X"
            break
        elif figure == "0":
            state["botFigure"] = "X"
            state["playerFigure"] = "0"
            break
        else:
            print("Выбрать можно только X или 0")


whichFigure()


def board():
    boardText = " ----- ----- ----- \n"
    for i in range(1, 10):
        boardText += f"|  {state[str(i)]}  "

        if i == 3 or i == 6:
            boardText += "|\n ----- ----- ----- \n"
        if i == 9:
            boardText += "|\n ----- ----- -----"
    return boardText


winNumbers = ({1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {3, 5, 7}, {1, 5, 9})


def bot():
    playerMove = set()
    botMove = set()
    mass = []

    for i in range(1, 10):
        if state[str(i)] == state["playerFigure"]:
            playerMove.add(i)

    for a in range(1, 10):
        if state[str(a)] == state["botFigure"]:
            botMove.add(a)

    for b in winNumbers:
        sets = b - botMove
        if len(sets) == 1:
            if state[str(sets)[1]] == " ":
                state[str(sets)[1]] = state["botFigure"]
                return

    for j in winNumbers:
        sets = j - playerMove
        if len(sets) == 1:
            if state[str(sets)[1]] != state["botFigure"]:
                state[str(sets)[1]] = state["botFigure"]
                return
        elif len(sets) == 2:
            for k in sets:
                mass.append(k)

    if len(mass) > 0:
        randomNum = str(random.uniform(0, len(mass)))[0]
        if state["5"] == " ":
            state["5"] = state["botFigure"]
        else:
            state[str(mass[int(randomNum)])] = state["botFigure"]


def continueOrStop():
    question = input("Продолжить (N или n) - нет или же любая буква чтобы продолжить: ")
    if question.lower() == "n":
        return "break"
    else:
        whichFigure()
        return "continue"


def winOrFail():
    playerMove = set()
    botMove = set()

    for n in range(1, 10):
        if state[str(n)] == state["playerFigure"]:
            playerMove.add(n)
        elif state[str(n)] == state["botFigure"]:
            botMove.add(n)

    for a in winNumbers:
        setsForPlayer = a - playerMove
        setsForBot = a - botMove
        if len(setsForPlayer) == 0:
            print("Вы выиграли!")
            return continueOrStop()
        elif len(setsForBot) == 0:
            print("Вы проиграли!")
            return continueOrStop()

    if state["1"] != " " and state["2"] != " " and state["3"] != " " and state["4"] != " " and state["5"] != " " and \
            state["6"] != " " and state["7"] != " " and state["8"] != " " and state["9"] != " ":
        print("Ничья!")
        return continueOrStop()


while True:
    try:
        number = int(input("Выберите номер от 1 до 9: "))
        if abs(number) < 1 or abs(number) > 9:
            raise TypeError
        else:
            if state[str(abs(number))] == " ":
                state[str(abs(number))] = state["playerFigure"]
                bot()
                print(board())

                with open('boardText.txt', 'a') as boardW:
                    boardW.write(board() + "\n\n")
                    boardW.close()

                text = winOrFail()
                if text == "break":
                    print("Пока!")
                    with open('boardText.txt', 'w') as delete:
                        pass
                    break
                elif text == "continue":
                    for i in range(1, 10):
                        state[str(i)] = " "
            else:
                print("Ход занят!")
    except ValueError:
        print("Введите цифру а не букву!")
    except TypeError:
        print("Введите цифру не больше 9 и не меньше 1!")
