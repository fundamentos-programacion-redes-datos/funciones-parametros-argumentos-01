"""


"""
# Define la función (procedimiento) con 4 parámetros
# Se asigna un valor por defecto al parámetro "lista_notas"
def generar_reporte(nombre, apellido, edad, lista_notas=[10, 10, 5]):
    """
    Función que genera un reporte de notas a partir de la información
    de un estudiante, incluyendo nombre, apellido, edad y una lista de notas.
    Calcula el promedio de las notas y muestra el informe formateado.
    """

    # Calcula la suma total de las notas contenidas en lista_notas
    suma_notas = sum(lista_notas)  
    
    # Calcula el promedio dividiendo la suma entre la cantidad de notas
    promedio_notas = suma_notas / len(lista_notas)  
    
    # Se genera el reporte en función de las variables recibidas como parámetros
    mensaje_final = "Reporte de Notas\n"  
    mensaje_final = f"{mensaje_final}Nombres y Apellidos: {nombre} {apellido}\n" \
                    f"Edad: {edad}\n\n" \
                    f"Notas:\n"
    
    # Se recorre la lista de notas para agregarlas al reporte, usando un bucle for
    for i in lista_notas:
        mensaje_final = f"{mensaje_final}{i}\n"

    # Se agrega el promedio final al reporte, formateado con 2 decimales
    mensaje_final = f"{mensaje_final}Promedio: {promedio_notas:.2f}"  
    
    # Se muestra el mensaje final con los datos del estudiante
    print(mensaje_final)


# Define el punto de entrada principal del script
# Garantiza que el código dentro de este bloque solo se ejecute si el script
# es ejecutado directamente y no si se importa como módulo en otro archivo
if __name__ == "__main__":
    #
    # Se crea una lista con las notas del estudiante
    mi_lista_notas = [10, 9, 8.5]
    
    # Se invoca la función "generar_reporte" enviando 4 argumentos explícitos
    # En este caso, el parámetro "lista_notas" recibe un argumento personalizado
    generar_reporte("María Elizabeth", "García López", 25, mi_lista_notas)
    
    print("--------------------------------")

    # Se invoca la función sin enviar un argumento para "lista_notas"
    # Como el parámetro tiene un valor por defecto ([10, 10, 5]),
    # la función utilizará esa lista de manera automática
    generar_reporte("Paul José", "Benítez Salazar", 20)



