import random
a=0
valores=[]
while a<1000:
    a+=1
    num= random.randint(100,500)
    valores.append(num)


def calcular_total(*args,**keyargs):
    a=0
    valor=0
    while a < 1000:
        valor = valor+args[0][a]
        a+=1

    
    
    valor = str(valor)
    valor_total = "Total a pagar: R$ " + valor
    print(valor_total)


calcular_total(valores)