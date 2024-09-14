import requests
from bs4 import BeautifulSoup
import time
import sys  # Importar sys para terminar el script


def obtener_url():
    url = 'https://culphiliv.weebly.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extraer el título de la página para usarlo en mensajes de error
    titulo_pagina = soup.find('title').text if soup.find(
        'title') else "Sin título"

    # Buscar el botón específico
    boton = soup.find('a', class_='wsite-button')
    if boton:
        return boton['href']

    # Si no se encuentra el botón, buscar elementos que puedan indicar un error
    error_header = soup.find('h2', class_='header')
    error_message = soup.find('p', class_='error')
    if error_header and error_message:
        # Mostrar los mensajes de error encontrados y terminar el script
        print(f"Error encontrado: {error_header.text} - {error_message.text}")
        sys.exit(1)  # Terminar el script con un código de error

    # Si no hay errores claros, simplemente notificar que el botón no se encontró
    print(f"No se encontró el botón en la página '{
          titulo_pagina}'. Verifica la página y el selector.")
    sys.exit(1)  # Terminar el script con un código de error


def guardar_url_nueva(url):
    try:
        with open('urls.txt', 'r+') as file:
            urls_existentes = file.read().splitlines()
            if url not in urls_existentes:
                file.write(url + '\n')
    except FileNotFoundError:
        with open('urls.txt', 'w') as file:
            file.write(url + '\n')


def main():
    intervalos = {
        '1': 60 * 60,   # Cada hora
        '2': 30 * 60,   # Cada 30 minutos
        '3': 10 * 60,   # Cada 10 minutos
        '4': 5 * 60,    # Cada 5 minutos
        '5': 60         # Cada minuto
    }
    frecuencia = '5'  # Elige aquí la frecuencia.

    while True:
        url = obtener_url()
        if url:
            guardar_url_nueva(url)
        time.sleep(intervalos[frecuencia])  # Usa el intervalo seleccionado


if __name__ == '__main__':
    main()
