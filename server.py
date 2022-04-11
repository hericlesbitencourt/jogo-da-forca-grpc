import time
from concurrent import futures

import grpc

import jogo_da_forca_pb2
import jogo_da_forca_pb2_grpc
from utils.library import getSecretWord

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class JogoDaForcaServicer(jogo_da_forca_pb2_grpc.JogoDaForcaServiceServicer):

    def __init__(self):
        self.wrongLetters = ''
        self.correctLetters = ''
        self.players = []
        self.secretWord = getSecretWord()
        self.gameStarted = True

    def AddPlayer(self, request, context):
        if len(self.players) <= 2:
            new_player = jogo_da_forca_pb2.Player(name=request.name)
            self.players.append(new_player)
            print(f"O jogador {new_player.name} entrou no jogo.")
            return new_player
        else:
            self.players.pop(1)
            self.raise_internal_error("Ocorreu um erro!", context)
            return jogo_da_forca_pb2.Player()
    
    def RequestStateOfGame(self, request, context):
        return jogo_da_forca_pb2.StateOfGame(
            **{
                "players": self.players,
                "secretWord": self.secretWord,
                "wrongLetters": self.wrongLetters,
                "correctLetters": self.correctLetters,
                "gameStarted": self.gameStarted,
            }
        )

    def SetGameStartFalse(self, request: jogo_da_forca_pb2.Empty(), context):
        self.gameStarted = False
        return jogo_da_forca_pb2.Empty()

    def SetGameStartTrue(self, request: jogo_da_forca_pb2.Empty(), context):
        self.wrongLetters = ''
        self.rightLetters = ''
        self.gameStarted = True
        self.secretWord = getSecretWord()
        return jogo_da_forca_pb2.Empty()

    def AddGuessToCorrectLetters(self, request, context):
        self.correctLetters += request.letter
        return jogo_da_forca_pb2.Empty()

    def AddGuessToWrongLetters(self, request, context):
        self.wrongLetters += request.letter
        return jogo_da_forca_pb2.Empty()

    def PlayerWon(self, request: jogo_da_forca_pb2.Empty(), context):
        won = True
        for letter in self.secretWord:
            if letter not in self.correctLetters:
                won = False
                break
        return jogo_da_forca_pb2.BoolResponse(result=won)

    def ChangeTurn(self, request: jogo_da_forca_pb2.Empty(), context):
        playersCopy = self.players.copy()
        self.players[0], self.players[1] = playersCopy[1], playersCopy[0]
        return jogo_da_forca_pb2.Empty()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    jogo_da_forca_pb2_grpc.add_JogoDaForcaServiceServicer_to_server(
        JogoDaForcaServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
