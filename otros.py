from PIL import Image

for i in range(1,2):
    numero = str(i)
    numero_formateado = f"00{i}" + ".jpg"
    imagen_png = Image.open(numero_formateado)
    imagen_png.save(f"00{i}" + ".webp", 'webp')
    print(f"Convertido: {numero_formateado}")
#LuchoPingon