a, b, c = (float(i) for i in input().split())
triangulo = (a * c)/2
circulo = 3.14159 * (c * c)
trapezio = c * (a + b) / 2
quadrado = b * b
retangulo = a * b
print("TRIANGULO: %0.3f" % triangulo)
print("CIRCULO: %0.3f" % circulo)
print("TRAPEZIO: %0.3f" % trapezio)
print("QUADRADO: %0.3f" % quadrado)
print("RETANGULO: %0.3f" % retangulo)
