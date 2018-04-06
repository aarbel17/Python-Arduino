#Alejandro Arbelaez Ramirez

def guardar_datos(datos):
    archivo = open("Datos.csv", "a")
    archivo.write(str(datos))
    archivo.write("\n")
    archivo.close()
def obtener_fecha():
    import datetime
    fec=datetime.datetime.now()
    d=fec.day
    m=fec.month
    y=fec.year
    h=fec.hour
    mi=fec.minute
    s=fec.second
    v=[d,m,y,h,mi,s]
    return(v)
def graficar(x,y,nombre):
    import matplotlib.pyplot as plt
    import numpy as np
    plt.plot(x,y)
    plt.title(nombre)
    plt.grid()
    plt.show()
def leer(archivo):
    d=open(archivo)
    d=d.readlines()

    #Inicializa la lista dat
    dat=[]

    #Ciclo para eliminacion de \n, , y ;
    for i in d:
        a=i.strip()
        dat.append(a)
    return dat

import serial
arduino = serial.Serial('COM6', 115200, timeout=.1)

r=input("Ingresar 1 para tomar datos: \n")
if r==1:
    c=[]
    f=[]
    k=[]
    h=[]
    fecha=[]

    v=['t','f','k','h']
    for i in range(4):
        for i in v:
            arduino.write(i)
            data = float(arduino.readline().strip())
            if i == 't':
                c.append(data)
            elif i=='f':
                f.append(data)
            elif i =='k':
                k.append(data)
            elif i=='h':
                h.append(data)
            import time
            time.sleep(0.12)
    for i in range(len(c)):
        temp=[c[i],f[i],k[i],h[i]]
        guardar_datos(temp)
    print("Archivo guardado")

else:
    print("No se adquirieron datos")
