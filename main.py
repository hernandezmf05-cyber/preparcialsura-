import random

#llamando las funciones
from funcionUno import ingresar_usuarios
from funcionDos import crear_listado
from funcionTres import clasificar_prenda

ingresar_usuarios("juan@gmail.com", "admin123", "james falcao", 8, "la mazea")
prenda={
        "id":random.randint(1,100),
        "tipo":random.choice(["camiseta","jean","pantalon","correa","zapatos"]),
        "marca":random.choice(["Arturo Calle","albertoVO5","gorditos SEXY","lolas","ardidas"]),
        "precio": random.choice([25000,30000,70000,42000]),
        "estado": random.choice(["bueno","optimo","regular"])
    }
crear_listado(10,prenda)

clasificar_prenda("REGULAR")