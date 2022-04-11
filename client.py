from urllib import request
import grpc
import time
import threading

import jogo_da_forca_pb2
import jogo_da_forca_pb2_grpc
from utils.forca import DRAW_FORCA
from utils.library import printGame, getLetterGuess

playerName = input('Digite o seu nome: ')

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = jogo_da_forca_pb2_grpc.JogoDaForcaServiceStub(channel)
    player = jogo_da_forca_pb2.Player(name=playerName)
    try:
        player = stub.AddPlayer(player)
    except grpc.RpcError as e:
        print(e)
        print("Ocorreu um erro ao adicionar o jogador.")
        quit()

    state = stub.RequestStateOfGame(player)
    
    print(f"Seja bem vindo ao Jogo da Forca {player.name}. Siga as instruções abaixo.")
    print(
    """
    O objetivo deste jogo é descobrir uma palavra adivinhando as letras que ela possui.
    A cada rodada, os jogadores irão escolher uma letra que suspeitem fazer parte da palavra.
    Caso a palavra contenha esta letra, será mostrado em que posição(ões) ela está.
    Entretanto, caso esta letra não exista na palavra, será desenhada uma parte do corpo do boneco do jogador.
    O vencedor é o que conseguir digitar a última letra da palavra.
    """
    )
    i = 0;
    while len(state.players) != 2:
        if i == 0:
            print('Aguarde o segundo jogador entrar na partida...')
            i = 1
        state = stub.RequestStateOfGame(player)
    try:
        while state.gameStarted:
            if state.players[0].name == player.name:
                print(f"É a sua vez {player.name}!\n")
                printGame(state.wrongLetters, state.correctLetters, state.secretWord)
                
                letter = getLetterGuess(state.wrongLetters, state.correctLetters)

                if letter in state.secretWord:
                    stub.AddGuessToCorrectLetters(jogo_da_forca_pb2.LetterGuess(letter=letter))
                    state = stub.RequestStateOfGame(player)
                    playerWon = stub.PlayerWon(jogo_da_forca_pb2.Empty())
                    
                    if playerWon.result == True:
                        print("Você advinhou! A palavra é " + state.secretWord + '!')
                        stub.SetGameStartFalse(jogo_da_forca_pb2.Empty())
                        state = stub.RequestStateOfGame(player)
                    else:
                        stub.ChangeTurn(jogo_da_forca_pb2.Empty())
                        state = stub.RequestStateOfGame(player)
                else:
                    stub.AddGuessToWrongLetters(jogo_da_forca_pb2.LetterGuess(letter=letter))
                    state = stub.RequestStateOfGame(player)
                    stub.ChangeTurn(jogo_da_forca_pb2.Empty())
                    state = stub.RequestStateOfGame(player)
                    if len(state.wrongLetters) == len(DRAW_FORCA) - 1:
                        printGame(state.wrongLetters, state.correctLetters, state.secretWord)
                        print("Ninguém acertou a palavra!")
                        print('A palavra correta era '+state.secretWord+'.')
                        stub.SetGameStartFalse(jogo_da_forca_pb2.Empty())
                        state = stub.RequestStateOfGame(player)
            else:
                if state.gameStarted:
                    print(f"Aguarde, o jogador {state.players[0].name} está jogando.")
                    time.sleep(5)
                    state = stub.RequestStateOfGame(player)
                        
    except KeyboardInterrupt:
        print("Você saiu do jogo.")
    finally:
        if len(state.wrongLetters) == len(DRAW_FORCA) - 1:
            printGame(state.wrongLetters, state.correctLetters, state.secretWord)
            print("Ninguém acertou a palavra!")
            print('A palavra correta era '+state.secretWord+'.')
        input("Aperter ENTER para sair.")


if __name__ == '__main__':
    run()
