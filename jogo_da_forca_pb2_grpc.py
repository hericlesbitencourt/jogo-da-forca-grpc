# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import jogo_da_forca_pb2 as jogo__da__forca__pb2


class JogoDaForcaServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddPlayer = channel.unary_unary(
                '/JogoDaForcaService/AddPlayer',
                request_serializer=jogo__da__forca__pb2.Player.SerializeToString,
                response_deserializer=jogo__da__forca__pb2.Player.FromString,
                )
        self.RequestStateOfGame = channel.unary_unary(
                '/JogoDaForcaService/RequestStateOfGame',
                request_serializer=jogo__da__forca__pb2.Player.SerializeToString,
                response_deserializer=jogo__da__forca__pb2.StateOfGame.FromString,
                )
        self.AddGuessToCorrectLetters = channel.unary_unary(
                '/JogoDaForcaService/AddGuessToCorrectLetters',
                request_serializer=jogo__da__forca__pb2.LetterGuess.SerializeToString,
                response_deserializer=jogo__da__forca__pb2.Empty.FromString,
                )
        self.AddGuessToWrongLetters = channel.unary_unary(
                '/JogoDaForcaService/AddGuessToWrongLetters',
                request_serializer=jogo__da__forca__pb2.LetterGuess.SerializeToString,
                response_deserializer=jogo__da__forca__pb2.Empty.FromString,
                )
        self.PlayerWon = channel.unary_unary(
                '/JogoDaForcaService/PlayerWon',
                request_serializer=jogo__da__forca__pb2.Empty.SerializeToString,
                response_deserializer=jogo__da__forca__pb2.BoolResponse.FromString,
                )
        self.SetGameStartFalse = channel.unary_unary(
                '/JogoDaForcaService/SetGameStartFalse',
                request_serializer=jogo__da__forca__pb2.Empty.SerializeToString,
                response_deserializer=jogo__da__forca__pb2.Empty.FromString,
                )
        self.SetGameStartTrue = channel.unary_unary(
                '/JogoDaForcaService/SetGameStartTrue',
                request_serializer=jogo__da__forca__pb2.Empty.SerializeToString,
                response_deserializer=jogo__da__forca__pb2.Empty.FromString,
                )
        self.ChangeTurn = channel.unary_unary(
                '/JogoDaForcaService/ChangeTurn',
                request_serializer=jogo__da__forca__pb2.Empty.SerializeToString,
                response_deserializer=jogo__da__forca__pb2.Empty.FromString,
                )


class JogoDaForcaServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddPlayer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RequestStateOfGame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddGuessToCorrectLetters(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddGuessToWrongLetters(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PlayerWon(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetGameStartFalse(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetGameStartTrue(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangeTurn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_JogoDaForcaServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddPlayer': grpc.unary_unary_rpc_method_handler(
                    servicer.AddPlayer,
                    request_deserializer=jogo__da__forca__pb2.Player.FromString,
                    response_serializer=jogo__da__forca__pb2.Player.SerializeToString,
            ),
            'RequestStateOfGame': grpc.unary_unary_rpc_method_handler(
                    servicer.RequestStateOfGame,
                    request_deserializer=jogo__da__forca__pb2.Player.FromString,
                    response_serializer=jogo__da__forca__pb2.StateOfGame.SerializeToString,
            ),
            'AddGuessToCorrectLetters': grpc.unary_unary_rpc_method_handler(
                    servicer.AddGuessToCorrectLetters,
                    request_deserializer=jogo__da__forca__pb2.LetterGuess.FromString,
                    response_serializer=jogo__da__forca__pb2.Empty.SerializeToString,
            ),
            'AddGuessToWrongLetters': grpc.unary_unary_rpc_method_handler(
                    servicer.AddGuessToWrongLetters,
                    request_deserializer=jogo__da__forca__pb2.LetterGuess.FromString,
                    response_serializer=jogo__da__forca__pb2.Empty.SerializeToString,
            ),
            'PlayerWon': grpc.unary_unary_rpc_method_handler(
                    servicer.PlayerWon,
                    request_deserializer=jogo__da__forca__pb2.Empty.FromString,
                    response_serializer=jogo__da__forca__pb2.BoolResponse.SerializeToString,
            ),
            'SetGameStartFalse': grpc.unary_unary_rpc_method_handler(
                    servicer.SetGameStartFalse,
                    request_deserializer=jogo__da__forca__pb2.Empty.FromString,
                    response_serializer=jogo__da__forca__pb2.Empty.SerializeToString,
            ),
            'SetGameStartTrue': grpc.unary_unary_rpc_method_handler(
                    servicer.SetGameStartTrue,
                    request_deserializer=jogo__da__forca__pb2.Empty.FromString,
                    response_serializer=jogo__da__forca__pb2.Empty.SerializeToString,
            ),
            'ChangeTurn': grpc.unary_unary_rpc_method_handler(
                    servicer.ChangeTurn,
                    request_deserializer=jogo__da__forca__pb2.Empty.FromString,
                    response_serializer=jogo__da__forca__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'JogoDaForcaService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class JogoDaForcaService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddPlayer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/JogoDaForcaService/AddPlayer',
            jogo__da__forca__pb2.Player.SerializeToString,
            jogo__da__forca__pb2.Player.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RequestStateOfGame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/JogoDaForcaService/RequestStateOfGame',
            jogo__da__forca__pb2.Player.SerializeToString,
            jogo__da__forca__pb2.StateOfGame.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddGuessToCorrectLetters(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/JogoDaForcaService/AddGuessToCorrectLetters',
            jogo__da__forca__pb2.LetterGuess.SerializeToString,
            jogo__da__forca__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddGuessToWrongLetters(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/JogoDaForcaService/AddGuessToWrongLetters',
            jogo__da__forca__pb2.LetterGuess.SerializeToString,
            jogo__da__forca__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PlayerWon(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/JogoDaForcaService/PlayerWon',
            jogo__da__forca__pb2.Empty.SerializeToString,
            jogo__da__forca__pb2.BoolResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetGameStartFalse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/JogoDaForcaService/SetGameStartFalse',
            jogo__da__forca__pb2.Empty.SerializeToString,
            jogo__da__forca__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetGameStartTrue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/JogoDaForcaService/SetGameStartTrue',
            jogo__da__forca__pb2.Empty.SerializeToString,
            jogo__da__forca__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChangeTurn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/JogoDaForcaService/ChangeTurn',
            jogo__da__forca__pb2.Empty.SerializeToString,
            jogo__da__forca__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
