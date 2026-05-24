
# --- PARTE 2: RESULTADOS ---

ruta_archivo = "datos/ventas.csv"

def obtener_analisis():
    ventas_totales = 0
    productos_cantidad = {} # Diccionario para guardar: {"nombre_producto": cantidad_total}
    
    with open(ruta_archivo, "r") as archivo:
        next(archivo) # Saltamos los títulos
        for linea in archivo:
            datos = linea.strip().split(",")
            nombre = datos[1]
            cantidad = int(datos[2])
            precio = float(datos[3])
            
            # Sumar venta total
            ventas_totales += cantidad * precio
            
            # Sumar cantidad por producto
            productos_cantidad[nombre] = productos_cantidad.get(nombre, 0) + cantidad
                
    # Buscar el más vendido
    mas_vendido = max(productos_cantidad, key=productos_cantidad.get)
    
    # --- Guardamos el resultado en la carpeta resultados ---
    with open("resultados/reporte.txt", "w") as f:
        f.write(f"Ventas Totales: ${ventas_totales:.2f}\n")
        f.write(f"Producto más vendido: {mas_vendido} ({productos_cantidad[mas_vendido]} unidades)\n")

# Ejecutamos la función
obtener_analisis()
