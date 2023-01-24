import random
# NOMES DAS PESSOAS
pessoas = ['caio','pedro','matheus','joão','everton','renan']

def separador_grupos(lista_pessoas,pessoas_por_grupo) :
    random.shuffle(lista_pessoas)
    index = 1 # IDENTIFICADOR DO GRUPO

    grupo = []
    
    for pessoa in lista_pessoas :
        grupo.append(pessoa)
        
        if len(grupo) == pessoas_por_grupo :
            print(f"Grupo {index}: {grupo}")
            grupo = []
            index = index + 1
    
    if(grupo != []) :
        print(f"Grupo {index}: {grupo}")
            
separador_grupos(pessoas,4)