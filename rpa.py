import pyautogui
import subprocess
import time
import pytesseract
from PIL import ImageGrab
from pynput.keyboard import Controller


def lancer_logiciel(nom_logiciel):
    try:
        # Exécute le nom du logiciel comme une commande dans le shell
        subprocess.run(nom_logiciel, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur: Impossible de lancer {nom_logiciel}. Détails : {e}")
    except FileNotFoundError:
        print(f"Erreur : Le logiciel '{nom_logiciel}' n'a pas été trouvé. Assurez-vous qu'il est installé et accessible dans le PATH.")
def split_text_to_list(text):
    elements = []
    word = ""

    for char in text:
        if char.isalnum():  # Vérifie si le caractère fait partie d'un mot
            word += char
        else:
            if word:
                elements.append(word)  # Ajoute le mot accumulé
                word = ""
            if char == ' ':
                elements.append(' ')  # Ajoute l'espace
            elif char == '\n':
                elements.append('\n')  # Ajoute le retour à la ligne

    # Ajoute le dernier mot s'il existe
    if word:
        elements.append(word)

    return elements

def type_with_delay(text,keyboard, delay=0):
    for char in text:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(delay)
def replace_newline_sequences(chars):
    result = []
    i = 0
    while i < len(chars):
        if i + 1 < len(chars) and chars[i] == '\n' and chars[i + 1] == '\n':
            result.append(' ')
            result.append('\n')
            i += 2  # Skip the next '\n'
        else:
            result.append(chars[i])
            i += 1
    return result	
def autoComplete():
    # Définir la région rectangulaire (left, top, right, bottom)
    bbox = (463, 305, 1457, 412) # les coordonnées ont étés obtenu graçe une autre programme  coord.py 
    time.sleep(2)  # Attendre que le navigateur soit prêt
    # Capture la capture d'écran de la région spécifiée
    screenshot = ImageGrab.grab(bbox)
    # Utilise pytesseract pour extraire le texte de l'image
    text = pytesseract.image_to_string(screenshot, lang='fra')  # 'fra' pour le français
    text = replace_newline_sequences(text)
    # Affiche le texte extrait
    print(text)
    result = split_text_to_list(text)
    #print(result)
    keyboard = Controller()
    pyautogui.click(x=665, y=452)  # google chrome
    for chaine in result[:-1]:
    	#pyautogui.write(chaine)
    	 type_with_delay(chaine,keyboard)
    pyautogui.write(' ') 



if __name__ == "__main__":
    # Demande à l'utilisateur de saisir le nom du logiciel à lancer
    #nom_logiciel = input("Entrez le nom du logiciel à lancer : ")
    #lancer_logiciel(nom_logiciel)
    lancer_logiciel("google-chrome")
    #s'assurer que le navigateur est ouvert et en plein écran
    time.sleep(2)  # Attendre que le navigateur soit prêt
    # Clique dans la barre de recherche de Google (à ajuster selon la position)
    #pyautogui.click(x=397, y=92)  #firefox 
    pyautogui.click(x=279, y=89)  # google chrome
    # Tape la requête(https://10fastfingers.com/typing-test/french)  / et : sont permutés dû au clavier mais un shift pourait resoudre le problème comme pour les le 10 et le . 
    pyautogui.write('https/::')    
    pyautogui.keyDown('shift')
    pyautogui.write('10')    
    pyautogui.keyUp('shift')
    pyautogui.write('fastfingers')  
    pyautogui.keyDown('shift')  
    pyautogui.write('.') 
    pyautogui.keyUp('shift')
    pyautogui.write('com:typing-test:french')       
    # Appuis sur Entrée
    pyautogui.press('enter')
    
    start_time = time.time()
    duree = 60  # 1 minute = 60 secondes
    while time.time() - start_time < duree:
    	autoComplete()
    	time.sleep(1)  # Délai de 1 seconde entre les appels de la fonction

    
