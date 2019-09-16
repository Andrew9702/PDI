import sys
import random
import math
import io
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import * 
from PIL import Image, ImageDraw, ImageFont, ImageStat
from pathlib import Path

class Filtros(QWidget):

	def __init__(self, parent = None):
		super(Filtros, self).__init__(parent)
		self.setWindowTitle("Editor de filtros")
		self.resize(700,500)
		self.imagen = None
		self.pixmap = None
		self.label1 = QLabel(self)
		self.label1.setGeometry(100,5,800,400)
		self.label1.move(100,25)
		self.labelmod = QLabel(self)
		self.labelmod.setGeometry(100,5,800,400)
		self.menu = QMenu()

		self.byns = QPushButton("Seleccionar un filtro", self)
		self.opn = QPushButton("abrir imagen", self)
		self.opn.move(100,425)
		self.opn.clicked.connect(self.obtener_imagen)

		self.cal = QPushButton("Construir album", self)
		self.cal.move(100,460)
		self.cal.clicked.connect(self.construir)

		self.brillo = QSlider(Qt.Horizontal, self)
		self.brillo.setMinimum(-128)
		self.brillo.setMaximum(128)
		self.brillo.setValue(0)
		self.brillo.setTickPosition(QSlider.TicksBelow)
		self.brillo.setTickInterval(5)
		self.brillo.move(300,450)
		self.brillo.valueChanged.connect(self.brillof)

		self.conjunto_imagenes = []
		self.colores = []

		self.ruta_imagen = None

		self.menu.addAction("filtro verde", self.filtro_verde)
		self.menu.addAction("filtro azul", self.filtro_azul)
		self.menu.addAction("filtro rojo", self.filtro_rojo)
		self.menu.addAction("mosaico", self.mosaico)
		self.menu.addAction("blur", self.blury)
		self.menu.addAction("motion blur", self.m_blury)
		self.menu.addAction("find edges", self.edges)
		self.menu.addAction("sharpen", self.sharp)
		self.menu.addAction("emboss", self.emboss)
		self.menu.addAction("mean_median filter", self.media_f)
		self.menu.addAction("arroba color", self.m_color)
		self.menu.addAction("arroba byn", self.m_byn)
		self.menu.addAction("letras", self.letrar)
		self.menu.addAction("naipes", self.m_naipes)
		self.menu.addAction("domino", self.m_domino)
		self.menu.addAction("quitar marca de agua", self.marca_agua)
		self.menu.addAction("metodo 1", self.sucio_rapido)
		self.menu.addAction("metodo 2", self.luma)
		self.menu.addAction("metodo 3", self.desaturacion)
		self.menu.addAction("metodo 4 max", self.descomponer_max)
		self.menu.addAction("metodo 4 min", self.descomponer_min)
		self.menu.addAction("metodo 5 red", self.solo_colorR)
		self.menu.addAction("metodo 5 green", self.solo_colorG)
		self.menu.addAction("metodo 5 blue", self.solo_colorB)
		self.menu.addAction("metodo 6", self.sombras)
		self.menu.addAction("semitonos", self.semitonos)
		self.menu.addAction("luz negra", self.luz_negra)
		self.menu.addAction("arte rubik", self.arte_raux)
		self.menu.addAction("Dithering", self.dithering)
		self.menu.addAction("Fotomosaicos", self.fotomosaico)
		self.byns.setMenu(self.menu)

		self.byns.move(300,425)

	def obtener_imagen(self):
		archivo = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg *.png)")
		self.imagen = QImage(archivo)
		self.pixmap = QPixmap.fromImage(self.imagen)
		self.pixmap = self.pixmap.scaledToHeight(500)
		self.label1.setPixmap(self.pixmap)

	def filtro_verde(self):
		if(self.imagen != None):
			copia = self.imagen.copy()
			for i in range(copia.size().width()):
				for j in range(copia.size().height()):
					color_actual = QColor(copia.pixel(i,j))
					color_actual.setBlue(0)
					color_actual.setRed(0)
					copia.setPixel(i, j, color_actual.rgb())
			self.pixmap = QPixmap.fromImage(copia)
			self.pixmap = self.pixmap.scaledToHeight(500)
			self.label1.setPixmap(self.pixmap)

	def filtro_azul(self):
		if(self.imagen != None):
			copia = self.imagen.copy()
			for i in range(copia.size().width()):
				for j in range(copia.size().height()):
					color_actual = QColor(copia.pixel(i,j))
					color_actual.setGreen(0)
					color_actual.setRed(0)
					copia.setPixel(i, j, color_actual.rgb())
			self.pixmap = QPixmap.fromImage(copia)
			self.pixmap = self.pixmap.scaledToHeight(500)
			self.label1.setPixmap(self.pixmap)

	def filtro_rojo(self):
		if(self.imagen != None):
			copia = self.imagen.copy()
			for i in range(copia.size().width()):
				for j in range(copia.size().height()):
					color_actual = QColor(copia.pixel(i,j))
					color_actual.setGreen(0)
					color_actual.setBlue(0)
					copia.setPixel(i, j, color_actual.rgb())
			self.pixmap = QPixmap.fromImage(copia)
			self.pixmap = self.pixmap.scaledToHeight(500)
			self.label1.setPixmap(self.pixmap)

	def sucio_rapido(self):
		if(self.imagen != None):
			copia = self.imagen.copy()
			for i in range(copia.size().width()):
				for j in range(copia.size().height()):
					color_actual = QColor(copia.pixel(i,j))

					gris = (color_actual.red() + color_actual.green() + color_actual.blue()) / 3

					copia.setPixel(i, j, QColor(gris,gris,gris).rgb())
			self.pixmap = QPixmap.fromImage(copia)
			self.pixmap = self.pixmap.scaledToHeight(500)
			self.label1.setPixmap(self.pixmap)

	def luma(self, imagen):
		if(self.imagen != None):
			copia = self.imagen.copy()
			for i in range(copia.size().width()):
				for j in range(copia.size().height()):
					color_actual = QColor(copia.pixel(i,j))

					gris = (color_actual.red() * 0.299 + color_actual.green() * 0.587 + color_actual.blue() * 0.114)

					copia.setPixel(i, j, QColor(gris,gris,gris).rgb())
			self.pixmap = QPixmap.fromImage(copia)
			self.pixmap = self.pixmap.scaledToHeight(500)
			self.label1.setPixmap(self.pixmap)
			return copia

	def desaturacion(self):
		if(self.imagen != None):
			copia = self.imagen.copy()
			for i in range(copia.size().width()):
				for j in range(copia.size().height()):
					color_actual = QColor(copia.pixel(i,j))

					gris = (max(color_actual.red(), color_actual.green(), color_actual.blue()) + min(color_actual.red(), color_actual.green(), color_actual.blue())) / 2

					copia.setPixel(i, j, QColor(gris,gris,gris).rgb())
			self.pixmap = QPixmap.fromImage(copia)
			self.pixmap = self.pixmap.scaledToHeight(500)
			self.label1.setPixmap(self.pixmap)

	def descomponer_max(self):
		if(self.imagen != None):
			copia = self.imagen.copy()
			for i in range(copia.size().width()):
				for j in range(copia.size().height()):
					color_actual = QColor(copia.pixel(i,j))

					gris = max(color_actual.red(), color_actual.green(), color_actual.blue())

					copia.setPixel(i, j, QColor(gris,gris,gris).rgb())
			self.labelmod.setPixmap(QPixmap.fromImage(copia))

	def descomponer_min(self):
		if(self.imagen != None):
			copia = self.imagen.copy()
			for i in range(copia.size().width()):
				for j in range(copia.size().height()):
					color_actual = QColor(copia.pixel(i,j))

					gris = min(color_actual.red(), color_actual.green(), color_actual.blue())

					copia.setPixel(i, j, QColor(gris,gris,gris).rgb())
			self.labelmod.setPixmap(QPixmap.fromImage(copia))

	def solo_colorR(self):
		if(self.imagen != None):
			copia = self.imagen.copy()
			for i in range(copia.size().width()):
				for j in range(copia.size().height()):
					color_actual = QColor(copia.pixel(i,j))

					gris = color_actual.red()

					copia.setPixel(i, j, QColor(gris,gris,gris).rgb())
			self.labelmod.setPixmap(QPixmap.fromImage(copia))
			return copia

	def solo_colorG(self):
		if(self.imagen != None):
			copia = self.imagen.copy()
			for i in range(copia.size().width()):
				for j in range(copia.size().height()):
					color_actual = QColor(copia.pixel(i,j))

					gris = color_actual.green()

					copia.setPixel(i, j, QColor(gris,gris,gris).rgb())
			self.labelmod.setPixmap(QPixmap.fromImage(copia))

	def solo_colorB(self):
		if(self.imagen != None):
			copia = self.imagen.copy()
			for i in range(copia.size().width()):
				for j in range(copia.size().height()):
					color_actual = QColor(copia.pixel(i,j))

					gris = color_actual.blue()

					copia.setPixel(i, j, QColor(gris,gris,gris).rgb())
			self.labelmod.setPixmap(QPixmap.fromImage(copia))

	def sombras(self):
		sombras = random.randint(2, 256)
		factor_conversion = 255 / (sombras - 1)
		if(self.imagen != None):
			copia = self.imagen.copy()
			for i in range(copia.size().width()):
				for j in range(copia.size().height()):
					color_actual = QColor(copia.pixel(i,j))
					valor_medio = (color_actual.red() + color_actual.green() + color_actual.blue()) / 3
					gris = int((valor_medio / factor_conversion) + 0.5) * factor_conversion
					copia.setPixel(i, j, QColor(gris,gris,gris).rgb())
			self.labelmod.setPixmap(QPixmap.fromImage(copia))

	def brillof(self):
		cantidad = self.brillo.value()
		self.brillo_aux(cantidad)

	def brillo_aux(self, cantidad):
		if(self.imagen != None):
			copia = self.imagen.copy()
			brillo = cantidad
			for i in range(copia.size().width()):
				for j in range(copia.size().height()):
					color_actual = QColor(copia.pixel(i,j))
					r = color_actual.red() + brillo
					g = color_actual.green() + brillo
					b = color_actual.blue() + brillo
					r = min(max(r, 0), 255)
					g = min(max(g, 0), 255)
					b = min(max(b, 0), 255)
					copia.setPixel(i,j, QColor(r,g,b).rgb())
		self.labelmod.setPixmap(QPixmap.fromImage(copia))
		return copia

	def mosaico(self):
		self.mosaux(9, self.imagen)

	def mosaux(self,n, imagen):
		for k in range(imagen.size().width()):
			for l in range(imagen.size().height()):						
				promedio_r = 0
				promedio_g = 0
				promedio_b = 0
				if k % n == 0 and l % n == 0 and k != 0 and l != 0:
					for i in range(k - n, k):
						for j in range(l - n, l):
							color_actual = QColor(imagen.pixel(i,j))						
							r = color_actual.red()
							g = color_actual.green()
							b = color_actual.blue()
							promedio_r += int(r)
							promedio_g += int(g)
							promedio_b += int(b)
									
					for i in range(k-n, k):
						for j in range(l-n, l):
							imagen.setPixel(i,j, QColor(promedio_r//(n*n),promedio_g//(n*n),promedio_b//(n*n)).rgb())
		self.pixmap = QPixmap.fromImage(imagen)
		self.pixmap = self.pixmap.scaledToHeight(500)
		self.label1.setPixmap(self.pixmap)
		return imagen

	def convolucion(self, imagen, matriz, factor, bias):
		anchura = imagen.size().width()
		altura = imagen.size().height()
		tamanio = QSize(anchura, altura)
		copia = QImage(tamanio,QImage.Format_ARGB32)
		for i in range(anchura - len(matriz)+1):
			for j in range(altura - len(matriz)+1):
				rojo = 0.0
				verde = 0.0
				azul = 0.0
				for x in range(len(matriz)):
					for y in range(len(matriz)):

						indX = (i - len(matriz) / 2 + x + anchura) % anchura
						indY = (j - len(matriz) / 2 + y + altura) % altura

						color_actual = QColor(imagen.pixel(indX,indY))

						rojo += color_actual.red() * matriz[x][y]
						verde += color_actual.green() * matriz[x][y]
						azul += color_actual.blue() * matriz[x][y]

				rojo = min(max((factor*rojo +bias), 0), 255)
				verde = min(max((factor*verde +bias), 0), 255)
				azul = min(max((factor*azul +bias), 0), 255)
				copia.setPixel(int(i + len(matriz)/2), int(j +len(matriz)/ 2), QColor(rojo, verde, azul).rgb())
		return copia

	def blury(self):
		if(self.imagen != None):
			copia = self.imagen.copy()
			matriz = [[0.0,0.2,0.0],[0.2,0.2,0.2],[0.0,0.2,0.0]]
			resultado = self.convolucion(copia, matriz, 1.0, 0.0)
		self.labelmod.setPixmap(QPixmap.fromImage(resultado))

	def m_blury(self):
		if(self.imagen != None):
			copia = self.imagen.copy()
			matriz = [[1,0,0,0,0,0,0,0,0], [0,1,0,0,0,0,0,0,0], [0,0,1,0,0,0,0,0,0], [0,0,0,1,0,0,0,0,0], [0,0,0,0,1,0,0,0,0], [0,0,0,0,0,1,0,0,0], [0,0,0,0,0,0,1,0,0], [0,0,0,0,0,0,0,1,0], [0,0,0,0,0,0,0,0,1]]
			resultado = self.convolucion(copia, matriz, 1.0 / 9.0, 0.0)
		self.labelmod.setPixmap(QPixmap.fromImage(resultado))

	def edges(self):
		if(self.imagen != None):
			copia = self.imagen.copy()
			matriz = [[0,0,-1,0,0], [0,0,-1,0,0], [0,0,2,0,0], [0,0,0,0,0], [0,0,0,0,0]]
			resultado = self.convolucion(copia, matriz, 1.0, 0.0)
		self.labelmod.setPixmap(QPixmap.fromImage(resultado))

	def sharp(self):
		if(self.imagen != None):
			copia = self.imagen.copy()
			matriz = [[-1,-1,-1], [-1,9,-1], [-1,-1,-1]]
			resultado = self.convolucion(copia, matriz, 1.0, 0.0)
		self.labelmod.setPixmap(QPixmap.fromImage(resultado))		

	def emboss(self):
		if(self.imagen != None):
			copia = self.imagen.copy()
			matriz = [[-1,-1,0], [-1,0,1], [0,1,1]]
			resultado = self.convolucion(copia, matriz, 1.0, 128.0)
		self.labelmod.setPixmap(QPixmap.fromImage(resultado))		

	def media_f(self):
		if(self.imagen != None):
			copia = self.imagen.copy()
			matriz = [[1,1,1], [1,1,1], [1,1,1]]
			resultado = self.convolucion(copia, matriz, 1.0/9.0, 0.0)
		self.labelmod.setPixmap(QPixmap.fromImage(resultado))

	def letras(self, foto, fuente):
		anchura = foto.size().width()
		altura = foto.size().height()
		imagen = Image.new("RGB", (anchura,altura), (255,255,255))
		dibujo = ImageDraw.Draw(imagen)
		for i in range(0, anchura, 8):
			for j in range(0, altura, 8):
				color_actual = QColor(foto.pixel(i,j))
				dibujo.text((i,j), "@", (color_actual.red(), color_actual.green(), color_actual.blue()), font = fuente)
		imagen.save('letras_imagen.png')
		return imagen

	def m_color(self):
		if(self.imagen != None):
			copia = self.imagen.copy()
			fuente = ImageFont.truetype("DancingScript-Bold.ttf", 10)
			imagen = self.letras(copia, fuente)
			imagen.show()

	def m_byn(self):
		if(self.imagen != None):
			copia = self.luma(self.imagen.copy())
			fuente = ImageFont.truetype("DancingScript-Bold.ttf", 10)
			imagen = self.letras(copia, fuente)
			imagen.show()

	def m_naipes(self):
		if(self.imagen != None):
			copia = self.imagen.copy()
			fuente = ImageFont.truetype("PLAYCRDS.TTF", 10)
			imagen = self.letras(copia, fuente)
			imagen.show()

	def m_domino(self):
		if(self.imagen != None):
			copia = self.imagen.copy()
			fuente = ImageFont.truetype("Lasvwd__.ttf", 10)
			imagen = self.letras(copia, fuente)
			imagen.show()

	def letrar(self):
		if(self.imagen != None):
			copia = self.luma(self.imagen.copy())
			anchura = copia.size().width()
			altura = copia.size().height()
			imagen = Image.new("RGB", (anchura,altura), (255,255,255))
			dibujo = ImageDraw.Draw(imagen)
			fuente = ImageFont.truetype("DancingScript-Bold.ttf", 10)
			for i in range(0, anchura, 7):
				for j in range(0, altura, 7):
					color_actual = QColor(copia.pixel(i,j))
					if color_actual.red() >= 240:
						dibujo.text((i,j), "_", (color_actual.red(), color_actual.green(), color_actual.blue()), font = fuente)
					elif color_actual.red() >= 226:
						dibujo.text((i,j), ".", (color_actual.red(), color_actual.green(), color_actual.blue()), font = fuente)
					elif color_actual.red() >= 210:
						dibujo.text((i,j), "+", (color_actual.red(), color_actual.green(), color_actual.blue()), font = fuente)
					elif color_actual.red() >= 192:
						dibujo.text((i,j), "%", (color_actual.red(), color_actual.green(), color_actual.blue()), font = fuente)
					elif color_actual.red() >= 176:
						dibujo.text((i,j), "$", (color_actual.red(), color_actual.green(), color_actual.blue()), font = fuente)
					elif color_actual.red() >= 160:
						dibujo.text((i,j), "2", (color_actual.red(), color_actual.green(), color_actual.blue()), font = fuente)
					elif color_actual.red() >= 144:
						dibujo.text((i,j), "Y", (color_actual.red(), color_actual.green(), color_actual.blue()), font = fuente)
					elif color_actual.red() >= 128:
						dibujo.text((i,j), "0", (color_actual.red(), color_actual.green(), color_actual.blue()), font = fuente)
					elif color_actual.red() >= 112:
						dibujo.text((i,j), "D", (color_actual.red(), color_actual.green(), color_actual.blue()), font = fuente)
					elif color_actual.red() >= 96:
						dibujo.text((i,j), "A", (color_actual.red(), color_actual.green(), color_actual.blue()), font = fuente)
					elif color_actual.red() >= 80:
						dibujo.text((i,j), "U", (color_actual.red(), color_actual.green(), color_actual.blue()), font = fuente)
					elif color_actual.red() >= 64:
						dibujo.text((i,j), "Q", (color_actual.red(), color_actual.green(), color_actual.blue()), font = fuente)
					elif color_actual.red() >= 48:
						dibujo.text((i,j), "#", (color_actual.red(), color_actual.green(), color_actual.blue()), font = fuente)
					elif color_actual.red() >= 32:
						dibujo.text((i,j), "H", (color_actual.red(), color_actual.green(), color_actual.blue()), font = fuente)
					elif color_actual.red() >= 16:
						dibujo.text((i,j), "N", (color_actual.red(), color_actual.green(), color_actual.blue()), font = fuente)
					elif color_actual.red() >= 0:
						dibujo.text((i,j), "M", (color_actual.red(), color_actual.green(), color_actual.blue()), font = fuente)
			imagen.save('letras_imagen.png')
			imagen.show()

	def marca_agua(self):
		r,g,b = 0,0,0
		rg,gg,bg = 0,0,0
		rb,gb,bb = 0,0,0
		if(self.imagen != None):
			copia = self.imagen.copy()
			anchura = copia.size().width()
			altura = copia.size().height()
			imagen_revelada = self.ver_marca(copia)
			gris_rojos = self.solo_colorR()
			brillo_alto = self.brillo_aux(-3)
			tamanio = QSize(anchura, altura)
			nueva = QImage(tamanio,QImage.Format_ARGB32)
			for i in range (anchura):
				for j in range (altura):
					color_actual = QColor(imagen_revelada.pixel(i,j))
					r = color_actual.red()
					g = color_actual.green()
					b = color_actual.blue()
					if(r<11 and b <11 and g<11):
						nueva.setPixel(i, j, QColor(copia.pixel(i,j)).rgb())
					else:
						rg = QColor(gris_rojos.pixel(i,j)).red()
						gg = QColor(gris_rojos.pixel(i,j)).green()
						bg = QColor(gris_rojos.pixel(i,j)).blue()
						rb = QColor(brillo_alto.pixel(i,j)).red()
						gb = QColor(brillo_alto.pixel(i,j)).green()
						bb = QColor(brillo_alto.pixel(i,j)).blue()
						if((rg < rb) and (gg < gb) and (bg < bb)):
							nueva.setPixel(i, j, QColor(brillo_alto.pixel(i, j)).rgb())
						else:
							nueva.setPixel(i, j, QColor(gris_rojos.pixel(i, j)).rgb())
		self.labelmod.setPixmap(QPixmap.fromImage(nueva))

			
	def ver_marca(self, imagen):
		r,g,b = 0,0,0
		anchura = imagen.size().width()
		altura = imagen.size().height()
		tamanio = QSize(anchura, altura)
		copia = QImage(tamanio,QImage.Format_ARGB32)
		for i in range (anchura):
			for j in range (altura):
				color_actual = QColor(imagen.pixel(i,j))
				r = 0
				g = abs(color_actual.green() - color_actual.red())
				b = abs(color_actual.blue() - color_actual.red())
				copia.setPixel(i, j, QColor(r,g, b).rgb())
		return copia

	def semitonos(self):
		if(self.imagen != None):
			blanegro = self.luma(self.imagen)
			anchura = self.imagen.size().width()
			altura = self.imagen.size().height()
			tamanio = QSize(anchura, altura)
			copia = QImage(tamanio,QImage.Format_ARGB32)
			for i in range (1,anchura-1):
				for j in range (altura-1):
					color_actual = QColor(blanegro.pixel(i,j))
					pr,pg,pb = color_actual.red(), color_actual.green(), color_actual.blue()
					nuevoR = round(pr/255) * 255
					nuevoG = round(pg/255) * 255
					nuevoB = round(pb/255) * 255
					copia.setPixel(i, j, QColor(nuevoR,nuevoG,nuevoB).rgb())

					errorR = pr - nuevoR
					errorG = pg - nuevoG
					errorB = pb - nuevoB

					color_actual_2 = QColor(blanegro.pixel(i+1,j))
					r,g,b = color_actual_2.red(), color_actual_2.green(), color_actual_2.blue()
					r,g,b = r + errorR * 7/16.0, g + errorG * 7/16.0, b + errorB * 7/16.0
					if(r > 255 or g > 255 or b > 255):
						r, g, b = min(r,255), min(g,255), min(b,255)
					copia.setPixel(i+1, j, QColor(r,g,b).rgb())

					color_actual_3 = QColor(blanegro.pixel(i-1,j+1))
					r,g,b = color_actual_3.red(), color_actual_3.green(), color_actual_3.blue()
					r,g,b = r + errorR * 3/16.0, g + errorG * 3/16.0, b + errorB * 3/16.0
					if(r > 255 or g > 255 or b > 255):
						r, g, b = min(r,255), min(g,255), min(b,255)
					copia.setPixel(i-1, j+1, QColor(r,g,b).rgb())

					color_actual_4 = QColor(blanegro.pixel(i,j+1))
					r,g,b = color_actual_4.red(), color_actual_4.green(), color_actual_4.blue()
					r,g,b = r + errorR * 5/16.0, g + errorG * 5/16.0, b + errorB * 5/16.0
					if(r > 255 or g > 255 or b > 255):
						r, g, b = min(r,255), min(g,255), min(b,255)
					copia.setPixel(i, j+1, QColor(r,g,b).rgb())

					color_actual_5 = QColor(blanegro.pixel(i+1,j+1))
					r,g,b = color_actual_5.red(), color_actual_5.green(), color_actual_5.blue()
					r,g,b = r + errorR * 1/16.0, g + errorG * 1/16.0, b + errorB * 1/16.0
					if(r > 255 or g > 255 or b > 255):
						r, g, b = min(r,255), min(g,255), min(b,255)
					copia.setPixel(i+1, j+1, QColor(r,g,b).rgb())
		self.labelmod.setPixmap(QPixmap.fromImage(copia))

	def luz_negra(self):
		r,g,b,ln,rc,gc,bc = 0,0,0,0,0,0,0
		if(self.imagen != None):
			anchura = self.imagen.size().width()
			altura = self.imagen.size().height()
			tamanio = QSize(anchura, altura)
			copia = QImage(tamanio,QImage.Format_ARGB32)
			for i in range(anchura):
				for j in range(altura):
					color_actual = QColor(self.imagen.pixel(i,j))
					rc = color_actual.red()
					gc = color_actual.green()
					bc = color_actual.blue()
					ln = (rc+gc+bc)/3

					r = abs(rc-ln)*2
					g = abs(gc-ln)*2
					b = abs(bc-ln)+2

					r = min(max(r,0),255)
					g = min(max(g,0),255)
					b = min(max(b,0),255)

					copia.setPixel(i, j, QColor(r,g,b).rgb())
		self.pixmap = QPixmap.fromImage(copia)
		self.pixmap = self.pixmap.scaledToHeight(500)
		self.label1.setPixmap(self.pixmap)

	def arte_raux(self):
		if(self.imagen != None):
			negros = self.luma(self.imagen)
			mosai = self.mosaux(5, negros)
			anchura = self.imagen.size().width()
			altura = self.imagen.size().height()
			tamanio = QSize(anchura, altura)
			copia = QImage(tamanio,QImage.Format_ARGB32)
			for i in range(anchura):
				for j in range(altura):
					color_actual = QColor(mosai.pixel(i,j))
					r = color_actual.red()
					g = color_actual.green()
					b = color_actual.blue()
					if(r >= 200):
						copia.setPixel(i, j, QColor(255,255,255).rgb())
					if(r >= 150 and r < 200):
						copia.setPixel(i, j, QColor(255,255,0).rgb())
					if(r >= 100 and r < 150):
						copia.setPixel(i, j, QColor(255,165,0).rgb())
					if(r >= 70 and r < 100):
						copia.setPixel(i, j, QColor(255,0,0).rgb())
					if(r >= 40 and r < 70):
						copia.setPixel(i, j, QColor(0,180,0).rgb())
					if(r >= 0 and r < 40):
						copia.setPixel(i, j, QColor(0,0,180).rgb())
			self.pixmap = QPixmap.fromImage(copia)
			self.pixmap = self.pixmap.scaledToHeight(500)
			self.label1.setPixmap(self.pixmap)

	def dithering(self):
		if(self.imagen != None):
			negros = self.luma(self.imagen)
			anchura = self.imagen.size().width()
			altura = self.imagen.size().height()
			tamanio = QSize(anchura, altura)
			copia = QImage(tamanio,QImage.Format_ARGB32)
			error = 0
			for i in range(anchura):
				error = 0
				for j in range(altura):
					color_actual = QColor(negros.pixel(i,j))
					gris_c = self.verificacion(int(color_actual.red()/100 * 255 + error))
					if(gris_c == 255 or gris_c == 0):
						copia.setPixel(i,j, QColor(gris_c, gris_c, gris_c).rgb())
						error = 0
					elif(gris_c < 127):
						copia.setPixel(i,j, QColor(0, 0, 0).rgb())
						error += gris_c
					else:
						copia.setPixel(i,j, QColor(255, 255, 255).rgb())
						error = gris_c - 255
			self.pixmap = QPixmap.fromImage(copia)
			self.pixmap = self.pixmap.scaledToHeight(500)
			self.label1.setPixmap(self.pixmap)

	#Metodo que realiza el fotomosaico de la imagen seleccionada.
	def fotomosaico(self):
		if(self.imagen != None):

			#Cargamos el archivo de texto con su ruta
			self.ruta_imagen = QFileDialog.getOpenFileName(self, 'Open File', '~/', 'txt(*.txt)')

			#Obtenemos los datos de la imagen
			anchura = self.imagen.size().width()
			altura = self.imagen.size().height()

			#Construimos una nueva imagen en la cual quedara el resultado del filtro
			copia = Image.new("RGB", (anchura,altura), (255,255,255))

			#Aplicamos el filtro mosaico, lo cual ayudara a simplificar el proceso de construir la imagen
			mosai = self.mosaux(8, self.imagen)

			#Revisamos que no esten vacios los conjuntos.
			if(len(self.conjunto_imagenes) == 0 and len(self.colores) == 0):
				self.cargar_imagenes(8,8)

			#Se recorre cada region del mosaico
			for i in range(0,anchura,8):
				for j in range(0,altura,8):
					#Se calcula que imagen tiene mas presente el color de la region actual
					imagen = self.diferencia_colores(mosai.pixel(i,j))

					#Se asigna la mejor imagen a la region de la imagen del mosaico
					copia.paste(self.conjunto_imagenes[imagen], (i,j))

			#Finalmente se guarda la imagen y se muestra					
			copia.save('fotomosaico_construido.png')
			copia.show()

	#Metodo que construye los dos conjuntos que nos serviran para construir la imagen
	def cargar_imagenes(self, i, j):
		if(self.ruta_imagen != None):
			archivo_paquete = open(str(self.ruta_imagen), "r")
			tamanio = i, j
			for linea in archivo_paquete:
				#Separamos los componentes del archivo en un arreglo
				#Estos son r, g, b, ruta de la imagen
				componentes = linea.split("/")
				#Agregamos la tripleta de colores al conjunto colores
				self.colores.append((int(componentes[0]), int(componentes[1]), int(componentes[2])))

				#Unimos los componentes restantes, pues es la direccion de la imagen
				path = self.arma_direccion(componentes[3:])

				#Abrimos la imagen ya asignamos una miniatura
				extraida = Image.open(path)
				extraida.thumbnail(tamanio, Image.ANTIALIAS)

				#Agregamos la ruta de la imagen al conjunto de imagenes
				self.conjunto_imagenes.append(extraida)

			#Cerramos el archivo de texto
			archivo_paquete.close()
		else:
			print("Ocurrio un error, no existe el archivo")

	#Calcula que imagen tiene el promedio mas parecido a una region de la imagen que se va a construir.
	def diferencia_colores(self,pixel):
		diff = []

		#Obtenemos el color de la region actual
		color_actual = QColor(pixel)

		#La separamos en sus componentes
		r, g, b = color_actual.red(), color_actual.green(), color_actual.blue()

		#Calculamos la diferencia en color de cada imagen y la region actual
		for color in self.colores:
			d = math.sqrt((r - color[0])**2 + (g-color[1])**2 + (b-color[2])**2)
			diff.append(d)

		#El minimo en la diferencia de colores, sera la imagen asociada a esa region
		cercano = min(diff)
		ind = diff.index(cercano)
		return ind

	#Metodo encargado de construir un archivo de texto con los rgb predominantes en la imagen
	#Ademas de la ruta de la imagen.
	def construir(self):
		try:
			#El archivo de texto resultante se llamara resultado.txt
			resultado = open("resultado.txt", "w+")
			file = str(QFileDialog.getExistingDirectory(self, "Selecciona el directorio de imagenes"))
			# Recorremos el directorio con las imagenes
			for root, dirs, files in os.walk(file):
				for directorio in dirs:
					#Abrimos la imagen para trabajar con ella
					imagen_actual = Image.open(os.path.abspath(os.path.join(root, directorio)))
			# Recorremos el directorio con las imagenes
			for archivo in files:
				imagen_actual = Image.open(os.path.abspath(os.path.join(root, archivo)))
				#Usamos la funcion stat para obtener los componentes rgb promedio de la imagen
				color_p = tuple(ImageStat.Stat(imagen_actual).median)
				#Escribimos en el archivo de texto los colores y la ruta a la imagen
				resultado.write(str(color_p[0]) + "/" + str(color_p[1]) + "/"  + str(color_p[2]) + "/" + os.path.abspath(os.path.join(root, archivo)) + "\n")
		
			#Finalmente cerramos el archivo y mandamos un anuncio de que se termino
			resultado.close()
			print("Archivo construido.\nAhora por favor selecciona una imagen y luego el filtro fotomosaico\nY selecciona el archivo de texto: resultado.txt")
		except IOError:
			print("No se ha podido leer el archivo, asegurese de que sea una carpeta de imagenes.")

	def verificacion(self, x):
		if(x > 255):
			return 255
		elif(x<0):
			return 0
		return x

	#Metodo que une los componentes de texto
	def arma_direccion(self,componentes):	
		direx = ""
		for componente in componentes:
			direx += componente + "/"
		return direx[:-2]

aplicacion = QApplication(sys.argv)
filtros = Filtros()
filtros.show()
aplicacion.exec_()
