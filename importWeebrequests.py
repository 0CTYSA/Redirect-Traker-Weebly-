import requests
from bs4 import BeautifulSoup
import time
import sys


def obtener_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        titulo_pagina = soup.find('title').text if soup.find(
            'title') else "Untitled"

        boton = soup.find('a', class_='wsite-button')
        if boton:
            return boton['href']

        error_header = soup.find('h2', class_='header')
        error_message = soup.find('p', class_='error')
        if error_header and error_message:
            print(f"2. Error found in '{url}'\nContent: {
                  error_header.text} - {error_message.text}\n")
            return None

        print(f"1. Button not found on page '{url}'\nTitle of the page: <{
              titulo_pagina}>\nNota: Verify the page and the selector.\n")
        return None
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")
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
    print("Enter URLs and type 'run' to start scanning:")
    urls = []
    while True:
        entrada = input()
        if entrada.lower() == 'run':
            break
        urls.append(entrada)

    intervalos = {
        '1': 60 * 60,   # Hourly
        '2': 30 * 60,   # Every 30 minutes
        '3': 10 * 60,   # Every 10 minutes
        '4': 5 * 60,    # Every 5 minutes
        '5': 60         # Every minute
    }
    frecuencia = input(
        "Choose the frequency: '1' for every hour, '2' for every 30 minutes, etc.: ")
    errores_contados = 0

    while True:
        for url in urls:
            result_url = obtener_url(url)
            if result_url:
                guardar_url_nueva(result_url)
            else:
                errores_contados += 1

            time.sleep(5)  # You can adjust this to space out the requests

        if errores_contados == len(urls):
            print("All sites have been scanned, contain errors, or the button could not be located.\n... Finalizing the process ...\n")
            break

        time.sleep(intervalos[frecuencia])  # Uses the selected interval


if __name__ == '__main__':
    main()
