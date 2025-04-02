def xor_cipher(text, key):
	# Convertir tanto el texto como la clave a bytes
	if type(text) == str:
		text_bytes = text.encode()
	else:
		text_bytes = text
	key_bytes = key.encode()  # Convertir la clave a bytes

	# Cifrar con XOR
	cipher_text = bytes([text_bytes[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(text_bytes))])
	
	return cipher_text

print(xor_cipher(bytes.fromhex("747d75746f0209500001040552020553010601560557560108040003525650020d52060150"), "21430").decode())