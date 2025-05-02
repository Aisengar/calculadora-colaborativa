def suma(a,b):
    """
        suma los terminos
        arg:
        a(int): numero 1
        b(int): numero 2
    """
    return a + b


def resta(a,b):
    """
        resta los terminos
        arg:
        a(int): numero 1
        b(int): numero 2    
    """
    return a - b


def multiplicacipon(a,b):
    """
        multiplica los terminos
        arg:
        a(int): numero 1
        b(int): numero 2
    """
    return a * b


def division(a,b):
    """
        divide los terminos
        arg:
        a(int): numero 1
        b(int): numero 2
    """
    try:
        division = a/b
        return division
    except ZeroDivisionError:
        print("No se perite la divicion por Zero")
    except ValueError:
        print('No se permiten numero float o cadenas de texto')

def menu():
    """
        Menu de seleccion de Operaciones Matematicas
        arg:
        opcion(str): opcion seleccionada por el usuario
    """

    try:
        print("Calculadora Básica")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion not in ['0','1','2','3','4']:
            print('La opción tiene que ser un número entre 0 y 4.')
            opcion = input("Selecciona una opción valida: ")
        return opcion
    except ValueError:
        print('No se permiten cadenas de caracteres')
        print('Ocurrió un error inesperado con el valor ingresado.') # General message as specific ValueError isn't likely here


def main(opcion):
    """
        Logica principal de la calculadora
        arg:
        a(int): numero seleccionado por el usuario
        b(int): numero seleccionado por el usuario
    """
    try:
        if opcion != "0":
            a = int(input("Ingresa el primer número: "))
            b = int(input("Ingresa el segundo número: ")) 
        match opcion:
            case "1":
                print("Resultado de la suma: ", suma(a,b))
            case "2":
                print("Resultado de la resta: ", resta(a,b))
            case "3":
                print("Resultado de la resta: ", multiplicacipon(a,b))
            case "4":
                print("Resultado de la resta: ", division(a,b))
            case "0":
                print("Saliendo de la calculadora...")
            case _: 
                print("Opción no válida. Por favor, selecciona una opción válida Intentalo nuevamente.")
    except ValueError:
        print("Error: Debes ingresar números enteros.")

        


def calculadora():
     opcion = 1
     while opcion != "0":
        opcion = menu()
        main(opcion)

#Inicialisador de Calculadora
Calculadora = calculadora()

