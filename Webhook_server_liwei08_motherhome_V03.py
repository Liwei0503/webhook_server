# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
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
import threading
import time
import queue

Mystock = 'SQQQ'
My_Stock_quantity = '5'
semaphore = threading.Semaphore(1)
my_queue = queue.Queue()
semaphore = threading.Semaphore(1)
Thread_Run=0

class Worker(threading.Thread):
  def __init__(self, queue, num, semaphore):
    threading.Thread.__init__(self)
    self.queue = queue
    self.num = num
    self.semaphore = semaphore

  def run(self):
    Thread_Run=1
    while self.queue.qsize() > 0:
      msg = self.queue.get()

      # 取得旗標
      semaphore.acquire()
      # print("Semaphore acquired by Worker %d" % self.num)
      # print("\n\rThread_Run=1\n\r")
      # 僅允許有限個執行緒同時進的工作
      # print("Worker %d: %s" % (self.num, msg))
      # time.sleep(5)

      if re.match("buy",msg["side"] ):
          print ('it is buy in..\n\r')
          Stock_Buy_in(msg["pair"], int(msg["size"]))
          # #Stock_Buy_in("TQQQ", int(My_json["size"]))
      if re.match("sell",msg["side"] ):
          print ('it is sell out..\n\r')
          Stock_Sell_out(msg["pair"],  int(msg["size"]))
          # #Stock_Sell_out("TQQQ",  int(My_json["size"]))


      # 釋放旗標
      # print("Semaphore released by Worker %d" % self.num)
      self.semaphore.release()
    Thread_Run=0
    # print("\n\r$Thread_Run=0\n\r")        
# my_worker1 = Worker(my_queue, 1, semaphore)
#my_worker1.start()

def Stock_Buy_in(stock_name, stock_quantity): 
#-----------買進
    # #init_stock_web()
    pyautogui.click(105,  22) #點選firstrade交易頁籤    
    # pyautogui.click((pyautogui.locateCenterOnScreen(
    #     'C:/Users/Liwei/python-imagesearch/firstrade_01.png')),interval=1)
    pyautogui.click( 315, 197,interval=1)
    # pyautogui.click((pyautogui.locateCenterOnScreen(
    #     'C:/Users/Liwei/python-imagesearch/firstrade_02.png')),interval=0.5)
    pyautogui.click(37, 438,interval=0.5)

    pyautogui.press('tab')
    #pyautogui.typewrite(My_Stock_quantity)
    pyautogui.typewrite(str(stock_quantity))
    pyautogui.press('tab')
    #pyautogui.typewrite(Mystock)
    pyautogui.typewrite(stock_name)      
    pyautogui.press('tab')
    pyautogui.press('tab',interval=1) 
    pyautogui.press('down',interval=0.5) 
    #pyautogui.click((pyautogui.locateCenterOnScreen('C:/Users/Liwei/python-imagesearch/firstrade_05.png')),interval=1.5)
    #pyautogui.click((pyautogui.locateCenterOnScreen('E:/Projeccts/Python_Project/firstrade_05.png')),interval=1.5)
    pyautogui.moveTo(753, 656,duration=1)
    pyautogui.click(753, 656,duration=0) 
    # pyautogui.click((pyautogui.locateCenterOnScreen(
    #     'C:/Users/Liwei/python-imagesearch/firstrade_06.png'))8TQQQ,interval=1.5)
    print ('Buy in:', stock_name, '*num:', str(stock_quantity))
    init_stock_web()

def Stock_Sell_out(stock_name, stock_quantity): 
#-----------賣出
    #init_stock_web()
    pyautogui.click(105,  22) #點選firstrade交易頁籤    
    # pyautogui.click((pyautogui.locateCenterOnScreen(
    #     'C:/Users/Liwei/python-imagesearch/firstrade_01.png')),interval=1)
    pyautogui.click( 315, 197,interval=1)
    # pyautogui.click((pyautogui.locateCenterOnScreen(
    #     'C:/Users/Liwei/python-imagesearch/firstrade_02.png')),interval=0.5)
    pyautogui.click(37, 438,interval=0.5)
    
    pyautogui.press('down',interval=1) #賣出
    pyautogui.press('tab',interval=1)
    pyautogui.typewrite(str(stock_quantity))
    pyautogui.press('tab')
    pyautogui.typewrite(stock_name)       
    pyautogui.press('tab')
    pyautogui.press('tab',interval=0.5) 
    pyautogui.press('down',interval=0.5) 
    #pyautogui.click((pyautogui.locateCenterOnScreen('E:/Projeccts/Python_Project/firstrade_05.png')),interval=1.5)
    pyautogui.moveTo(753, 656,duration=1)
    pyautogui.click(753, 656,duration=0) 
    # pyautogui.click((pyautogui.locateCenterOnScreen(
    #     'C:/Users/Liwei/python-imagesearch/firstrade_06.png')),interval=1.5)
    print ('Sell out:', stock_name, '*num:', str(stock_quantity))
    init_stock_web()

def init_stock_web():
    #pyautogui.click(125,38)
    pyautogui.click(105,  22) #點選firstrade交易頁籤    
    #pyautogui.click(1154,1003)
    #pyautogui.click( 315, 197,interval=1)
    
    press_up_times_max = 5
    press_up_times = 1
    while press_up_times<= press_up_times_max:
        pyautogui.press('up')
        press_up_times+=1
    # pyautogui.click((pyautogui.locateCenterOnScreen(
    #     'C:/Users/Liwei/python-imagesearch/firstrade_00.png')),interval=1)
    pyautogui.click( 315, 197,interval=0.6)
    
    # pyautogui.click((pyautogui.locateCenterOnScreen(
    #     'C:/Users/Liwei/python-imagesearch/firstrade_01.png')),interval=1)
    pyautogui.click( 315, 197,interval=0.6)
    # # pyautogui.click((pyautogui.locateCenterOnScreen(
    # #     'C:/Users/Liwei/python-imagesearch/firstrade_02.png')),interval=0)
    pyautogui.click(612, 790,interval=0)
   # pyautogui.click(607, 282,interval=0.5)


from flask import Flask, request, abort
app = Flask(__name__)
@app.route('/webhook', methods=['POST'])

def get_webhook():

    if request.method == 'POST':
        
        print("received data: \n\r", request.json) 
        My_json=request.json
        # #print (My_json)
        # #print(type(My_json))
        # print("------Packet Data------")
        # print("pair: ", My_json["pair"])
        # print("side: ", My_json["side"])
        # print("size: ", My_json["size"])
        # print("update_size: ", My_json["update_size"])
        # print("-----------------------")        
        my_queue.put(My_json)
        if (Thread_Run==0):
            my_worker1 = Worker(my_queue, 1, semaphore)
            my_worker1.start()
            print("my_worker1.start()")
            
        
        # if re.match("buy",My_json["side"] ):
        #     print ('it is buy in..\n\r')
        #     # Stock_Buy_in(My_json["pair"], int(My_json["size"]))
        #     # #Stock_Buy_in("TQQQ", int(My_json["size"]))
        # if re.match("sell",My_json["side"] ):
        #     print ('it is sell out..\n\r')
        #     # Stock_Sell_out(My_json["pair"],  int(My_json["size"]))
        #     # #Stock_Sell_out("TQQQ",  int(My_json["size"]))
        return 'success', 200
    else:
        
        abort(400)
if __name__ == '__main__':
    app.run()



