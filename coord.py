import pyautogui
import time

print("Déplacez votre souris vers l'emplacement désiré...")

# Déplace la souris vers (100, 100)
#pyautogui.moveTo(100, 100, duration=1)

# Attendez 5 secondes pour que vous puissiez placer votre souris
time.sleep(5)
print(pyautogui.position())  # Déplacez la souris à l'emplacement souhaité pour obtenir les coordonnées
# Obtenez et affichez les coordonnées de la souris
x, y = pyautogui.position()
print(f"Les coordonnées de la souris sont : x={x}, y={y}")

