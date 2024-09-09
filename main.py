def suma(a, b):
    """Devuelve la suma de a y b."""
    return a + b

def resta(a, b):
    """Devuelve la resta de a menos b."""
    return a - b

def multiplicacion(a, b):
    """Devuelve el producto de a y b."""
    return a * b

def division(a, b):
    """Devuelve la división de a entre b. Lanza un error si b es 0."""
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b
