# Jogo da Forca gRPC
    
## Instructions

Install the dependencies:

    $ pip install -r requirements.txt

Generate protobuf files:

    $ python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/jogo_da_forca.proto
    
Run client and server:

    $ python server.py
    $ python client.py