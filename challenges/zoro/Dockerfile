# Usamos una imagen base de Ubuntu
FROM ubuntu:22.04

# Evitar interactividad en la instalación de paquetes
# ARG DEBIAN_FRONTEND=noninteractive

# Actualizar e instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    sudo \
    python3 \
    python3-pip \
    python3-dev \
    git \
    vim \
    nano \
    curl \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

# Crear un usuario "zoro" y darle una contraseña
RUN useradd -ms /bin/bash zoro && echo "zoro:FLAG_08d3164f15a022f7fb28617afb39a63a" | chpasswd && adduser zoro sudo

# Deshabilitamos el acceso directo como root para que los alumnos no inicien con permisos de administrador
RUN passwd -l root

# Establecer el directorio de trabajo
WORKDIR /home/zoro

# Copiar los archivos del reto dentro del contenedor
COPY ./ONEPIECE /home/zoro/ONEPIECE

# Cambiar la propiedad de los archivos al usuario zoro
RUN chown -R zoro:zoro /home/zoro

# Cambiar al usuario "zoro" por defecto
USER nobody

EXPOSE 8000 
# Script de inicio
CMD ["bash"]