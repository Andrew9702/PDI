from PIL import Image

#La ruta hacia la imagen.
ruta = "tango.png"

#Obtenemos la imagen em um objeto imagen
imagen = Image.open(ruta)

#Metodo que regresara la imagen con filtro en blanco y negro
def escala_grises(imagen):
	largo, ancho = imagen.size

	#Creamos la imagen a la que se le aplicara el filtro
	byn = Image.new("RGB", (largo,ancho), "white")

	for i in range(0, largo):
		for j in range(0, ancho):

			pix = imagen.getpixel((i,j))
			r = pix[0]
			g = pix[1]
			b = pix[2]

			gray = (r + g + b)/3
			byn.putpixel((i,j), (gray,gray,gray))
	
	return byn

#Metodo que regresara la imagen con filtro en rojo
def filtro_rojo(imagen):
	largo, ancho = imagen.size

	imrojo = Image.new("RGB", (largo,ancho), "white")

	for i in range(0, largo):
		for j in range(0, ancho):

			pix = imagen.getpixel((i,j))

			red = pix[0]

			imrojo.putpixel((i,j), (red,0,0))

	return imrojo

#Metodo que regresara la imagen con filtro en verde
def filtro_verde(imagen):
	largo, ancho = imagen.size

	imverd = Image.new("RGB", (largo,ancho), "white")

	for i in range(0, largo):
		for j in range(0, ancho):

			pix = imagen.getpixel((i,j))

			green = pix[1]

			imverd.putpixel((i,j), (0,green,0))

	return imverd

#Metodo que regresara la imagen con filtro en azul
def filtro_azul(imagen):
	largo, ancho = imagen.size

	imazul = Image.new("RGB", (largo,ancho), "white")

	for i in range(0, largo):
		for j in range(0, ancho):

			pix = imagen.getpixel((i,j))

			blue = pix[2]

			imazul.putpixel((i,j), (0,0,blue))

	return imazul

#Metodo que regresara la imagen con mas brillo
def brillo(imagen):
	largo, ancho = imagen.size
	imbri = Image.new("RGB", (largo,ancho), "white")

	for i in range(0, largo):
		for j in range(0, ancho):
			
			pix = imagen.getpixel((i,j))
			r = pix[0]
			g = pix[1]
			b = pix[2]

			total = r +g +b

			imbri.putpixel((i,j), (r*total / 255 , g*total / 255, b*total / 255))

	return imbri

def mosaico(imagen):
	largo, ancho = imagen.size
	imo = Image.new("RGB", (largo,ancho), "white")

	for i in range(0, largo):
		for j in range(0, ancho-1):
			
			pix = imagen.getpixel((i,j))
			r = pix[0]
			g = pix[1]
			b = pix[2]

			imo.putpixel((2*i, j+1),(r,0,0))

	return imo

x = filtro_azul(imagen)
x.show()
