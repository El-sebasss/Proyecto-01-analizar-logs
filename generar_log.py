#!/usr/bin/env python3

fecha = "2025-01-15"
hora = "14:23:01"
ip = "192.168.1.10"
metodo = "GET"
ruta = "/productos"
codigo = 200


with open("data/acceso.log", "w") as f:
     for i in range(10):
       linea = f"{fecha} {hora} {ip} {metodo} {ruta} {codigo}\n"
       f.write(linea)

print("Listo: data/acceso.log generado con 10 lineas ") 
