import socket



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((socket.gethostname(), 6969))
    print(server)
    server.listen()
    while True:
        conexao, addr = server.accept()
        with conexao:
            print(f"Client connected: {addr}")
            while True:
                sent_data = conexao.recv(1024)
                
                if not sent_data:
                    break 
                decoded_data = sent_data.decode()
                
                data_list = decoded_data.split("|")
               
                inicial_code = int(data_list[0])
                n = int(data_list[1])
                
                if(inicial_code < 10000000):
                    conexao.sendall(b"The inicial code is not within range. It must be higher than 12.000.000")
                    break
               
                if(n < 5000 or n > 15000):
                    conexao.sendall(b"The n is not within range. It must be between 5000 and 15000.")
                    break
                
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as process_client:
                    process_client.connect(("192.168.0.5", 6969))
                    print(process_client)
                   
                    message_to_send = str(inicial_code) + "|" + str(n)
                    
                    process_client.sendall(message_to_send.encode())
                    
                    data = process_client.recv(1024)
                    print(f"Answer from server: {data.decode()}")
                
                conexao.sendall(data)
                print("Client disconnected.")
                print()