
<h1 align="center">pico-ducky</h1>
<div align="center">
  <strong>Haz un USB Rubber Ducky barato pero poderoso con un Raspberry Pi Pico</strong>
</div>
<br />
<div align="center">
  <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/dbisu/pico-ducky">
  <img alt="GitHub license" src="https://img.shields.io/github/license/dbisu/pico-ducky">
  <a href="https://github.com/dbisu/pico-ducky/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/dbisu/pico-ducky"></a>
  <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/dbisu/pico-ducky">
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/dbisu/pico-ducky">
</div>
<br />
Guía de inicio rápido
Instala y haz que tu USB Rubber Ducky funcione en menos de 5 minutos.

Descarga la última versión desde la página de Releases.

Conecta el dispositivo a un puerto USB mientras mantienes presionado el botón de arranque. Aparecerá como un dispositivo de medios extraíbles llamado RPI-RP2.

Instala CircuitPython en el Pico o Pico W.

Si usas una placa Pico:

Copia el archivo adafruit-circuitpython-raspberry_pi_pico-en_US-8.0.0.uf2 a la raíz del Pico (RPI-RP2). El dispositivo se reiniciará y, después de un segundo más o menos, se reconectará como CIRCUITPY.

Si usas una placa Pico W:

Copia el archivo adafruit-circuitpython-raspberry_pi_pico_w-en_US-8.0.0.uf2 a la raíz del Pico (RPI-RP2). El dispositivo se reiniciará y, después de un segundo más o menos, se reconectará como CIRCUITPY.

Copia la carpeta lib a la raíz del CIRCUITPY.

Copia *.py a la raíz del CIRCUITPY.

Sigue las instrucciones en README.md para entrar en el modo de configuración.

Copia tu payload como payload.dd en la raíz del CIRCUITPY.

Desconecta el dispositivo del puerto USB y quita el puente de configuración.

Disfruta de tu Pico-Ducky.

Modo de configuración
Para editar el payload, entra en modo de configuración conectando el pin 1 (GP0) al pin 3 (GND), esto evitará que el pico-ducky inyecte el payload en tu propia máquina.
La forma más fácil de hacerlo es usando un cable de puente entre esos pines, como se ve a continuación.



Modo de habilitación/deshabilitación de USB
Si necesitas que el pico-ducky no aparezca como un dispositivo de almacenamiento masivo USB para mayor discreción, sigue estas instrucciones.

Entra en modo de configuración.
Copia tu script payload al pico-ducky.
Desconecta el pico de tu PC anfitrión.
Conecta un cable de puente entre el pin 18 (GND) y el pin 20 (GPIO15).
Esto evitará que el pico-ducky aparezca como una unidad USB cuando se conecte al ordenador objetivo.
Retira el puente y vuelve a conectar a tu PC para reprogramar.
Pico: El modo predeterminado es almacenamiento masivo USB habilitado.
Pico W: El modo predeterminado es almacenamiento masivo USB deshabilitado



Instrucciones completas de instalación
Instala y haz que tu USB Rubber Ducky funcione en menos de 5 minutos.

Clona el repositorio para obtener una copia local de los archivos. git clone https://github.com/dbisu/pico-ducky.git

Descarga CircuitPython para Raspberry Pi Pico. *Actualizado a 8.0.0
Descarga CircuitPython para Raspberry Pi Pico W. *Actualizado a 8.0.0

Conecta el dispositivo a un puerto USB mientras mantienes presionado el botón de arranque. Aparecerá como un dispositivo de medios extraíbles llamado RPI-RP2.

Copia el archivo .uf2 descargado a la raíz del Pico (RPI-RP2). El dispositivo se reiniciará y, después de un segundo más o menos, se reconectará como CIRCUITPY.

Descarga adafruit-circuitpython-bundle-8.x-mpy-YYYYMMDD.zip aquí y extráelo fuera del dispositivo.

Navega a lib en la carpeta recién extraída y copia adafruit_hid a la carpeta lib en tu Raspberry Pi Pico.

Copia adafruit_debouncer.mpy y adafruit_ticks.mpy a la carpeta lib en tu Raspberry Pi Pico.

Copia asyncio a la carpeta lib en tu Pico.

Copia adafruit_wsgi a la carpeta lib en tu Pico.

Copia boot.py de tu clon a la raíz de tu Pico.

Copia duckyinpython.py, code.py, webapp.py, wsgiserver.py a la carpeta raíz del Pico.

Solo para Pico W Crea el archivo secrets.py en la raíz del Pico W. Esto contiene el nombre y la contraseña del AP que será creado por el Pico W.
secrets = { 'ssid' : "BadAPName", 'password' : "badpassword" }

Encuentra un script aquí o crea tu propio script usando Ducky Script y guárdalo como payload.dd en el Pico. Actualmente, pico-ducky solo soporta DuckyScript 1.0, no 3.0.

Ten cuidado, si tu dispositivo no está en modo de configuración, el dispositivo se reiniciará y después de medio segundo, el script se ejecutará.

