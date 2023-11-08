import time as delay
from urllib.request import urlopen
import RPi.GPIO as gpio
import requests

gpio.setmode(gpio.BOARD)

# Variáveis de controle GPIO
ledVerde, ledVermelho = 11, 12
botao = 18
contador = 0  # Inicializando o contador
leitura1 = True
leitura2 = True
leitura3 = True
leitura4 = True
leitura5 = True

gpio.setup(ledVerde, gpio.OUT)
gpio.setup(ledVermelho, gpio.OUT)
gpio.setup(botao, gpio.IN, pull_up_down=gpio.PUD_DOWN)  # Configurar o botão como entrada



def conexao():
    try:
        urlopen('https://www.materdei.edu.br/pt', timeout=1)
        return True
    except:
        return False

if conexao() == True:
    print("Pressione o Botão")

while True:
    # Verifica se houve o clique no botão
    if gpio.input(botao) == True:
        contador += 1
        delay.sleep(0.5)

    # Executa a validação conforme o estabelecido
    if contador == 1 and leitura1 == True:
        gpio.output(ledVermelho, True)
        delay.sleep(2)
        gpio.output(ledVermelho, False)

        consulta_l_col = requests.get('https://api.thingspeak.com/channels/2309190/fields/1/last?key=K5TJHMHAD8WT2UB1')
        # delay.sleep(15)
       consulta_e_col = requests.get('https://api.thingspeak.com/channels/2309190/fields/2/last?key=K5TJHMHAD8WT2UB1')
        # delay.sleep(15)
        consulta_u_col = requests.get('https://api.thingspeak.com/channels/2309190/fields/3/last?key=K5TJHMHAD8WT2UB1')
        # delay.sleep(15)
        consulta_t_col = requests.get('https://api.thingspeak.com/channels/2309190/fields/4/last?key=K5TJHMHAD8WT2UB1')

        
    
        print("Consulta Realizada")
        valor_l_col = float(consulta_l_col.text)
        valor_e_col = float(consulta_e_col.text)
        valor_u_col = float(consulta_u_col.text)
        valor_t_col = float(consulta_t_col.text)
        if consulta_l_col.status_code == 200 and float(consulta_l_col.text) != -1.0:
            valido1 = True
            print(f"Valor Lido: {valor_l_col}")
        else:
            valido1 = False
            print("Falha ao consultar o campo 1")

        if consulta_e_col.status_code == 200 and float(consulta_e_col.text) != -1.0:
            valido2 = True
            print(f"Valor Lido: {valor_e_col}")
        else:
            valido2 = False
            print("Falha ao consultar o campo 2")

        if consulta_u_col.status_code == 200 and float(consulta_u_col.text) != -1.0:
            valido3 = True
            print(f"Valor Lido: {valor_u_col}")
        else:
            valido3 = False
            print("Falha ao consultar o campo 3")

        
        if consulta_t_col.status_code == 200 and float(consulta_t_col.text) != -1.0:
            valido4 = True
            print(f"Valor Lido: {valor_t_col}")
        else:
            valido4 = False
            print("Falha ao consultar o campo 4")

        if valido1 == True and valido2 == True and valido3 == True and valido4 == True:
            gpio.output(ledVerde, True)
            delay.sleep(1)
            gpio.output(ledVerde, False)
            delay.sleep(1)
            gpio.output(ledVerde, True)
            delay.sleep(1)
            gpio.output(ledVerde, False)
            delay.sleep(1)
            gpio.output(ledVerde, True)
            delay.sleep(1)
            gpio.output(ledVerde, False)
            delay.sleep(1)
        else:
            gpio.output(ledVermelho, True)
            delay.sleep(1)
            gpio.output(ledVermelho, False)
            delay.sleep(1)
            gpio.output(ledVermelho, True)
            delay.sleep(1)
            gpio.output(ledVermelho, False)
            delay.sleep(1)   
            gpio.output(ledVermelho, True)
            delay.sleep(1)
            gpio.output(ledVermelho, False)
            delay.sleep(1)    
        
        print('Clique novamente')
        leitura5 = True
        leitura1 = False
        
    if contador == 2 and leitura2 == True:
        if float(consulta_e_col.text) <= 80:
            gpio.output(ledVermelho, True)
            delay.sleep(3)
            print('Lixeira cheia')
            gpio.output(ledVermelho, False)
            
        else:
            gpio.output(ledVerde, True)
            delay.sleep(3)
            print('Lixeira vazia')
            gpio.output(ledVerde, False)
            
        print('Pode clicar de novo')
        leitura2 = False    
        
    if contador == 3 and leitura3 == True:   
        print('Entrouuuu')     
        consulta_l = requests.get('https://api.thingspeak.com/channels/2309190/fields/1/last?key=K5TJHMHAD8WT2UB1')
        # delay.sleep(15)
        consulta_e = requests.get('https://api.thingspeak.com/channels/2309190/fields/2/last?key=K5TJHMHAD8WT2UB1')
        # delay.sleep(15)
        consulta_u = requests.get('https://api.thingspeak.com/channels/2309190/fields/3/last?key=K5TJHMHAD8WT2UB1')
        # delay.sleep(15)
        consulta_t = requests.get('https://api.thingspeak.com/channels/2309190/fields/4/last?key=K5TJHMHAD8WT2UB1')

        valor_u = float(consulta_u.text)
        valor_t = float(consulta_t.text)
        valor_l = float(consulta_l.text)
        valor_e = float(consulta_e.text)
        
        conta_u = valor_u_col - valor_u
        conta_t = valor_t_col - valor_t
        
        print('Nossa valor ' + str(valor_u) + ' Valor do coleguinha ' + str(valor_u_col) + ' A diferença: ' + str(conta_u))
        print('Nossa valor ' + str(valor_t) + ' Valor do coleguinha ' + str(valor_t_col) + ' A diferença: ' + str(conta_t))
        
        print('Clique pela 4 vez')
        leitura3 = False
        
    if contador == 4 and leitura4 == True: 
        consulta_e_col3 = requests.get('https://api.thingspeak.com/channels/2309190/fields/2/last?key=K5TJHMHAD8WT2UB1')
        # delay.sleep(15)
        
        valor_e_col3 = float(consulta_e.text)

        
        print('Nossa valor ' + str(valor_e) + 
              ' Valor do coleguinha 2 ' + str(valor_e_col) + 
              ' Colega 3 ' + str(valor_e_col3))
        
        if valor_e < valor_e_col and valor_e < valor_e_col3:
            gpio.output(ledVerde, True)
            delay.sleep(3)
            print('Nossa Lixeira está mais vazia')
            gpio.output(ledVerde, False)
        
        elif valor_e > valor_e_col and valor_e_col < valor_e_col3:
            gpio.output(ledVerde, True)
            delay.sleep(1)
            gpio.output(ledVerde, False)
            delay.sleep(1)
            gpio.output(ledVerde, True)
            delay.sleep(1)
            gpio.output(ledVerde, False)
            delay.sleep(1)
            gpio.output(ledVerde, True)
            delay.sleep(1)
            gpio.output(ledVerde, False)
            delay.sleep(1)
            gpio.output(ledVerde, True)
            delay.sleep(1)
            gpio.output(ledVerde, False)
            delay.sleep(1)
            gpio.output(ledVerde, True)
            delay.sleep(1)
            gpio.output(ledVerde, False)
        
        else:
            gpio.output(ledVermelho, True)
            delay.sleep(3)
            gpio.output(ledVermelho, False)
            
        print('Clique pela ultima vez')
        print("Deu certo")
        leitura4 = False
        
    if contador == 5 and leitura5 == True:
        print('entrou')
        contador = 0
        leitura1 = True
        leitura2 = True
        leitura3 = True
        leitura4 = True
        leitura5 = False
        
        
