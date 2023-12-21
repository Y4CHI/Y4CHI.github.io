from PIL import Image

# Abrir la imagen PNG
imagen_png = Image.open('inicio.png')

# Guardar la imagen en formato WebP
imagen_png.save('inicio.webp', 'webp')

print("Imagen convertida a WebP con éxito.")
