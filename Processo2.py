import socket

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Bem vindo, aqui temos o código destinado ao Processo 2")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    
    
    servidor.bind((socket.gethostname(), 6969))

    print(servidor)
    
    servidor.listen()
    
    
    while True:
        
        adicionado, conectado = servidor.accept()

        with conectado:
            
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print(f"Conectado: {adicionado}")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            
            while True:
                
                data_recived = conectado.recv(1024)
                
                if not data_recived:
                    break 
                
                decoded_data = data_recived.decode()
                
                data_list = decoded_data.split("|")
               
                abertura = int(data_list[0])
                
                p = int(data_list[1])
                
                if(abertura < 2000000):
                    conectado.sendall(b"Inicial fora de RANGE")
                    break
               
                if(p < 5000 or p > 20000):
                    conectado.sendall(b"X esta fora de RANGE.")
                    break
                
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as process_client:
                    process_client.connect(("locallhost", 8888))
                    print(process_client)
                   
                    message_to_send = str(abertura) + "/*/" + str(p)
                    
                    process_client.sendall(message_to_send.encode())
                    
                    data = process_client.recv(1024)
                    print(f"Resposta: {data.decode()}")
                
                
                
                
                conectado.sendall(data)
                print("Desconectado.")
                print()