# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Pacote que trata a imagem PIL e a retorna como JPEG
"""

from io import BytesIO
from flask import send_file, Response
from PIL import Image


def tratar_imagem_pil(imagem_meme: "Image") -> "BytesIO":
    """
    Processa uma imagem de meme.

    Salva a imagem de meme no formato JPEG com uma qualidade de 70%, utilizando um objeto BytesIO.
    Move o ponteiro de leitura/escrita para o início do objeto BytesIO.

    Args:
        imagem_meme: Objeto de imagem Pillow (PIL) representando o meme.

    Returns:
        meme_io: Objeto BytesIO contendo a imagem do meme processada.
    """
    # Cria uma instância de BytesIO
    meme_io = BytesIO()

    # Salva 'imagem_meme' no formato JPEG
    imagem_meme.save(meme_io, format="JPEG", quality=70)

    # Move o ponteiro de leitura/escrita para o início do objeto BytesIO
    meme_io.seek(0)

    return meme_io


def send_file_meme(img_meme: Image.Image) -> Response:
    """
    Envia um arquivo de imagem JPEG como resposta HTTP.

    Processa a imagem do meme usando a função tratar_imagem_pil para obter um objeto BytesIO.
    Em seguida, envia o objeto BytesIO como resposta HTTP utilizando a função send_file do Flask,
    especificando o tipo de mídia como 'image/jpeg'.

    Args:
        img_meme: Objeto de imagem Pillow (PIL) representando o meme.

    Returns:
        response: Resposta HTTP contendo a imagem do meme processada.
    """
    obj_io = tratar_imagem_pil(img_meme)

    return send_file(obj_io, mimetype="image/jpeg")
