def es_cedula_valida(cedula):
    # Asegurarse de que la cédula tenga exactamente 10 dígitos
    if len(cedula) != 10 or not cedula.isdigit():
        return False
    
    # Extraer los primeros 9 dígitos
    primeros_nueve = cedula[:-1]
    # Extraer el décimo dígito que es el dígito de verificación
    digito_verificacion = int(cedula[-1])

    # Multiplicadores alternos para el cálculo del dígito de verificación
    multiplicadores = [2, 1]  # alternancia 2, 1

    # Realizar la multiplicación alterna y ajustar resultados mayores que 9
    suma_total = 0
    for i, digito in enumerate(primeros_nueve):
        digito_int = int(digito)
        multiplicador = multiplicadores[i % 2]  # alternar entre 2 y 1
        resultado = digito_int * multiplicador
        
        # Si el resultado es mayor que 9, se suma el doble dígito para reducir a uno solo
        if resultado > 9:
            resultado = resultado - 9
        
        suma_total += resultado

    # Calcular el dígito de verificación esperado
    digito_verificacion_esperado = (10 - (suma_total % 10)) % 10

    # Comparar el dígito calculado con el dígito de verificación
    return digito_verificacion_esperado == digito_verificacion


# Ejemplo de uso
cedula = "0942445743"  # Cambia por cualquier número de cédula ecuatoriana para probar
if es_cedula_valida(cedula):
    print("La cédula es válida")
else:
    print("La cédula no es válida")