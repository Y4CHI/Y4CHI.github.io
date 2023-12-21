from PIL import Image

for i in range(2,4):
    numero = str(i)
    numero_formateado = "node2" + ".png"
    imagen_png = Image.open(numero_formateado)
    imagen_png.save("001" + ".webp", 'webp')
    print(f"Convertido: {numero_formateado}")
#LuchoPingon