Nota: por defecto, el Pico W no se mostrará como una unidad USB.

Servicio web del Pico W
El AP del Pico W por defecto tiene la dirección IP 192.168.4.1. Deberías poder encontrar el servicio web en http://192.168.4.1:80.

Los siguientes endpoints están disponibles en el servicio web:

bash
Copiar código
/
/new
/ducky
/edit/<filename>
/write/<filename>
/run/<filename>
Endpoints de la API

arduino
Copiar código
/api/run/<filenumber>
Modo de configuración
Para editar el payload, entra en modo de configuración conectando el pin 1 (GP0) al pin 3 (GND), esto evitará que el pico-ducky inyecte el payload en tu propia máquina.
La forma más fácil de hacerlo es usando un cable de puente entre esos pines, como se ve a continuación.



Modo de habilitación/deshabilitación de USB
Si necesitas que el pico-ducky no aparezca como un dispositivo de almacenamiento masivo USB para mayor discreción, sigue estas instrucciones.

Entra en modo de configuración.
Copia tu script payload al pico-ducky.
Desconecta el pico de tu PC anfitrión.
Conecta un cable de puente entre el pin 18 (GND) y el pin 20 (GPIO15).
Esto evitará que el pico-ducky aparezca como una unidad USB cuando se conecte al ordenador objetivo.
Retira el puente y vuelve a conectar a tu PC para reprogramar.
Pico: El modo predeterminado es almacenamiento masivo USB habilitado.
Pico W: El modo predeterminado es almacenamiento masivo USB deshabilitado



Múltiples payloads
Se pueden almacenar múltiples payloads en el Pico y Pico W.
Para seleccionar un payload, conecta a tierra uno de estos pines:

GP4 - payload.dd
GP5 - payload2.dd
GP10 - payload3.dd
GP11 - payload4.dd
Cambiar distribuciones de teclado
Copiado de Neradoc/Circuitpython_Keyboard_Layouts

Cómo usar una de estas distribuciones con el repositorio pico-ducky.
Ve a la página de la última versión, busca si tu idioma está en la lista.

Si tu idioma/distribución está en el paquete
Descarga el zip py, llamado circuitpython-keyboard-layouts-py-XXXXXXXX.zip.

NOTA: Puedes usar la versión mpy dirigida a la versión de Circuitpython que está en el dispositivo, pero en Raspberry Pi Pico no lo necesitas - solo reducen el tamaño del archivo y el uso de memoria al cargar, de lo cual el pico tiene suficiente.

Si tu idioma/distribución no está en el paquete
Prueba el generador en línea, debería proporcionarte un archivo zip con los paquetes para tu idioma.

https://www.neradoc.me/layouts/

Ahora tienes un archivo zip
Encuentra tu idioma/distribución en el directorio lib
Para un idioma LANG, copia los siguientes archivos desde la carpeta lib del zip al directorio lib de la placa.
NO modifiques el directorio adafruit_hid. Tus archivos van directamente en lib.
NO cambies los nombres o las extensiones de los archivos. Solo elige los correctos.
Reemplaza LANG con las letras para tu idioma de elección.

keyboard_layout_win_LANG.py
keycode_win_LANG.py
No olvides obtener la biblioteca adafruit_hid.

Así es como debería verse si tu idioma es francés, por ejemplo.



Modifica el código del pico-ducky para usar tu archivo de idioma:
Al comienzo del archivo comenta estas líneas:

py
Copiar código
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS as KeyboardLayout
from adafruit_hid.keycode import Keycode
Descomenta estas líneas:
Reemplaza LANG con las letras para tu idioma de elección. El nombre debe coincidir con el archivo (sin la extensión py o mpy).

py
Copiar código
from keyboard_layout_win_LANG import KeyboardLayout
from keycode_win_LANG import Keycode
Ejemplo: Configurar a teclado alemán (WIN_DE)
py
Copiar código
from keyboard_layout_win_de import KeyboardLayout
from keycode_win_de import Keycode
Copia los archivos keyboard_layout_win_de.mpy y keycode_win_de.mpy a la carpeta /lib en la placa Pico

Copiar código
adafruit_hid/
keyboard_layout_win_de.mpy
keycode_win_de.mpy
Enlaces y recursos útiles
Cómo recuperar tu Pico si se corrompe o no arranca.
Instrucciones de reinicio

Herramienta de instalación
raspberrydeveloper creó una herramienta para convertir un RPi Pico en blanco en un ducky.
Puedes encontrar la herramienta aquí

Documentos
CircuitPython

CircuitPython HID

Ducky Script

Tutoriales en video
tutorial de pico-ducky por NetworkChuck

lista de reproducción USB Rubber Ducky por Hak5

tutorial de CircuitPython en Raspberry Pi Pico por DroneBot Workshop

Proyectos relacionados
Defcon31-ducky
Todavía hay algunos de estos disponibles para comprar, solo en EE.UU.
