import random

print("=========================================================")
print("   SISTEMA DE CIBERSEGURIDAD: GENERADOR DE CONTRASEÑAS   ")
print("=========================================================\n")

# Guardamos los caracteres en una lista de texto común y corriente
letras_y_simbolos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"

opcion = 0

# Bucle principal (Mientras la opción no sea 3, el programa sigue)
while opcion != 3:
    print("--- MENÚ PRINCIPAL ---")
    print("1. Generar nueva contraseña segura")
    print("2. Ver consejos de seguridad")
    print("3. Salir del sistema")
    
    opcion = int(input("Selecciona una opción (1-3): "))
    
    # Opción 1: Generar la contraseña
    if opcion == 1:
        print("\n----------------------------------------")
        largo = int(input("Ingresa el tamaño para tu contraseña (mínimo 8): "))
        
        if largo < 8:
            print("El tamaño mínimo debe ser de 8 caracteres.")
        else:
            contrasena_creada = ""
            contador = 0
            
            # Este ciclo saca letras al azar una por una hasta completar el largo
            while contador < largo:
                letra_al_azar = random.choice(letras_y_simbolos)
                contrasena_creada = contrasena_creada + letra_al_azar
                contador = contador + 1
                
            print("\n ¡Tu contraseña segura es!:", contrasena_creada)
        
    # Opción 2: Mostrar consejos sencillos
    elif opcion == 2:
        print("\n===================================")
        print("--- CONSEJOS DE SEGURIDAD ---")
        print("===================================")
        print("1. No uses tu nombre ni tu cumpleaños.")
        print("2. Usa una contraseña diferente para cada cuenta.")
        print("3. Cambia tus claves importantes seguido.\n")
        
    # Opción 3: Salir
    elif opcion == 3:
        print("\n Sistema cerrado. ¡Gracias por usar el programa!")
        
    else:
        print("\n Opción no válida. Intenta de nuevo.\n")