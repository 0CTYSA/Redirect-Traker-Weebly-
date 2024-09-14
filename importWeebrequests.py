import requests
from bs4 import BeautifulSoup
import time
import sys


def obtener_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        titulo_pagina = soup.find('title').text if soup.find(
            'title') else "Sin título"

        boton = soup.find('a', class_='wsite-button')
        if boton:
            return boton['href']

        error_header = soup.find('h2', class_='header')
        error_message = soup.find('p', class_='error')
        if error_header and error_message:
            print(f"Error encontrado en '{
                  url} - {titulo_pagina}': {error_header.text} - {error_message.text}")
            return None

        print(f"No se encontró el botón en la página '{
              url} - {titulo_pagina}'. Verifica la página y el selector.")
        return None
    except requests.RequestException as e:
        print(f"Error al acceder a {url}: {e}")
        return None


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
    print("Introduce las URLs y escribe 'run' para comenzar el escaneo:")
    urls = []
    while True:
        entrada = input()
        if entrada.lower() == 'run':
            break
        urls.append(entrada)

    intervalos = {
        '1': 60 * 60,   # Cada hora
        '2': 30 * 60,   # Cada 30 minutos
        '3': 10 * 60,   # Cada 10 minutos
        '4': 5 * 60,    # Cada 5 minutos
        '5': 60         # Cada minuto
    }
    frecuencia = input(
        "Elige la frecuencia: '1' para cada hora, '2' para cada 30 minutos, etc.: ")
    errores_contados = 0

    while True:
        for url in urls:
            result_url = obtener_url(url)
            if result_url:
                guardar_url_nueva(result_url)
            else:
                errores_contados += 1

            time.sleep(5)  # Puedes ajustar esto para espaciar las solicitudes

        if errores_contados == len(urls):
            print("Todos los sitios han sido escaneados con errores o sin encontrar el botón. Finalizando el proceso.")
            break  # Salir del bucle y finalizar si todos resultaron en error

        time.sleep(intervalos[frecuencia])  # Usa el intervalo seleccionado


if __name__ == '__main__':
    main()
