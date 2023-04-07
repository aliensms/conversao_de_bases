#Entradas em que o usuario ira informar os dados necessarios para a conversao de base. 
#num = quantidade a ser convertida, b1 = base de origem e b2 = base de destino.

num = int(input("Quantidade a ser convertida: "))
b1 = int(input("Base de origem: "))
b2 = int(input("Base de destino: "))

#verifica-se se as entradas das bases sao vazias ou nao.
#Caso esteja vazia considera-se a base como base 10.

if b1 == None: 
    b1 = 10

if b2 == None: 
    b2 = 10

#Aqui faremos a conversão de qualquer base para base 10
if b1 == 2:
    if b2 == 10:
        result = 0 #A variável result vai armazenar o resultado PARCIAL da conversão, começa com o valor zero mas atualiza a cada interação com o for.
    #Implementando o método de expansão de base para conversão
        for i in str(num): #O for vai percorrer o numero, que anteriormente foi declarado como uma STRING
            result = result * b1 + int(i) 
        print(num, "na base" ,b1, "equivale a:", result, "na base", b2)

if b1 == 10:
    if b2 == 8:
        cont = num / 8
        result = (int(cont) * 2) + num
        print(result)

print('ok')