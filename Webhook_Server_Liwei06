# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:29:04 2022

@author: Liwei
"""
import json
import difflib
import re
#import Auto_Firstrade_V04
import pyautogui,sys
Mystock = 'SQQQ'
My_Stock_quantity = '5'
def Stock_Buy_in(stock_name, stock_quantity): 
#-----------買進
    # #init_stock_web()
    # pyautogui.click((pyautogui.locateCenterOnScreen('C:/Users/Liwei/python-imagesearch/firstrade_01.png')),interval=1)
    pyautogui.click((pyautogui.locateCenterOnScreen('C:/Users/Liwei/python-imagesearch/firstrade_02.png')),interval=0)
    pyautogui.press('tab')
    #pyautogui.typewrite(My_Stock_quantity)
    pyautogui.typewrite(str(stock_quantity))
    pyautogui.press('tab')
    #pyautogui.typewrite(Mystock)
    pyautogui.typewrite(stock_name)      
    pyautogui.press('tab')
    pyautogui.press('tab',interval=0) 
    pyautogui.press('down',interval=1.5) 
    pyautogui.click((pyautogui.locateCenterOnScreen('C:/Users/Liwei/python-imagesearch/firstrade_05.png')),interval=0.5)
    #pyautogui.click((pyautogui.locateCenterOnScreen('C:/Users/Liwei/python-imagesearch/firstrade_06.png')),interval=1.5)
    print ('Buy in:', stock_name, '*num:', str(stock_quantity))
    init_stock_web()

def Stock_Sell_out(stock_name, stock_quantity): 
#-----------賣出
    #init_stock_web()
    # pyautogui.click((pyautogui.locateCenterOnScreen('C:/Users/Liwei/python-imagesearch/firstrade_01.png')),interval=1)
    pyautogui.click((pyautogui.locateCenterOnScreen('C:/Users/Liwei/python-imagesearch/firstrade_02.png')),interval=0)
    pyautogui.press('down',interval=0) #賣出
    pyautogui.press('tab',interval=0)
    pyautogui.typewrite(str(stock_quantity))
    pyautogui.press('tab')
    pyautogui.typewrite(stock_name)       
    pyautogui.press('tab')
    pyautogui.press('tab',interval=0) 
    pyautogui.press('down',interval=1.5) 
    pyautogui.click((pyautogui.locateCenterOnScreen('C:/Users/Liwei/python-imagesearch/firstrade_05.png')),interval=0.5)
    #pyautogui.click((pyautogui.locateCenterOnScreen('C:/Users/Liwei/python-imagesearch/firstrade_06.png')),interval=1.5)
    print ('Sell out:', stock_name, '*num:', str(stock_quantity))
    init_stock_web()

def init_stock_web():
    pyautogui.click(125,38)
    press_up_times_max = 5
    press_up_times = 1
    while press_up_times<= press_up_times_max:
        pyautogui.press('up')
        press_up_times+=1
    pyautogui.click((pyautogui.locateCenterOnScreen('C:/Users/Liwei/python-imagesearch/firstrade_00.png')),interval=0.1)
    pyautogui.click((pyautogui.locateCenterOnScreen('C:/Users/Liwei/python-imagesearch/firstrade_01.png')),interval=1)
    #pyautogui.click((pyautogui.locateCenterOnScreen('C:/Users/Liwei/python-imagesearch/firstrade_02.png')),interval=0)
    
from flask import Flask, request, abort
app = Flask(__name__)
@app.route('/webhook', methods=['POST'])

def get_webhook():

    if request.method == 'POST':
        
        print("received data: \n\r", request.json) 
        My_json=request.json
        #print (My_json)
        #print(type(My_json))
        print("------Packet Data------")
        print("pair: ", My_json["pair"])
        print("side: ", My_json["side"])
        print("size: ", My_json["size"])
        print("update_size: ", My_json["update_size"])
        print("-----------------------")
        if re.match("buy",My_json["side"] ):
            print ('it is buy in..\n\r')
            Stock_Buy_in(My_json["pair"], int(My_json["size"]))
            #Stock_Buy_in("TQQQ", int(My_json["size"]))
        if re.match("sell",My_json["side"] ):
            print ('it is sell out..\n\r')
            Stock_Sell_out(My_json["pair"],  int(My_json["size"]))
            #Stock_Sell_out("TQQQ",  int(My_json["size"]))
        return 'success', 200
    else:
        
        abort(400)
if __name__ == '__main__':
    app.run()
