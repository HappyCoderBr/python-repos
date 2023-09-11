'''programa para validar datas'''
#bissexto FEV = 29 d, de resto tudo igual 
#31 28 31 30. 31 30 31 31. 30 31 30 31 == normal

#loop para executar o programa
while True:
    #input para o dia
    var_dia = int(input('Digite o dia: '))
    #input para o mes
    var_mes = int(input('Digite o mes: '))
    #input para o ano
    var_ano = int(input('Digite o ano: '))
    
    #validar a data digitada
    if var_ano > 0 and var_mes > 0 and var_mes < 13 and var_dia > 0 and var_dia < 32:
        #verificar se o ano e bissexto
        if var_ano % 4 == 0 and var_mes == 2 and var_dia < 30:
        #notificar o usuario se a data e valida
            print('A data digitada e valida!')
        elif var_mes != 2 and var_dia < 32:
            print('A data digitada e valida!')
        else:
            print('A data digitada e invalida!')
    else:
        print('A data e invalida!')
    
    #perguntar se o usuario quer rodar o module de novo
    var_rerun = int(input('Se desejar executar o module de novo digite 0, caso contrario digite 1'))
    #se digitado 0, o programa roda de novo
    if var_rerun == 0:
        continue
    #se digitado 1 o programa sera terminado
    if var_rerun == 1:
        break
            
            
            
            

            
        
    

