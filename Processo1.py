import time
import socket
import random

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Bem vindo, aqui vamos medir o tempo de execução (Processo 1)")
quant_Repet = int(input("quantos LOOPS deseja?  "))
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")


tempo_Inicial = time.time()

tempo = False

for i in range(quant_Repet):
    
    inicio = random.randint(20000000,9999999999)

    aleatorio = random.randint(5000,15001)
    
    menssagem = str(inicio) + str(aleatorio)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
       
        s.connect(("192.168.10.112", 6969)) #seu ipv4
        
        s.sendall(menssagem.encode())

        prime_key = s.recv(1024)
        
        print(f"CAHVE {i}: {prime_key.decode()}")

        tempo_Final = time.time()

        tempo_Gasto = tempo_Final-tempo_Inicial

        if(not tempo and tempo_Gasto >= 5):
            
            
            print("5 segundos de execução.")
            
            
            tempo = True


print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(f"Tempo total da execução = {tempo_Gasto}")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")