# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 20:27:02 2024

@author: user
"""

from PIL import Image
from tkinter import filedialog as fd
import pillow_avif
import os


local_atual = os.path.abspath(os.getcwd())

path = fd.askopenfilename(title = "Selecione a imagem",
                          initialdir = local_atual,
                          filetypes = (
                              ("image files", ".webp"),
                              ("image files", ".AVIF")
                              )
                          )

if path != "":
    
    Imagem = Image.open(path)
    
    path_dps_poto = path[: path.find(".")]
    
    png = Imagem.convert("RGBA")
    
    png.save(path_dps_poto + ".png")

