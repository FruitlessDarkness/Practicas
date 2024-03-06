codigo_postal=int(input("Por favor, ingresa tu código postal: "))
if 50000<=codigo_postal<=50030:
    print("Estas dentro del rango de entrega")
else:
    print ("Lo siento, no puedo entregar a tu ubicacion \U0001F641")