#Necesito crear 1000000 prendas que tengan
#id
#tipo
#marca
#precio
#estado
import random

prendas=[]
for i in range(1000000):
    prenda={
        "id":random.randint(1,100),
        "tipo":random.choice(["camiseta","jean","pantalon","correa","zapatos"]),
        "marca":random.choice(["Arturo Calle","albertoVO5","gorditos SEXY","lolas","ardidas"]),
        "precio": random.choice([25000,30000,70000,42000]),
        "estado": random.choice(["bueno","optimo","regular"])
    }
    prendas.append(prenda)
print(prendas)
