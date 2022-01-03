#-*- coding: utf-8 -*-

def fibonacci(x):
    a, b= 0, 1
    for i in range(1,x+1):
        a, b= b,a + b
        print("{}) a: {}y b:{}".format(i,a,b))

def limite():
    #variable local
    while True:
        try:
            var= int(input("ingresa hasta que vuelta llega fibonacci: "))
            fibonacci(var)
            break
        except:
            print("debes ingresar un entero")
        
limite()
