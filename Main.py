#funcao secundaria 1
def filho1(argumento):
    print(f'Filho 1 escreveu: "{argumento}" .')

#funcao secundaria 2
def filho2(argumento,quantidade):
    if quantidade >= 1:
        for i in range(quantidade):
            print(f'Filho 2 na vez {i+1} escreveu: "{argumento}" .')
    else:
        print(f"A quantidade:'{quantidade}' não é válida.")

#funcao principal
def pai(*args):
    print("Filho 1",end=" ")
    if len(args)>=1:
        print()
        executado=0
        for argumento in args:
            if type(argumento)==str:
                filho1(argumento)
                executado+=1
        if executado == 0:
            print(f"Não possui 'str' .")
    else:
        print("Não executado.")
    print("Filho 2",end=" ")
    if len(args)>=2:
        print()
        executado1=executado2=0
        for argumento in args:
            if type(argumento)==str:                
                for quantidade in args:
                    if type(quantidade)==int:
                        filho2(argumento,quantidade)
                        executado2+=1
                if executado2 == 0:
                    print(f"Não possui 'int' .")
                executado1+=1
            if executado1>0 and executado2==0:
                print("Filho 2 encerrado")
                break
        if executado1 == 0:
            print(f"Não possui 'str' .")
    else:
        print("Não executado.")


print('pai()')
pai()
print()
print('pai("oi")')
pai("oi")
print()
print('pai("Olá","oi")')
pai("Olá","oi")            
print()
print('pai(1)')
pai(1)
print()
print('pai(1,2)')
pai(1,2)
print()
print('pai(1,"oi")')
pai(1,"oi")
print()
print('pai("Olá",1)')
pai("Olá",1)
print()
print('pai("Olá",2,1)')
pai("Olá",2,1)
print()
print('pai("Olá",1,"oi")')
pai("Olá",1,"oi")
print()
print('pai("Olá",1,"oi",2)')
pai("Olá",1,"oi",2)
print()
