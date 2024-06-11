from machine import Pin, I2C
import ssd1306
import framebuf
import time

# Inicializa I2C y realiza un escaneo para verificar la dirección
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)
print("Escaneando I2C...")
devices = i2c.scan()
if devices:
    for device in devices:
        print(f"Dispositivo I2C encontrado en dirección: {hex(device)}")
else:
    print("No se encontraron dispositivos I2C")

# Usa la dirección I2C obtenida en el escaneo
oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

# Realiza una operación simple para verificar
oled.fill(0)  # Limpia la pantalla
oled.text("Hijos de puta", 0, 0)
oled.show()
time.sleep(2)
