from pynput import mouse as ms
from pynput.keyboard import Key, Controller, Listener
import time
import csv
from tkinter import filedialog
from tkinter import *
import sys
import threading
from threading import Thread
import _thread
from tkinter import messagebox

run = True
resetX = 0
resetY = 0
keyboard = Controller()
def on_click(x, y, button, pressed):
    global resetX
    resetX = ms.Controller().position[0]
    global resetY
    resetY = ms.Controller().position[1]
    if pressed:
        # Stop listener
        return False

def on_press(key):
	if key == Key.esc:
		# Stop listener
		print("stopping")
		_thread.interrupt_main()

def stopper():
	with Listener(on_press=on_press) as listener:
		listener.join()  


def month_selector(month):
    switcher = {
                "1": 0,
                "2": 1,
                "3": 2,
                "4": 3,
                "5": 4,
                "6": 5,
                "7": 6,
                "8": 7,
                "9": 8,
                "10": 9,
                "11": 10,
                "12": 11,
    }

    return switcher.get(month)

def year_selector(year):
    switcher = {
                "2018": 0,
                "2019": 1,
                "2020": 2,
                "2021": 3,
                "2022": 4,
                "2023": 5,
                "2024": 6,
                "2025": 7,
                "2026": 8,
                "2027": 9,
                "2028": 10,
                "2029": 12,
                "2030": 13,
                "2031": 14,        
               
    }

    return switcher.get(year)

def country_selector(country):
    switcher = {
                "USA": 0,
                "CANADA": 1,
    }

    return switcher.get(country)

def card_selector(card):
    switcher = {
                "Discover": 0,
                "MasterCard": 1,
                "Visa": 2,
                "American Express": 3,
                "Solo": 4,
                "JCB": 5,
    }

    return switcher.get(card)

def state_selector(country, state):
    if country == "CANADA":
        switcher = {
                "AB": 0,
                "BC": 1,
                "MB": 2,
                "NB": 3,
                "NL": 4,
                "NT": 5,
                "NS": 6,
                "NU": 7,
                "ON": 8,
                "PE": 9,
                "QC": 10,
                "SK": 11,
                "YT": 12,
        }
    elif country == "USA":
        switcher = {
                            "AL": 0,
                            "AK": 1,
                            "AS": 2,
                            "AZ": 3,
                            "AR": 4,
                            "CA": 5,
                            "CO": 6,
                            "CT": 7,
                            "DE": 8,
                            "DC": 9,
                            "FM": 10,
                            "FL": 11,
                            "GA": 12,
                            "GU": 13,
                            "HI": 14,
                            "ID": 15,
                            "IL": 16,
                            "IN": 17,
                            "IA": 18,
                            "KS": 19,
                            "KY": 20,
                            "LA": 21,
                            "ME": 22,
                            "MH": 23,
                            "MD": 24,
                            "MA": 25,
                            "MI": 26,
                            "MN": 27,
                            "MS": 28,
                            "MO": 29,
                            "MT": 30,
                            "NE": 31,
                            "NV": 32,
                            "NH": 33,
                            "NJ": 34,
                            "NM": 35,
                            "NY": 36,
                            "NC": 37,
                            "ND": 38,
                            "MP": 39,
                            "OH": 40,
                            "OK": 41,
                            "OR": 42,
                            "PW": 43,
                            "PA": 44,
                            "PR": 45,
                            "RI": 46,
                            "SC": 47,
                            "SD": 48,
                            "TN": 49,
                            "TX": 50,
                            "UT": 51,
                            "VT": 52,
                            "VI": 53,
                            "VA": 54,
                            "WA": 55,
                            "WV": 56,
                            "WI": 57,
                            "WY": 58,
                    
            }

    return switcher.get(state)

root = Tk()
root.withdraw()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
print (root.filename)
file=open(root.filename, "r")
reader = csv.reader(file)

root.deiconify()
messagebox.showinfo("Information","Upon clicking this OK button, the program will start listening for you to click on the RESET button in the Sieu profile page. Once you click that it will begin emulating keystrokes so if something goes wrong, press the ""ESC"" key to stop the program at any time")
with ms.Listener(on_click=on_click) as listener:
    listener.join()

time.sleep(1)
saveX = resetX + 46
saveY = resetY
pnX = resetX
pnY = resetY + 70

time_delay = 0.03

