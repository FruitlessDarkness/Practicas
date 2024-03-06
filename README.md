# Practicas
# Problema 1
print ("¿Que fecha es hoy?")
x=input("")
print("¿En que fecha naciste?")
y=input("")
if x==y:
    print("Hoy es tu cumpleaños")
elif x<y:
    print("Hoy no es tu cumpleaños")
elif x>y:
    print("Hoy no es tu cumpleaños")
# Problema 2
num1=float(input("Ingrese el primer número: "))
num2=float(input("Ingresa el segundo número: "))
num3=float(input("Ingrese el tercer número: "))
num4=float(input("Ingresa el cuarto número: "))
suma= num1+num2
producto= num3*num4
if suma==producto:
    print(f"Los numeros coinciden {num1}+{num2}={num3}*{num4}={suma}")
else:
    print("Los numeros no coinciden")
# Problema 3