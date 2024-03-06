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