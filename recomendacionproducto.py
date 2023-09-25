class Producto:
    def __init__(self, nombre, caracteristicas):
        self.nombre = nombre
        self.caracteristicas = caracteristicas

class Cliente:
    def __init__(self, nombre, preferencias):
        self.nombre = nombre
        self.preferencias = preferencias

class NodoDecision:
    def __init__(self, pregunta, rama_si, rama_no):
        self.pregunta = pregunta
        self.rama_si = rama_si
        self.rama_no = rama_no

def generar_recomendaciones_arbol(cliente, nodo_decision, productos):
    if isinstance(nodo_decision, Producto):
        return [nodo_decision]

    if nodo_decision.pregunta in cliente.preferencias:
        recomendaciones_rama = generar_recomendaciones_arbol(cliente, nodo_decision.rama_si, productos)
    else:
        recomendaciones_rama = generar_recomendaciones_arbol(cliente, nodo_decision.rama_no, productos)

    return recomendaciones_rama

# Construir un árbol de decisiones
arbol_decision = NodoDecision(
    pregunta="herramienta",
    rama_si=NodoDecision(
        pregunta="metal",
        rama_si=Producto("Martillo", ["herramienta", "metal"]),
        rama_no=Producto("Destornillador", ["herramienta", "metal"])
    ),
    rama_no=NodoDecision(
        pregunta="limpieza",
        rama_si=Producto("Cepillo", ["limpieza", "cerdas"]),
        rama_no=Producto("Escoba", ["limpieza", "cerdas"])
    )
)
productos = [
    Producto("Sierra", ["herramienta", "metal"]),
    Producto("Pintura", ["decoración", "pintura"]),
    Producto("Tornillo", ["herramienta", "metal"]),
]
nombre_cliente = input("Ingresa tu nombre: ")
preferencias_cliente = input("Ingresa tus preferencias separadas por comas (por ejemplo: herramienta,metal): ").split(',')
cliente_personalizado = Cliente(nombre_cliente, preferencias_cliente)
recomendaciones_cliente = generar_recomendaciones_arbol(cliente_personalizado, arbol_decision, productos)
print(f"\nRecomendaciones para {cliente_personalizado.nombre}:")
for producto in recomendaciones_cliente:
    print(producto.nombre)
