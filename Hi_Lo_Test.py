from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException   
from IPython.display import display, clear_output
import ipywidgets as widgets
from selenium.common import exceptions
import time
import random 
import keyboard

import threading
import keyboard

### User Name
USER_ = "XXXX"
### Pword
PASS_ = "XXXX"

### global variable
VERY_VERY_QUICKWAIT_ = 0.05
VERY_QUICKWAIT_ = 0.3
QUICK_WAIT_ = 0.5 
MEDIUM_WAIT_ = 1 
LONG__WAIT_ = 3 

### Table
Table = []

### Card dealt
Card_dealt = []

# ------------ Waiting functions --------------    
# base + random 

def VERY_QUICKWAIT():  
    return VERY_QUICKWAIT_ + (random.random() / 10)

def QUICK_WAIT():
    return QUICK_WAIT_ + (random.random() / 5)

def MEDIUM_WAIT(): 
    return MEDIUM_WAIT_ + (random.random() / 2)

def LONG_ASS_WAIT(): # Pour la navigation entre les pages
    return LONG_ASS_WAIT_ + (random.random() / 1)

# slow typing function
def slow_typing(element, text):
   for character in text:
      element.send_keys(character)
      time.sleep(VERY_QUICKWAIT())

# look if selenium finds the element
def check_exists_by_xpath(xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

# Hi-Lo Strategy
def Hi_Lo(Table, Card_dealt):    
    count = 0
    for c in Table + Card_dealt:
        if c[-1] in ("0","K","J","Q","A"):
            count -= 1
        if c[-1] in ("2","3","4","5","6"):
            count += 1  
    return count
 
 # Open the browser with the driver or use the function below 
 def open_browser():
    browser = webdriver.Firefox()
    browser.get('https://portail.espacejeux.com/en/home')
    time.sleep(LONG_WAIT())  
    
### Function to open casino
# Open espacejeux
# Open account defined by USER_ & PASS_
# Look for the blackJack Party table 
# Open thr blackJack party table
# Change the camera view for html display of the cards (instead of the video)
def open_casino(browser):
    
    login_button = browser.find_element_by_xpath("//a[@id='mel-nav-toggle-conn']")
    login_button.click()
    ### fill in the login informations 
    Username = browser.find_element_by_xpath("//input[@id='login_username']")
    slow_typing(Username, USER_)

    Password = browser.find_element_by_xpath("//input[@id='login_password']")
    slow_typing(Password, PASS_)

    time.sleep(QUICK_WAIT())

    LoginForReal = browser.find_element_by_xpath("//button[@id='btn-login']")
    LoginForReal.click()
    
    ### Casino 
    time.sleep(LONG_WAIT())
    Casino = browser.find_element_by_xpath("//a[@href='https://www.espacejeux.com/en/casino']")
    Casino.click()
    
    ### Live Casino BlackJack
    time.sleep(LONG_WAIT())
    Casino_BJ = browser.find_element_by_xpath("//button[@class='menu-item__btn']")
    Casino_BJ.click()
    time.sleep(QUICK_WAIT())

    Casino_BJ = browser.find_element_by_xpath("//a[@href='/en/casino/live-casino/live-blackjack']")
    Casino_BJ.click()
    
    ### BlackJack Party
    time.sleep(LONG_WAIT())
    Casino_BJ_Party = browser.find_element_by_xpath("//span[text()='Blackjack Party']/../../../a[@class='buttonJouer']")
    Casino_BJ_Party.click()
    
    ### Switch to casino window
    time.sleep(LONG_WAIT()+ 2)
    browser.switch_to.window(browser.window_handles[1])
    
    ### Change camera view for html display 
    time.sleep(LONG_WAIT())
    Change_camera = browser.find_element_by_xpath("//button[@data-role='video-button']")
    Change_camera.click()
    
    
# Press Q to exit the main while loop (when shuffle)
keep_going = True
def key_capture_thread():
    global keep_going
    while True:
        if keyboard.is_pressed('q'): 
            keep_going = False

# Loop until q is pressed. Will display the Hi-Lo count after each iteration.
# After each play, cards dealth will append the Card_deatl list. 

# To do : Detect the shuffle 

def bot_thread(browser, Table):
    threading.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()
    global Card_dealt
    while(keep_going):
    # Will unpause from inactivity
        if check_exists_by_xpath("//div[@data-role='inactivity-message-clickable']"):
            MEDIUM_WAIT()
            print("Innactif")
            browser.find_element_by_xpath("//div[@data-role='inactivity-message-clickable']").click()
        else:
            time.sleep(VERY_VERY_QUICKWAIT_)
            Previous_round = Table
            Table = []
            try :
                #print('----------- Seat D ------------') #           
                SeatDealer_cards = browser.find_element_by_xpath("//div[@data-role='seatDealer']")   
                CardsDealer = SeatDealer_cards.find_elements_by_xpath(".//span[@cl='wrapper--1U4HP']")
                for card in CardsDealer:
                    Table.append(card.get_attribute('data-role'))

                #print('----------- Seat 7 ------------') #        
                Seat7_cards = browser.find_element_by_xpath("//div[@data-role='seat7']")   
                Cards7 = Seat7_cards.find_elements_by_xpath(".//span[@cl='wrapper--1U4HP']")
                for card in Cards7:
                    Table.append(card.get_attribute('data-role'))

                #print('----------- Seat 6 ------------') # 
                Seat6_cards = browser.find_element_by_xpath("//div[@data-role='seat6']")   
                Cards6 = Seat6_cards.find_elements_by_xpath(".//span[@cl='wrapper--1U4HP']")
                for card in Cards6:
                    Table.append(card.get_attribute('data-role'))

                #print('----------- Seat 5 ------------') # 
                Seat5_cards = browser.find_element_by_xpath("//div[@data-role='seat5']")   
                Cards5 = Seat5_cards.find_elements_by_xpath(".//span[@cl='wrapper--1U4HP']")
                for card in Cards5:
                    Table.append(card.get_attribute('data-role'))

                #print('----------- Seat 4 ------------') #   
                Seat4_cards = browser.find_element_by_xpath("//div[@data-role='seat4']")   
                Cards4 = Seat4_cards.find_elements_by_xpath(".//span[@cl='wrapper--1U4HP']")
                for card in Cards4:
                    Table.append(card.get_attribute('data-role'))

                #print('----------- Seat 3 ------------') #   
                Seat3_cards = browser.find_element_by_xpath("//div[@data-role='seat3']")   
                Cards3 = Seat3_cards.find_elements_by_xpath(".//span[@cl='wrapper--1U4HP']")
                for card in Cards3:
                    Table.append(card.get_attribute('data-role'))

                #print('----------- Seat 2 ------------') #   
                Seat2_cards = browser.find_element_by_xpath("//div[@data-role='seat2']")   
                Cards2 = Seat2_cards.find_elements_by_xpath(".//span[@cl='wrapper--1U4HP']")
                for card in Cards2:
                    Table.append(card.get_attribute('data-role'))

                #print('----------- Seat 1 ------------') #
                Seat1_cards = browser.find_element_by_xpath("//div[@data-role='seat1']")   
                Cards1 = Seat1_cards.find_elements_by_xpath(".//span[@cl='wrapper--1U4HP']")
                for card in Cards1:
                    Table.append(card.get_attribute('data-role'))

            except exceptions.StaleElementReferenceException as e:
                time.sleep(QUICK_WAIT_)

            except exceptions.NoSuchElementException as e:
                time.sleep(QUICK_WAIT_)

            if len(Table) == 0:
                # next round
                if len(Previous_round) != 0: 
                    Card_dealt = Card_dealt + Previous_round
                    Previous_round = []


            clear_output(wait=True)
            #display(Table)

            print("-------- Count -------------")

            #display(Card_dealt)
            display("Count :", Hi_Lo(Table, Card_dealt))
            threading.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()
            
         
