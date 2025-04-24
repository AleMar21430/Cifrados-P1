
from PIL import Image
import piexif
from luffy_xor import xor_cipher

def extraer_texto_metadata(imagen_path):
	# Abrir la imagen
	img = Image.open(imagen_path)
	
	# Obtener los metadatos EXIF
	exif_dict = piexif.load(img.info.get('exif', b''))
	
	# Obtener el texto almacenado en 'Artist' (o en el campo que elegimos)
	texto = exif_dict['0th'].get(piexif.ImageIFD.Artist)
	if texto:
		return texto.decode('utf-8')
	return None


# Uso del código para descifrar la imagen
# Ejemplo de uso
image_path = "challenges/luffy/poneglyph.jpeg"
student_id = "21430"
texto_cifrado = extraer_texto_metadata(image_path)
decrypted_text = xor_cipher(texto_cifrado, student_id)
print(decrypted_text)

image_path = "challenges/zoro/poneglyph.jpeg"
texto_cifrado = extraer_texto_metadata(image_path)
decrypted_text = xor_cipher(texto_cifrado, student_id)
print(decrypted_text)

image_path = "challenges/usopp/poneglyph.jpeg"
texto_cifrado = extraer_texto_metadata(image_path)
decrypted_text = xor_cipher(texto_cifrado, student_id)
print(decrypted_text)

image_path = "challenges/nami/poneglyph.jpeg"
texto_cifrado = extraer_texto_metadata(image_path)
decrypted_text = xor_cipher(texto_cifrado, student_id)
print(decrypted_text)