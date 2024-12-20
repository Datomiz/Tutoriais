# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 21:00:28 2024

@author: user
"""

from PIL import Image
from tkinter import filedialog as fd
import pillow_avif
import os

local_path = os.path.abspath(os.getcwd())

path = fd.askopenfilename(
    title = "Select your image",
    initialdir = local_path,
    filetypes = (
        ("image files", ".webp"),
        ("image files", ".AVIF")
        )
    )

if path != "":
    
    Image_file = Image.open(path)
    
    path_after_dot = path[:path.find(".")]
    
    png = Image_file.convert("RGBA")
    
    png.save(path_after_dot + ".png")