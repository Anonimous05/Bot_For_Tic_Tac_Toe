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
                if state["1"] == state["botFigure"] and state["2"] == state["botFigure"] and state["3"] == state[
                    "botFigure"] \
                        or state["1"] == state["botFigure"] and state["4"] == state["botFigure"] and state["7"] == \
                        state["botFigure"]:
                    print("Вы проиграли!")
                    break
                elif state["4"] == state["botFigure"] and state["5"] == state["botFigure"] and state["6"] == state[
                    "botFigure"] or state["2"] == state["botFigure"] and state["5"] == state["botFigure"] and state[
                    "8"] == state["botFigure"]:
                    print("Вы проиграли!")
                    break
                elif state["7"] == state["botFigure"] and state["8"] == state["botFigure"] and state["9"] == state[
                    "playerFigure"] or state["3"] == state["botFigure"] and state["6"] == state["botFigure"] and state[
                    "9"] == state["botFigure"]:
                    print("Вы проиграли!")
                    break
                elif state["1"] == state["botFigure"] and state["5"] == state["botFigure"] and state["9"] == state[
                    "botFigure"] or state["3"] == state["botFigure"] and state["5"] == state["botFigure"] and state[
                    "7"] == state["botFigure"]:
                    print("Вы проиграли!")
                    break

                elif state["1"] == state["playerFigure"] and state["2"] == state["playerFigure"] and state["3"] == state[
                    "playerFigure"] \
                        or state["1"] == state["playerFigure"] and state["4"] == state["playerFigure"] and state["7"] == \
                        state["playerFigure"]:
                    print("Вы выиграли!")
                    break
                elif state["4"] == state["playerFigure"] and state["5"] == state["playerFigure"] and state["6"] == state[
                    "playerFigure"] or state["2"] == state["playerFigure"] and state["5"] == state["playerFigure"] and state[
                    "8"] == state["playerFigure"]:
                    print("Вы выиграли!")
                    break
                elif state["7"] == state["playerFigure"] and state["8"] == state["playerFigure"] and state["9"] == state[
                    "playerFigure"] or state["3"] == state["playerFigure"] and state["6"] == state["playerFigure"] and state[
                    "9"] == state["playerFigure"]:
                    print("Вы выиграли!")
                    break
                elif state["1"] == state["playerFigure"] and state["5"] == state["playerFigure"] and state["9"] == state[
                    "playerFigure"] or state["3"] == state["playerFigure"] and state["5"] == state["playerFigure"] and state[
                    "7"] == state["playerFigure"]:
                    print("Вы выиграли!")
                    break

                if state["1"] != " " and state["2"] != " " and state["3"] != " " and state["4"] != " " and state["5"] != " " and state["6"] != " " and state["7"] != " " and state["8"] != " " and state["9"] != " ":
                    print("Ничья!")
                    break
            else:
                print("Ход занят!")
    except ValueError:
        print("Введите цифру а не букву!")
    except TypeError:
        print("Введите цифру не больше 9 и не меньше 1!")