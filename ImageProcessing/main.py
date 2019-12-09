# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import numpy as np

class Interface():
    def Captura(self):
        self.filename = askopenfilename()
        self.image = Image.open(self.filename)
        self.photo = ImageTk.PhotoImage(self.image)
        label = Label(self.root, image=self.photo).grid(row=1, column=0, padx=15, pady=5)    
     
    def Treinamento(self):
        pass
    
    def ClassificarImagens(self):
        pass
    
    def __init__(self):
        self.root = Tk()
        self.root.title('Classificador de Imagens')
        
        Button(self.root, text='Seleciona a Imagem', command=self.Captura).grid(row=0, column=0, pady=5)
        Button(self.root, text='Treinar', command=self.Treinamento).grid(row=0, column=1, pady=5)
        Button(self.root, text='Classificar', command=self.ClassificarImagens).grid(row=1, column=1, pady=5)
        
        self.root.mainloop()
        
Interface()