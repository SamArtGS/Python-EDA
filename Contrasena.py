contrasena = "SamArtGS75"
print("Nombre de usuario: Samuel Art GS")
def correcta(contrasena):
    correct=input("Contraseña: ")
    intentos = 0
    while correct != contrasena:
        if intentos == 3:
            print("Contraseña ingresada incorrectamente varias veces... Espere...")
            return True
        else:
            if correct == contrasena:
                print("Bienvenido")
                return True
            else:
                print("Contraseña incorrecta, favor de ingresar la correcta")
                intentos = intentos+1
print(correcta(contrasena) != False)