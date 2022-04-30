import socket
import sympy

def Primo1(x):
    if(sympy.isprime(x)):
        return x
    x+=1
    return Primo1(x)

 
    
def Primo2(x):
    if(sympy.isprime(x)):
        return x
    x-=1
    return Primo2(x)
    


def servidor():
    
    
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        
        s.bind((socket.gethostname(), 42069))
        print(s)
        s.listen()
        
        
        
        while True:
            conexao, addr = s.accept()
            with conexao:
                print(f"Conectado: {addr}")
                while True:
                    sent_data = conexao.recv(1024)
                    
                    
                    
                    decoded_data = sent_data.decode()
                    
                    data_list = decoded_data.split("|")
                    print(f"Numeros a serem recebidos: {data_list}")

                    if not sent_data:  # Verifica se foram recebidas informações
                        break
                    
                    inicial_code = int(data_list[0])
                    n = int(data_list[1])
                    
                    for i in range(n):
                        if(i == 0):
                            
                            n_Primo_1 = Primo1(inicial_code + 1)
                            n_Primo2 = Primo2(inicial_code + 1)
                        n_Primo_1 = Primo1(n_Primo_1)
                        n_Primo2 = Primo2(n_Primo2)
                    
                    
                    
                    print(f"{n} {n_Primo_1}")
                    print(f"{n} {n_Primo2}")


                    
                    answer = str(n_Primo_1) + str(n_Primo2)  # Junta os resultados
                    
                    conexao.sendall(answer.encode()) # Retorna a chave
                    print("Desconectado.")
                    print()
    

servidor()