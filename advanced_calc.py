import os
os.system('cls' if os.name == 'nt' else 'clear')
def regra3():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""\033[1;34m
 _____                      _        _               
| __  |___ ___ ___ ___    _| |___   | |_ ___ ___ ___ 
|    -| -_| . |  _| .'|  | . | -_|  |  _|  _| -_|_ -|
|__|__|___|_  |_| |__,|  |___|___|  |_| |_| |___|___|
          |___|                                      

""")
        a = input('[*] - Insira o prineiro número da situação problema : ')
        b = input('[*] - Insira o segundo número da situação problema : ')
        c = input('[*] - Insira o terceiro número da situação problema : ')
        proporcao = input('[*] - É inversamente ou diretamente proporcional [D/I] : ')
        if proporcao == 'D' or 'd':
           d = (int(a) * int(b))
           resultado = (int(a) / int(c))
           print('[!] - X = ' + str(resultado))
        elif proporcao == 'I' or 'i':
           d = a * c
           resultado = d / a
           print('[!] - X = ' + str(resultado))

def equation():
     os.system('cls' if os.name == 'nt' else 'clear')
     print("""\033[1;33m                                                                
 _____             _                                            
| __  |___ ___ ___| |_ _ ___ ___    ___ ___ _ _ ___ ___ ___ ___ 
|    -| -_|_ -| . | | | | -_|  _|  | -_| . | | | .'|  _| .'| . |
|__|__|___|___|___|_|\_/|___|_|    |___|_  |___|__,|___|__,|___|
                                         |_|                    

""")
     a = input('[*] - Insira aqui o primeiro numero que aparece na equacao antes da igualdade : ')
     b = input('[*] - Insira aqui o numero que esta apos a igualdade : ')
     x = input('[*] - Insira aqui o valor de x (Caso o valor de x for um, insira 1) : ')
     print ('\n[1] - Soma')
     print ('[2] - Subtração')
     print ('[3] - Multiplicacão')
     print ('[4] - Divisão\n')
     operacao = input('[*] - Insira aqui a operação desejada : ')
     if operacao == '1':    
        resultado = (int(b) - int(a))
        resultado = (int(resultado) / int(x))
        print('[!] - Equação realizada com sucesso, X = ' + str(resultado))
     elif operacao == '2':
          resultado = (int(b) + int(a))
          resultado = (int(resultado) / int(x))
          print('[!] - Equação realizada com sucesso, X = ' + str(resultado))
     elif operacao == '3': 
          resultado = (int(b) * int(a))
          resultado = (int(resultado) / int(x))
          print('[!] - Equação realizada com sucesso, X = ' + str(resultado))
     elif operacao == '4':
          resultado = (int(b) / int(a))
          resultado = (int(resultado) / int(x))
          print('[!] - Equação realizada com sucesso, X = ' + str(resultado))
     
def calculadora():
     os.system('cls' if os.name == 'nt' else 'clear')
     print("""\033[1;31m                                           
 _____     _         _       _             
|     |___| |___ _ _| |___ _| |___ ___ ___ 
|   --| .'| |  _| | | | .'| . | . |  _| .'|
|_____|__,|_|___|___|_|__,|___|___|_| |__,|
                                           

""")
     valor1 = input('[*] - Insira o primeiro número que deseja utilizar na operação : ')
     valor2 = input('[*] - Insira o segundo valor que deseja utilizar na operação : ')
     operacao = input('\n[1] - Soma\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão\n\n[*] - Qual operação das listadas acima deseja utilizar ? ')
     print('')
     if operacao == '1':    
        resultado = (int(valor1) + int(valor2))
        print('[!] - A soma realizada é igual a : ' + str(resultado))
     elif operacao == '2':
          if valor1 > valor2:
               resultado = (int(valor1) - int(valor2))
          else:
               resultado = (int(valor2) - int(valor1))
          print('[!] - A subtração realizada é igual a : ' + str(resultado))
     elif operacao == '3': 
          resultado = (int(valor1) * int(valor2))
          print('[!] - A multiplicação realizada é igual a : ' + str(resultado))
     elif operacao == '4':
          if valor1 > valor2:
               resultado = (int(valor1) / int(valor2))
          else:
               resultado = (int(valor2) / int(valor1))
          print('[!] - A divisão realizada é igual a : ' + str(resultado))

def calcular():
      os.system('cls' if os.name == 'nt' else 'clear')
      print("""\033[1;32m
                                                      
 _____   _                       _    _____     _     
|  _  |_| |_ _ ___ ___ ___ ___ _| |  |     |___| |___ 
|     | . | | | .'|   |  _| -_| . |  |   --| .'| |  _|
|__|__|___|\_/|__,|_|_|___|___|___|  |_____|__,|_|___|
                                                      
Made by - yThresh
Instagram - @ythresh666
Discord - ythresh#5593
""")
      print('[1] - Calcular regra de 3\n[2] - Resolver equação\n[3] - Calculadora normal\n')
      ops = input('Qual modo deseja usar ? ')
      if ops == '1':
         regra3()
      elif ops == '2':
           equation()
      elif ops == '3':
           calculadora()


calcular()
while True:
     mais_um = input('\n[?] - Deseja fazer uma nova operação ? [S/N] ')
     if mais_um.upper() == 'S':
        calcular()
     elif mais_um.upper() == 'N':
          exit()