if __name__ == '__main__':
	threaded = Thread(target=stopper)
	threaded.daemon = True
	threaded.start()		


	for inputValue in reader:
	        time.sleep(time_delay)
	         
	        ms.Controller().position = (pnX, pnY)
	        ms.Controller().press(ms.Button.left)
	        ms.Controller().release(ms.Button.left)

	        time.sleep(time_delay)
	        
	        for char in inputValue[0]:
	            keyboard.press(char)
	            keyboard.release(char)
	            
	        time.sleep(time_delay)
	        keyboard.press(Key.tab)
	        time.sleep(time_delay)
	        
	        for char in inputValue[1]:
	            keyboard.press(char)
	            keyboard.release(char)

	        time.sleep(time_delay)
	        keyboard.press(Key.tab)
	        time.sleep(time_delay)

	        for char in inputValue[2]:
	            keyboard.press(char)
	            keyboard.release(char)

	        time.sleep(time_delay)
	        keyboard.press(Key.tab)
	        time.sleep(time_delay)

	        for char in inputValue[3]:
	            keyboard.press(char)
	            keyboard.release(char)

	        time.sleep(time_delay)
	        keyboard.press(Key.tab)
	        time.sleep(time_delay)

	        for char in inputValue[4]:
	            keyboard.press(char)
	            keyboard.release(char)

	        time.sleep(time_delay)
	        keyboard.press(Key.tab)
	        time.sleep(time_delay)

	        for char in inputValue[5]:
	            keyboard.press(char)
	            keyboard.release(char)
	            
	        time.sleep(time_delay)     
	        keyboard.press(Key.tab)
	        time.sleep(time_delay)

	        for char in inputValue[6]:
	            keyboard.press(char)
	            keyboard.release(char)

	        time.sleep(time_delay)
	        keyboard.press(Key.tab)
	        time.sleep(time_delay)

	        for char in inputValue[7]:
	            keyboard.press(char)
	            keyboard.release(char)

	        time.sleep(time_delay)
	        keyboard.press(Key.tab)
	        time.sleep(time_delay)
	        
	        for char in inputValue[8]:
	            keyboard.press(char)
	            keyboard.release(char)
	            
	        time.sleep(time_delay)   
	        keyboard.press(Key.tab)
	        time.sleep(time_delay)
	        keyboard.press(Key.tab)
	        time.sleep(time_delay)

	        for tabs in range(country_selector(inputValue[10])):
	            keyboard.press(Key.down)
	            time.sleep(time_delay)
	            keyboard.release(Key.down)
	            time.sleep(time_delay)

	        time.sleep(time_delay)    
	        keyboard.press(Key.shift)
	        time.sleep(time_delay)
	        keyboard.press(Key.tab)
	        time.sleep(time_delay)
	        keyboard.release(Key.shift)
	        time.sleep(time_delay)
	        keyboard.release(Key.tab)
	        time.sleep(time_delay)

	        for tabs in range(state_selector(inputValue[10], inputValue[9])):
	            keyboard.press(Key.down)
	            keyboard.release(Key.down)
	            

	        time.sleep(time_delay)    
	        keyboard.press(Key.tab)
	        time.sleep(time_delay)
	        keyboard.press(Key.tab)
	        time.sleep(time_delay)

	        for tabs in range(card_selector(inputValue[11])):
	            keyboard.press(Key.down)
	            keyboard.release(Key.down)

	        time.sleep(time_delay)
	        keyboard.press(Key.tab)
	        time.sleep(time_delay)


	        for char in inputValue[12]:
	            keyboard.press(char)
	            keyboard.release(char)

	        time.sleep(time_delay)
	        keyboard.press(Key.tab)
	        time.sleep(time_delay)


	        for char in inputValue[13]:
	            keyboard.press(char)
	            keyboard.release(char)

	        time.sleep(time_delay)
	        keyboard.press(Key.tab)
	        time.sleep(time_delay)

	        for tabs in range(month_selector(inputValue[14])):
	            keyboard.press(Key.down)
	            keyboard.release(Key.down)

	        time.sleep(time_delay)
	        keyboard.press(Key.tab)
	        time.sleep(time_delay)

	        for tabs in range(year_selector(inputValue[15])):
	            keyboard.press(Key.down)
	            keyboard.release(Key.down)

	        time.sleep(time_delay)
	        ms.Controller().position = (saveX, saveY)
	        time.sleep(time_delay)
	        ms.Controller().press(ms.Button.left)
	        time.sleep(time_delay)
	        ms.Controller().release(ms.Button.left)
	        time.sleep(time_delay)

	        ms.Controller().position = (resetX, resetY)
	        time.sleep(time_delay)
	        ms.Controller().press(ms.Button.left)
	        time.sleep(time_delay)
	        ms.Controller().release(ms.Button.left)
	        time.sleep(time_delay)

	    


