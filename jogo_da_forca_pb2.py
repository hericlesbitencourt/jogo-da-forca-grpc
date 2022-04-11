# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jogo_da_forca.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13jogo_da_forca.proto\"\x16\n\x06Player\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x92\x01\n\x0bStateOfGame\x12\x18\n\x07players\x18\x02 \x03(\x0b\x32\x07.Player\x12\x14\n\x0cwrongLetters\x18\x03 \x01(\t\x12\x16\n\x0e\x63orrectLetters\x18\x04 \x01(\t\x12\x12\n\nplayerTurn\x18\x05 \x01(\t\x12\x12\n\nsecretWord\x18\x06 \x01(\t\x12\x13\n\x0bgameStarted\x18\x07 \x01(\x08\"\x1d\n\x0b\x42oolRequest\x12\x0e\n\x06result\x18\x08 \x01(\x08\"\x1e\n\x0c\x42oolResponse\x12\x0e\n\x06result\x18\t \x01(\x08\"\x1d\n\x0bLetterGuess\x12\x0e\n\x06letter\x18\n \x01(\t\" \n\x0eStringResponse\x12\x0e\n\x06result\x18\x0b \x01(\t\"\x07\n\x05\x45mpty2\xd1\x02\n\x12JogoDaForcaService\x12\x1f\n\tAddPlayer\x12\x07.Player\x1a\x07.Player\"\x00\x12-\n\x12RequestStateOfGame\x12\x07.Player\x1a\x0c.StateOfGame\"\x00\x12\x30\n\x18\x41\x64\x64GuessToCorrectLetters\x12\x0c.LetterGuess\x1a\x06.Empty\x12.\n\x16\x41\x64\x64GuessToWrongLetters\x12\x0c.LetterGuess\x1a\x06.Empty\x12\"\n\tPlayerWon\x12\x06.Empty\x1a\r.BoolResponse\x12#\n\x11SetGameStartFalse\x12\x06.Empty\x1a\x06.Empty\x12\"\n\x10SetGameStartTrue\x12\x06.Empty\x1a\x06.Empty\x12\x1c\n\nChangeTurn\x12\x06.Empty\x1a\x06.Emptyb\x06proto3')



_PLAYER = DESCRIPTOR.message_types_by_name['Player']
_STATEOFGAME = DESCRIPTOR.message_types_by_name['StateOfGame']
_BOOLREQUEST = DESCRIPTOR.message_types_by_name['BoolRequest']
_BOOLRESPONSE = DESCRIPTOR.message_types_by_name['BoolResponse']
_LETTERGUESS = DESCRIPTOR.message_types_by_name['LetterGuess']
_STRINGRESPONSE = DESCRIPTOR.message_types_by_name['StringResponse']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
Player = _reflection.GeneratedProtocolMessageType('Player', (_message.Message,), {
  'DESCRIPTOR' : _PLAYER,
  '__module__' : 'jogo_da_forca_pb2'
  # @@protoc_insertion_point(class_scope:Player)
  })
_sym_db.RegisterMessage(Player)

StateOfGame = _reflection.GeneratedProtocolMessageType('StateOfGame', (_message.Message,), {
  'DESCRIPTOR' : _STATEOFGAME,
  '__module__' : 'jogo_da_forca_pb2'
  # @@protoc_insertion_point(class_scope:StateOfGame)
  })
_sym_db.RegisterMessage(StateOfGame)

BoolRequest = _reflection.GeneratedProtocolMessageType('BoolRequest', (_message.Message,), {
  'DESCRIPTOR' : _BOOLREQUEST,
  '__module__' : 'jogo_da_forca_pb2'
  # @@protoc_insertion_point(class_scope:BoolRequest)
  })
_sym_db.RegisterMessage(BoolRequest)

BoolResponse = _reflection.GeneratedProtocolMessageType('BoolResponse', (_message.Message,), {
  'DESCRIPTOR' : _BOOLRESPONSE,
  '__module__' : 'jogo_da_forca_pb2'
  # @@protoc_insertion_point(class_scope:BoolResponse)
  })
_sym_db.RegisterMessage(BoolResponse)

LetterGuess = _reflection.GeneratedProtocolMessageType('LetterGuess', (_message.Message,), {
  'DESCRIPTOR' : _LETTERGUESS,
  '__module__' : 'jogo_da_forca_pb2'
  # @@protoc_insertion_point(class_scope:LetterGuess)
  })
_sym_db.RegisterMessage(LetterGuess)

StringResponse = _reflection.GeneratedProtocolMessageType('StringResponse', (_message.Message,), {
  'DESCRIPTOR' : _STRINGRESPONSE,
  '__module__' : 'jogo_da_forca_pb2'
  # @@protoc_insertion_point(class_scope:StringResponse)
  })
_sym_db.RegisterMessage(StringResponse)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'jogo_da_forca_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

_JOGODAFORCASERVICE = DESCRIPTOR.services_by_name['JogoDaForcaService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLAYER._serialized_start=23
  _PLAYER._serialized_end=45
  _STATEOFGAME._serialized_start=48
  _STATEOFGAME._serialized_end=194
  _BOOLREQUEST._serialized_start=196
  _BOOLREQUEST._serialized_end=225
  _BOOLRESPONSE._serialized_start=227
  _BOOLRESPONSE._serialized_end=257
  _LETTERGUESS._serialized_start=259
  _LETTERGUESS._serialized_end=288
  _STRINGRESPONSE._serialized_start=290
  _STRINGRESPONSE._serialized_end=322
  _EMPTY._serialized_start=324
  _EMPTY._serialized_end=331
  _JOGODAFORCASERVICE._serialized_start=334
  _JOGODAFORCASERVICE._serialized_end=671
# @@protoc_insertion_point(module_scope)