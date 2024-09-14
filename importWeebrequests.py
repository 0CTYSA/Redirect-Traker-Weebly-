import requests
from bs4 import BeautifulSoup
import time

def obtener_url():
    url = 'https://culphiliv.weebly.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    boton = soup.find('a', class_='wsite-button')
    if boton:
        return boton['href']
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
    intervalos = {
        '1': 60 * 60,   # Cada hora
        '2': 30 * 60,   # Cada 30 minutos
        '3': 10 * 60,   # Cada 10 minutos
        '4': 5 * 60,    # Cada 5 minutos
        '5': 60         # Cada minuto
    }
    frecuencia = '5'  # Elige aquí la frecuencia. Por ejemplo: '1' para cada hora, '2' para cada 30 minutos, etc.
    
    while True:
        url = obtener_url()
        if url:
            guardar_url_nueva(url)
        time.sleep(intervalos[frecuencia])  # Usa el intervalo seleccionado

if __name__ == '__main__':
    main()
