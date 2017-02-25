# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont


def generar_imagen_UV(fecha, hora, imagen):
    """
    Está función sirve para generar la imágenes de piranometro UV para twitter.
    :param fecha: fecha inicial de la imagen de piranómetro
    :param hora: hora inicial
    :param imagen: el nombre la imagen
    :return:
    """
    resultado = Image.new("RGB", (1240, 990))
    lateral = Image.open('menu.jpeg')

    cabecera = Image.open('header.jpeg')
    cabecera.thumbnail((1240, 306), Image.ANTIALIAS)
    resultado.paste(cabecera, (0, 0, 0 + 1240, 0 + 306))

    img = Image.open(imagen)
    width = 907
    height = 534
    im = img.resize((width, height), Image.ANTIALIAS)
    resultado.paste(im, (0, 306, 0 + 907, 306 + 534))

    lateral.thumbnail((333, 534), Image.ANTIALIAS)
    resultado.paste(lateral, (907, 306, 907 + 333, 306 + 534))

    pie = Image.open('footer.jpeg')
    pie.thumbnail((1240, 162), Image.ANTIALIAS)
    resultado.paste(pie, (0, 306 + 534, 1240, 306 + 534 + 162))

    font = ImageFont.truetype("arial.ttf", 50)
    fecha_hora = fecha + " " + hora
    draw = ImageDraw.Draw(resultado)

    draw.text((400, 240), fecha_hora, fill="white", font=font)
    resultado.save('radar.png')

if __name__ == '__main__':
    fecha = '2017-02-20'
    hora = '19:28'
    img = 'imagen.png'
    generar_imagen_UV(fecha, hora, img)
