import pyautogui
import keyboard
import time
import numpy as np

#Define list to be populated
arr_of_data = []

#Read file and get all the values

file = open("Folios Nuevos y Kilos.txt", "r")
lines = file.readlines()
file.close()

for line in lines:
    #if not blank line (ignore blank lines)
    if line.strip():
        splitted = line.split(sep = "\t")
        arr_of_data.append(splitted)


#Record lenght (rows and columns)
#rows (cantidad de folios WMS)
#columns (2 columns, folio y kilos)

rows = np.asarray(arr_of_data).shape[0]
columns = np.asarray(arr_of_data).shape[1]

#print data
#print(rows)
#print(columns)



#Digita Secuencia para Cerro Azul. Folio + enter. Kilos + Enter.    
#Al ingresar el folio se rellenan algunos campos necesarios. El ususario debe previamente rellenar los demas
#Cursor reaparece solo en barra caja para digitar el sgte Folio
#Obs. Agrega un time sleep porque wms puede ser lento

#El dato de Kilos (Column 1) viene incluido con un enter (salto de linea) \n
#El dato de Folio viene sin salto de linea. 

#Pero mejor borrar el salto de linea \n con rstrip() al momento de digitar y add enter aparte
#Loop thrugh List to write

'''
for i in range(rows):
    for j in range(columns):
        print(arr_of_data[i][j].rstrip())
        print("Here comes an enter key!")
        if(j==1):
            print("End of line!")

'''

#wait for 20 seconds for the User
print("Tienes 20 segundos para posarte en WMS - Campo Folio!")
time.sleep(20)

start_time = time.time()

for i in range(rows):
    for j in range(columns):
        #message to write is current value
        #rstrip removes \n
        value = arr_of_data[i][j].rstrip()
        #Si es el valor de kilos, si encuentra coma reemplaza por punto. (Formato de ingreso en WMS)
        if (j==1): 
            value = value.replace(",",".")

        pyautogui.typewrite(message = value, interval = 0.03)
        pyautogui.press("enter")
        #time sleep after every value
        time.sleep(0.35)

print("La digitacion de folios demoró: %s segundos" % (time.time() - start_time))
