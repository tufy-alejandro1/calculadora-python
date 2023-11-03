def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "No se puede dividir por cero."
    return a / b

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

print("Selecciona una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

choice = input("Ingresa la opción (1/2/3/4):")

if choice == '1':
    print("Resultado:", suma(num1, num2))

elif choice == '2':
    print("Resultado:", resta(num1, num2))

elif choice == '3':
    print("Resultado:", multiplicacion(num1, num2))

elif choice == '4':
    print("Resultado:", division(num1, num2))
else:
    print("Opción no válida")