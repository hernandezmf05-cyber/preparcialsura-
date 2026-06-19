#Entradas del sistema
nombre_usuario=input("digita tu nombre: ") 
correo_usuario=input("digita tu correo: ") 
contraseña_usuario=input("digita tu contraseña: ") 
ciudad_usuario=input("digita tu ciudad: ") 
edad_usuario=int(input("digita tu edad: ")) 

CORREO_BD="prueba@gmail.com"
CONTRASEÑA_BD="admin123"

#Condicional en python
if(correo_usuario==CORREO_BD and contraseña_usuario==CONTRASEÑA_BD):
    print("bienvenido al sistema 🆗")
else:
    print("fallamos en tu autenticacion ✖️")
