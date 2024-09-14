# Automatización de Escaneo para Sitios Weebly

Este proyecto contiene un script en Python diseñado específicamente para escanear y monitorear cambios en sitios web que utilizan el dominio "weebly.com". La automatización se enfoca en detectar y registrar las URLs de botones específicos dentro de estas páginas, facilitando el seguimiento de modificaciones y actualizaciones en los sitios de interés.

## Características

- **Detección de Cambios**: Capacidad para identificar cambios en las URLs de los botones en sitios Weebly.
- **Automatización**: Ejecuta escaneos en intervalos configurables para un seguimiento continuo.
- **Reporte de Errores**: Informa sobre errores encontrados durante el escaneo, como páginas no encontradas o elementos faltantes.

## Requisitos

Para ejecutar este script, necesitas tener instalado:

- Python 3.x
- Bibliotecas Python: `requests` y `BeautifulSoup4`

Puedes instalar las dependencias necesarias con el siguiente comando:

```bash
pip install requests beautifulsoup4
```

## Uso

1. Clona este repositorio o descarga los archivos directamente.
2. Abre tu terminal o línea de comandos.
3. Navega hasta el directorio donde se encuentra el script.
4. Ejecuta el script con el comando:

```bash
python importWeebrequests.py
```

5. Sigue las instrucciones en pantalla para introducir las URLs y comenzar el escaneo.

## Contribuir

Si deseas contribuir a este proyecto, por favor considera:

- Enviar sugerencias para mejorar el código.
- Reportar bugs.
- Añadir funcionalidades nuevas.

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo `LICENSE` para detalles.
