import socket



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:


    servidor.bind((socket.gethostname(), 8888))
    
    server.listen()


    while True:
        adicionado, conectado = server.accept()
        with conexao:
            
	print(f"Conectado: {adicionado}")
            while True:
                
		dados = conectado.recv(1024)
                
                
                decoded_data = sent_data.decode()
                
                
               if not dados:
                    break 

                inicializacao = int(lista[0])
               	q = int(data_list[1])
                
                if(inicializacao < 10000000):
                    
                    break
               
                if(q < 5000 or q > 15000):
                    
                    break
                
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as process_client:

                    process_client.connect(("192.168.0.5", 6969))
                    
                   
                    message_to_send = str(inicializacao) + str(q)
                    
                    process_client.sendall(message_to_send.encode())
                    
                    data = process_client.recv(1024)
                    print(f"{data.decode()}")
                
                


		conexao.sendall(data)


                print("Desconectado.")
                print()