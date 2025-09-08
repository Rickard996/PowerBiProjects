#Programa que digita folios o pallets ingresados previamente en FOLIOS.txt por el user

import pyautogui
import keyboard
import time
import ctypes

#Read file and get all the values

file = open("FOLIOS.txt", "r")
lines = file.readlines()
file.close()

#Check if cap lock is on. Define the functions
def is_capslock_on():
    return True if ctypes.WinDLL("User32.dll").GetKeyState(0x14) else False

def turn_capslock_on():
    if not is_capslock_on():
        pyautogui.press("capslock")

def turn_capslock_off():
    if is_capslock_on():
        pyautogui.press("capslock")

def press_backspace_key():
    pyautogui.press("backspace")

#codigo de Ingreso varas
def ingreso_varas():
    #wait for 15 seconds for the User
    print("Tienes 15 segundos para posarte en SAP/WMS!")
    time.sleep(15)

    for line in lines:
        pyautogui.typewrite(message = line, interval=0.05)
        time.sleep(0.05)
        
    #Last loop add enter
    pyautogui.press("enter")

#Codigo de Ingresa folios generico
def ingresa_folios_generico():
    #wait for 15 seconds for the User
    print("Tienes 15 segundos para posarte en SAP/WMS!")
    time.sleep(15)
    #turn off caps lock
    turn_capslock_off()
    start_time = time.time()
    for line in lines:
        line_two = str(line.upper())
        #print(line_two)
        pyautogui.typewrite(message = line_two, interval=0.03)
        time.sleep(0.15)
        pyautogui.press("enter")
        #time sleep between line
        time.sleep(0.15)
    pyautogui.press("enter")
    print("La digitacion de folios demoró: %s segundos" % (time.time() - start_time))

def ingresa_pallets_exportacion():
    #wait for 15 seconds for the User
    print("Tienes 15 segundos para posarte en SAP/WMS!")
    time.sleep(15)
    #turn off caps lock

    turn_capslock_off()
    start_time = time.time()
    for line in lines:
        line_two = str(line.upper())
        #print(line_two)
        pyautogui.typewrite(message = line_two, interval=0.03)
        time.sleep(0.05)
        pyautogui.press("enter")
        time.sleep(0.15)
        #press backspace 9 times
        for x in range(9):
            press_backspace_key()

        #time sleep between line
        time.sleep(0.15)
    
    print("La digitacion de folios demoró: %s segundos" % (time.time() - start_time))

#Ingresa por pallet en el armado bultos
def ingresa_pallets_bultos():
    #wait for 15 seconds for the User
    print("Tienes 15 segundos para posarte en SAP/WMS!")
    time.sleep(15)
    #turn on caps lock

    turn_capslock_off()
    start_time = time.time()
    for line in lines:
        line_two = str(line.upper())
        #print(line_two)
        pyautogui.typewrite(message = line_two, interval=0.03)
        #time.sleep(0.05)
        #pyautogui.press("enter")
        time.sleep(5.5)
        #press backspace 9 times
        for x in range(12):
            press_backspace_key()

        #time sleep between line
        time.sleep(0.05)

    #Last loop add enter
    pyautogui.press("enter")
    print("La digitacion de folios demoró: %s segundos" % (time.time() - start_time))


#Ask the user which version wishes to use? then use switch case to execute
mode = input('Que versión del digitador deseas usar?\n1.- Ingreso Varas (Digita folio + 1 Enter)\n2.- Ingresa Folios Genérico - Devoluciones (Digita folio + 2 Enter)\n3.- Ingreso Pallets exportacion (Digita Pallet + 2Enter + 9 Clear)\n4.- Ingreso Pallet Armado bultos (Digita pallet + Enter + 9 Clear)\n5.- Salir\n') 
mode = int(mode)       #cast to int

if mode == 1:
    ingreso_varas()
    pyautogui.hotkey('winleft', 'd')
elif mode == 2:
    ingresa_folios_generico()
    pyautogui.hotkey('winleft', 'd')
elif mode == 3:
    ingresa_pallets_exportacion()
    pyautogui.hotkey('winleft', 'd')
elif mode == 4:
    ingresa_pallets_bultos()
    pyautogui.hotkey('winleft', 'd')
else:
    print("Saliendo")






