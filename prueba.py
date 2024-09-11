from abc import ABC


class Players(ABC):
    pass

class HumanPlayer(Players):
    pass

class AutomaticPlayer(Players):
    pass



def ganador(state, player, board, states: list = []):
    # Generalizar estados de finalización
    for i in range(0, len(board)):
        states.append([])
        for j in range(0, len(board)):
            if j == i:
                states[i].append(1)
            else:
                states[i].append(0)

    for i in range(len(state)):
        if state in states:
            if type(player) is HumanPlayer:
                return 1  # Gana la maquina
            elif type(player) is AutomaticPlayer:
                return 0  # Gana el jugador
    # No hay ganadores


def Minimax(state: list, player: Players, board, max=-999, aux_state = []):
    if ganador(state, player, board):
        return


    else:
        for i in range(0, len(state)):
            aux_state.append(state[i])
        for i in range(0, len(state)):
            state = aux_state.copy()
            for j in range(1, state[i]+1):
                state[i] -= 1
                print(state)


"""estado = [2, 5, 4]
h1 = HumanPlayer()
Minimax(estado, h1, [2, 5, 4])"""


l = [2,3,4]
results = []

for i in range(0, len(l)):
    results.append()
        