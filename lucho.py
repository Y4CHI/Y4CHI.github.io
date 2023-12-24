from PIL import Image
import os

def convertir_png_a_webp(entrada, salida):
    try:
        # Abre la imagen PNG
        imagen_png = Image.open(entrada)

        # Guarda la imagen en formato WebP
        imagen_png.save(salida, 'WEBP')

        print(f'La conversión de {entrada} a {salida} fue exitosa.')

    except Exception as e:
        print(f'Ocurrió un error: {e}')

if __name__ == "__main__":
    # Rutas de entrada y salida
    carpeta_entrada = "C:\\Users\\black\\Pictures\\lucho-imagenes"
    carpeta_salida = "C:\\Users\\black\\Pictures\\lucho-imagenes\\modificada"

    # Verifica si la carpeta de entrada existe
    if os.path.exists(carpeta_entrada) and os.path.isdir(carpeta_entrada):
        # Crea la carpeta de salida si no existe
        os.makedirs(carpeta_salida, exist_ok=True)

        # Procesa cada imagen en la carpeta de entrada
        for i in range(15):
            nombre_archivo = f"{str(i).zfill(2)}.png"
            ruta_entrada = os.path.join(carpeta_entrada, nombre_archivo)
            ruta_salida = os.path.join(carpeta_salida, nombre_archivo.replace('.png', '.webp'))
            convertir_png_a_webp(ruta_entrada, ruta_salida)
    else:
        print(f'La carpeta de entrada {carpeta_entrada} no existe.')

    
    
