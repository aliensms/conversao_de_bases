#Primeiro vamos converter o valor desejado para base decimal:

def converte_pdecimal(num, b1):    #Função para a conversão de qualquer base para base 10, ultilizando o método de expansão.
    result = 0                     #A variável result vai armazenar o resultado PARCIAL da conversão
#A variavel começa com o valor zero mas atualiza a cada interação com o for.
    for i in str(num):                #O for vai percorrer o numero, que agora está declarado como uma STRING
        result = result * b1 + int(i) #Começa a operação com o valor zero, que é multiplicado pela base de origem e depois somado com o algorismo que esta sendo lido (da esquerda para direita)
        #(agora o num esta declarado como um inteiro)
    return(result)                    #Após o for percorrer todos os algorismos da string, a função retorna o resultado da conversão.

#Agora podemos converter o número em base decimal para qualque outra base:

def convert_qlqrBase(num, b2):     #Função para converter base decimal para qualquer outra base
    dig = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Todos os digitos que possam ser usados em qualquer base até 36
    result = ""                                  #Vai armazenar o resultado da conversão
    
    if num == 0:                                 #Caso a entrada do valor seja igual a zero o programa vai automaticamente devolver 0.
        return "0"
    
    while num > 0:                       #Enquanto NUM for maior que ZERO o programa vai continuar rodando nosso loop principal.
        divResto = num % b2              #Calcula o resto da divisão entre o valor e a base de destino
        result = dig[divResto] + result  #O resto da divisâo fica como indice na variavel "dig", digito esse que é adicionado a esquerda na variavel RESULT
        num = num // b2                  #num é dividio pela base de destino e o loop se repete
    return result          #Ao fim do loop, enfim a função retorna o resultado da conversão

#Entradas:

num = int(input("Quantidade a ser convertida: "))
b1 = int(input("Base de origem: ")) 
b2 = int(input("Base de destino: "))

if b1 == None:  #Caso a entrada do usuário esteja vazia, considera-se como base 10 (Valor Default)
    b1 = 10
if b2 == None:
    b2 = 10

valor_decimal = converte_pdecimal(num,b1) #Aplicamos a função converte_pdecimal nas duas entradas, valor a ser convertido e base de origem
num = valor_decimal                       #NUM assume o valor em base decimal
valorFinal = convert_qlqrBase(num, b2)    #A variavel valorFinal vai armazenar o resultado da função convert_qlqrbase aplicada no valor a ser converitdo e base de destino
#Assim obtemos o resultado da conversão

if b2 == 10:  #Caso a base de destino seja 10
    print(num, "na base" ,b1, "equivale a:", valorFinal, "na base", b2) #Imprime apenas uma saída
else:         #Em outros casos:
    print(num, "na base" ,b1, "equivale a:", valorFinal, "na base", b2) #Imprime o resultado da conversão
    print('valor equivalente na base 10:', valor_decimal)               #E também seu equivalente na base 10