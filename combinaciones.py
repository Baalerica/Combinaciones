import random

# Lista de artículos con precios
items = [
    ("Faro auxiliar para moto iron Racing luz blanca", 199),
    ("Direccionales azules para motocicleta iron Racing", 99),
    ("Faro auxiliar iron Racing", 549),
    ("2 Barra mini led IOL 7 pulgadas luz blanco", 399),
    ("Par de faros de lupa 60w luz led para moto", 1069),
    ("Faros ojo de ángel led luz auxiliar u7 lupa demonio", 1029),
    ("Par faro 34 led Eo safe imports esi-6141", 719),
    ("Cubierta de empuñadora de motocicleta luz led", 1720),
    ("Calavera trasera de led", 418),
    ("Alforjas laterales para motocicleta eo safe ESI-9002", 1429),
    ("Par de alforjas laterales de cuero hmr", 3450),
    ("Alforjas como las actuales", 4330),
    ("Bolsa portaherramienta como la de tu ama", 829),
    ("Bolsa para motocicleta belug color negro", 1429),
    ("Escritorio en L Arlette", 1999),
    ("Silla Oficina reclinable", 1699),
    ("Disco duro externo 2 TB", 2399),
    ("Disco duro externo 1 TB", 1699),
    ("Tablet apple 6ta", 4000),
    ("Tableta Lenovo M7", 3599),
    ("Tableta digitalizadora", 899),
    ("Apple watch", 5499),
    ("Memoria microSD 32", 105),
    ("Tripie Element mobbt 4 secciones", 4786),
    ("Kit de luces de fotografía", 1819),
    ("Correa para cámara", 497),
    ("Soporte para smartphone", 299),
]

# Presupuesto máximo
budget = 8500
max_combinations = 30  # Número máximo de combinaciones deseadas

# Función para generar combinaciones aleatorias dinámicamente
def generate_random_combinations(items, budget, max_combinations):
    random_combinations = []
    while len(random_combinations) < max_combinations:
        combo = random.sample(items, random.randint(1, len(items)))  # Generar una combinación aleatoria
        total_price = sum(item[1] for item in combo)
        if total_price <= budget:
            random_combinations.append((combo, total_price))
    
    # Ordenar por proximidad al presupuesto
    random_combinations.sort(key=lambda x: abs(budget - x[1]))
    return random_combinations

# Generar combinaciones aleatorias
random_combinations = generate_random_combinations(items, budget, max_combinations)

# Crear archivo de salida
output_path = "optimized_random_combinations2.txt"

with open(output_path, "w", encoding="utf-8") as file:
    file.write(f"Total de combinaciones generadas: {len(random_combinations)}\n\n")
    for i, (combo, total_price) in enumerate(random_combinations, start=1):
        combo_names = [item[0] for item in combo]
        file.write(f"Combinación {i}:\n")
        file.write(f"  Artículos: {', '.join(combo_names)}\n")
        file.write(f"  Precio total: ${total_price}\n\n")

print(f"Archivo generado: {output_path}")
