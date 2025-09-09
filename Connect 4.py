#Connect 4

#Importing all the necessary modules and libraries

import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

#Defining the variables for winning

P1_wins=0
P2_wins=0

#Defing the functions for each button

def start():
    global chance
    Startbtn['state']='disabled'
    Clearbtn['state']='normal'
    Playagainbtn['state']='normal'
    GameOverbtn['state']='normal'
    btn1['state']='normal'
    btn2['state']='normal'
    btn3['state']='normal'
    btn4['state']='normal'
    btn5['state']='normal'
    btn6['state']='normal'
    btn7['state']='normal'

    chance=1

def gameover():
    game.destroy
    if P1_wins>P2_wins:
        messagebox.showinfo('Connect 4','Player 1 wins')
    elif P2_wins>P1_wins:
        messagebox.showinfo('Connect 4','Player 2 wins')
    else:
        messagebox.showinfo('Connect 4','It is a Tie')
    
def clear():
    btn1['bg']='white'
    btn1['state']='normal'
    btn2['bg']='white'
    btn2['state']='normal'
    btn3['bg']='white'
    btn3['state']='normal'
    btn4['bg']='white'
    btn4['state']='normal'
    btn5['bg']='white'
    btn5['state']='normal'
    btn6['bg']='white'
    btn6['state']='normal'
    btn7['bg']='white'
    btn7['state']='normal'
    btn8['bg']='white'
    btn8['state']='disabled'
    btn9['bg']='white'
    btn9['state']='disabled'
    btn10['bg']='white'
    btn10['state']='disabled'
    btn11['bg']='white'
    btn11['state']='disabled'
    btn12['bg']='white'
    btn12['state']='disabled'
    btn13['bg']='white'
    btn13['state']='disabled'
    btn14['bg']='white'
    btn14['state']='disabled'
    btn15['bg']='white'
    btn15['state']='disabled'
    btn16['bg']='white'
    btn16['state']='disabled'
    btn17['bg']='white'
    btn17['state']='disabled'
    btn18['bg']='white'
    btn18['state']='disabled'
    btn19['bg']='white'
    btn19['state']='disabled'
    btn20['bg']='white'
    btn20['state']='disabled'
    btn21['bg']='white'
    btn21['state']='disabled'
    btn22['bg']='white'
    btn22['state']='disabled'
    btn23['bg']='white'
    btn23['state']='disabled'
    btn24['bg']='white'
    btn24['state']='disabled'
    btn25['bg']='white'
    btn25['state']='disabled'
    btn26['bg']='white'
    btn26['state']='disabled'
    btn27['bg']='white'
    btn27['state']='disabled'
    btn28['bg']='white'
    btn28['state']='disabled'
    btn29['bg']='white'
    btn29['state']='disabled'
    btn30['bg']='white'
    btn30['state']='disabled'
    btn31['bg']='white'
    btn31['state']='disabled'
    btn32['bg']='white'
    btn32['state']='disabled'
    btn33['bg']='white'
    btn33['state']='disabled'
    btn34['bg']='white'
    btn34['state']='disabled'
    btn35['bg']='white'
    btn35['state']='disabled'
    btn36['bg']='white'
    btn36['state']='disabled'
    btn37['bg']='white'
    btn37['state']='disabled'
    btn38['bg']='white'
    btn38['state']='disabled'
    btn39['bg']='white'
    btn39['state']='disabled'
    btn40['bg']='white'
    btn40['state']='disabled'
    btn41['bg']='white'
    btn41['state']='disabled'
    btn42['bg']='white'
    btn42['state']='disabled'

def playagain():
    btn1['bg']='white'
    btn1['state']='normal'
    btn2['bg']='white'
    btn2['state']='normal'
    btn3['bg']='white'
    btn3['state']='normal'
    btn4['bg']='white'
    btn4['state']='normal'
    btn5['bg']='white'
    btn5['state']='normal'
    btn6['bg']='white'
    btn6['state']='normal'
    btn7['bg']='white'
    btn7['state']='normal'
    btn8['bg']='white'
    btn8['state']='disabled'
    btn9['bg']='white'
    btn9['state']='disabled'
    btn10['bg']='white'
    btn10['state']='disabled'
    btn11['bg']='white'
    btn11['state']='disabled'
    btn12['bg']='white'
    btn12['state']='disabled'
    btn13['bg']='white'
    btn13['state']='disabled'
    btn14['bg']='white'
    btn14['state']='disabled'
    btn15['bg']='white'
    btn15['state']='disabled'
    btn16['bg']='white'
    btn16['state']='disabled'
    btn17['bg']='white'
    btn17['state']='disabled'
    btn18['bg']='white'
    btn18['state']='disabled'
    btn19['bg']='white'
    btn19['state']='disabled'
    btn20['bg']='white'
    btn20['state']='disabled'
    btn21['bg']='white'
    btn21['state']='disabled'
    btn22['bg']='white'
    btn22['state']='disabled'
    btn23['bg']='white'
    btn23['state']='disabled'
    btn24['bg']='white'
    btn24['state']='disabled'
    btn25['bg']='white'
    btn25['state']='disabled'
    btn26['bg']='white'
    btn26['state']='disabled'
    btn27['bg']='white'
    btn27['state']='disabled'
    btn28['bg']='white'
    btn28['state']='disabled'
    btn29['bg']='white'
    btn29['state']='disabled'
    btn30['bg']='white'
    btn30['state']='disabled'
    btn31['bg']='white'
    btn31['state']='disabled'
    btn32['bg']='white'
    btn32['state']='disabled'
    btn33['bg']='white'
    btn33['state']='disabled'
    btn34['bg']='white'
    btn34['state']='disabled'
    btn35['bg']='white'
    btn35['state']='disabled'
    btn36['bg']='white'
    btn36['state']='disabled'
    btn37['bg']='white'
    btn37['state']='disabled'
    btn38['bg']='white'
    btn38['state']='disabled'
    btn39['bg']='white'
    btn39['state']='disabled'
    btn40['bg']='white'
    btn40['state']='disabled'
    btn41['bg']='white'
    btn41['state']='disabled'
    btn42['bg']='white'
    btn42['state']='disabled'

#Defining the functions for coin slots

def btn1_F():
    global chance
    btn1['state']='disabled'
    btn8['state']='normal'
    if chance==1:
        btn1['bg']='red'
        chance=2
    elif chance==2:
        btn1['bg']='yellow'
        chance=1
    winning()

def btn2_F():
    global chance
    btn2['state']='disabled'
    btn9['state']='normal'
    if chance==1:
        btn2['bg']='red'
        chance=2
    elif chance==2:
        btn2['bg']='yellow'
        chance=1
    winning()
    
def btn3_F():
    global chance
    btn3['state']='disabled'
    btn10['state']='normal'
    if chance==1:
        btn3['bg']='red'
        chance=2
    elif chance==2:
        btn3['bg']='yellow'
        chance=1
    winning()

def btn4_F():
    global chance
    btn4['state']='disabled'
    btn11['state']='normal'
    if chance==1:
        btn4['bg']='red'
        chance=2
    elif chance==2:
        btn4['bg']='yellow'
        chance=1
    winning()

def btn5_F():
    global chance
    btn5['state']='disabled'
    btn12['state']='normal'
    if chance==1:
        btn5['bg']='red'
        chance=2
    elif chance==2:
        btn5['bg']='yellow'
        chance=1
    winning()

def btn6_F():
    global chance
    btn6['state']='disabled'
    btn13['state']='normal'
    if chance==1:
        btn6['bg']='red'
        chance=2
    elif chance==2:
        btn6['bg']='yellow'
        chance=1
    winning()
    

def btn7_F():
    global chance
    btn7['state']='disabled'
    btn14['state']='normal'
    if chance==1:
        btn7['bg']='red'
        chance=2
    elif chance==2:
        btn7['bg']='yellow'
        chance=1
    winning()

def btn8_F():
    global chance
    btn8['state']='disabled'
    btn15['state']='normal'
    if chance==1:
        btn8['bg']='red'
        chance=2
    elif chance==2:
        btn8['bg']='yellow'
        chance=1
    winning()

def btn9_F():
    global chance
    btn9['state']='disabled'
    btn16['state']='normal'
    if chance==1:
        btn9['bg']='red'
        chance=2
    elif chance==2:
        btn9['bg']='yellow'
        chance=1
    winning()
    
def btn10_F():
    global chance
    btn10['state']='disabled'
    btn17['state']='normal'
    if chance==1:
        btn10['bg']='red'
        chance=2
    elif chance==2:
        btn10['bg']='yellow'
        chance=1
    winning()

def btn11_F():
    global chance
    btn11['state']='disabled'
    btn18['state']='normal'
    if chance==1:
        btn11['bg']='red'
        chance=2
    elif chance==2:
        btn11['bg']='yellow'
        chance=1
    winning()

def btn12_F():
    global chance
    btn12['state']='disabled'
    btn19['state']='normal'
    if chance==1:
        btn12['bg']='red'
        chance=2
    elif chance==2:
        btn12['bg']='yellow'
        chance=1
    winning()

def btn13_F():
    global chance
    btn13['state']='disabled'
    btn20['state']='normal'
    if chance==1:
        btn13['bg']='red'
        chance=2
    elif chance==2:
        btn13['bg']='yellow'
        chance=1
    winning()

def btn14_F():
    global chance
    btn14['state']='disabled'
    btn21['state']='normal'
    if chance==1:
        btn14['bg']='red'
        chance=2
    elif chance==2:
        btn14['bg']='yellow'
        chance=1
    winning()

def btn15_F():
    global chance
    btn15['state']='disabled'
    btn22['state']='normal'
    if chance==1:
        btn15['bg']='red'
        chance=2
    elif chance==2:
        btn15['bg']='yellow'
        chance=1
    winning()

def btn16_F():
    global chance
    btn16['state']='disabled'
    btn23['state']='normal'
    if chance==1:
        btn16['bg']='red'
        chance=2
    elif chance==2:
        btn16['bg']='yellow'
        chance=1
    winning()
    
def btn17_F():
    global chance
    btn17['state']='disabled'
    btn24['state']='normal'
    if chance==1:
        btn17['bg']='red'
        chance=2
    elif chance==2:
        btn17['bg']='yellow'
        chance=1
    winning()

def btn18_F():
    global chance
    btn18['state']='disabled'
    btn25['state']='normal'
    if chance==1:
        btn18['bg']='red'
        chance=2
    elif chance==2:
        btn18['bg']='yellow'
        chance=1
    winning()

def btn19_F():
    global chance
    btn19['state']='disabled'
    btn26['state']='normal'
    if chance==1:
        btn19['bg']='red'
        chance=2
    elif chance==2:
        btn19['bg']='yellow'
        chance=1
    winning()

def btn20_F():
    global chance
    btn20['state']='disabled'
    btn27['state']='normal'
    if chance==1:
        btn20['bg']='red'
        chance=2
    elif chance==2:
        btn20['bg']='yellow'
        chance=1
    winning()

def btn21_F():
    global chance
    btn21['state']='disabled'
    btn28['state']='normal'
    if chance==1:
        btn21['bg']='red'
        chance=2
    elif chance==2:
        btn21['bg']='yellow'
        chance=1
    winning()

def btn22_F():
    global chance
    btn22['state']='disabled'
    btn29['state']='normal'
    if chance==1:
        btn22['bg']='red'
        chance=2
    elif chance==2:
        btn22['bg']='yellow'
        chance=1
    winning()

def btn23_F():
    global chance
    btn23['state']='disabled'
    btn30['state']='normal'
    if chance==1:
        btn23['bg']='red'
        chance=2
    elif chance==2:
        btn23['bg']='yellow'
        chance=1
    winning()
    
def btn24_F():
    global chance
    btn24['state']='disabled'
    btn31['state']='normal'
    if chance==1:
        btn24['bg']='red'
        chance=2
    elif chance==2:
        btn24['bg']='yellow'
        chance=1
    winning()

def btn25_F():
    global chance
    btn25['state']='disabled'
    btn32['state']='normal'
    if chance==1:
        btn25['bg']='red'
        chance=2
    elif chance==2:
        btn25['bg']='yellow'
        chance=1
    winning()

def btn26_F():
    global chance
    btn26['state']='disabled'
    btn33['state']='normal'
    if chance==1:
        btn26['bg']='red'
        chance=2
    elif chance==2:
        btn26['bg']='yellow'
        chance=1
    winning()

def btn27_F():
    global chance
    btn27['state']='disabled'
    btn34['state']='normal'
    if chance==1:
        btn27['bg']='red'
        chance=2
    elif chance==2:
        btn27['bg']='yellow'
        chance=1
    winning()

def btn28_F():
    global chance
    btn28['state']='disabled'
    btn35['state']='normal'
    if chance==1:
        btn28['bg']='red'
        chance=2
    elif chance==2:
        btn28['bg']='yellow'
        chance=1
    winning()

def btn29_F():
    global chance
    btn29['state']='disabled'
    btn36['state']='normal'
    if chance==1:
        btn29['bg']='red'
        chance=2
    elif chance==2:
        btn29['bg']='yellow'
        chance=1
    winning()

def btn30_F():
    global chance
    btn30['state']='disabled'
    btn37['state']='normal'
    if chance==1:
        btn30['bg']='red'
        chance=2
    elif chance==2:
        btn30['bg']='yellow'
        chance=1
    winning()
    
def btn31_F():
    global chance
    btn31['state']='disabled'
    btn38['state']='normal'
    if chance==1:
        btn31['bg']='red'
        chance=2
    elif chance==2:
        btn31['bg']='yellow'
        chance=1
    winning()

def btn32_F():
    global chance
    btn32['state']='disabled'
    btn39['state']='normal'
    if chance==1:
        btn32['bg']='red'
        chance=2
    elif chance==2:
        btn32['bg']='yellow'
        chance=1
    winning()

def btn33_F():
    global chance
    btn33['state']='disabled'
    btn40['state']='normal'
    if chance==1:
        btn33['bg']='red'
        chance=2
    elif chance==2:
        btn33['bg']='yellow'
        chance=1
    winning()

def btn34_F():
    global chance
    btn34['state']='disabled'
    btn41['state']='normal'
    if chance==1:
        btn34['bg']='red'
        chance=2
    elif chance==2:
        btn34['bg']='yellow'
        chance=1
    winning()

def btn35_F():
    global chance
    btn35['state']='disabled'
    btn42['state']='normal'
    if chance==1:
        btn35['bg']='red'
        chance=2
    elif chance==2:
        btn35['bg']='yellow'
        chance=1
    winning()

def btn36_F():
    global chance
    btn36['state']='disabled'
    if chance==1:
        btn36['bg']='red'
        chance=2
    elif chance==2:
        btn36['bg']='yellow'
        chance=1
    winning()

def btn37_F():
    global chance
    btn37['state']='disabled'
    if chance==1:
        btn37['bg']='red'
        chance=2
    elif chance==2:
        btn37['bg']='yellow'
        chance=1
    winning()
    
def btn38_F():
    global chance
    btn38['state']='disabled'
    if chance==1:
        btn38['bg']='red'
        chance=2
    elif chance==2:
        btn38['bg']='yellow'
        chance=1
    winning()

def btn39_F():
    global chance
    btn39['state']='disabled'
    if chance==1:
        btn39['bg']='red'
        chance=2
    elif chance==2:
        btn39['bg']='yellow'
        chance=1
    winning()

def btn40_F():
    global chance
    btn40['state']='disabled'
    if chance==1:
        btn40['bg']='red'
        chance=2
    elif chance==2:
        btn40['bg']='yellow'
        chance=1
    winning()

def btn41_F():
    global chance
    btn41['state']='disabled'
    if chance==1:
        btn41['bg']='red'
        chance=2
    elif chance==2:
        btn41['bg']='yellow'
        chance=1
    winning()

def btn42_F():
    global chance
    btn42['state']='disabled'
    if chance==1:
        btn42['bg']='red'
        chance=2
    elif chance==2:
        btn42['bg']='yellow'
        chance=1
    winning()

#Defining the Win function

def winning():
    global P1_wins
    global P2_wins
    Playerwin=0
    if btn1['bg']==btn2['bg']==btn3['bg']==btn4['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn5['bg']==btn2['bg']==btn3['bg']==btn4['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn5['bg']==btn6['bg']==btn3['bg']==btn4['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn5['bg']==btn6['bg']==btn7['bg']==btn4['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn8['bg']==btn9['bg']==btn10['bg']==btn11['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn12['bg']==btn9['bg']==btn10['bg']==btn11['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn12['bg']==btn13['bg']==btn10['bg']==btn11['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn12['bg']==btn13['bg']==btn14['bg']==btn11['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn15['bg']==btn16['bg']==btn17['bg']==btn18['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn19['bg']==btn16['bg']==btn17['bg']==btn18['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn19['bg']==btn20['bg']==btn17['bg']==btn18['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn19['bg']==btn20['bg']==btn21['bg']==btn18['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn22['bg']==btn23['bg']==btn24['bg']==btn25['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn26['bg']==btn23['bg']==btn24['bg']==btn25['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn26['bg']==btn27['bg']==btn24['bg']==btn25['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn26['bg']==btn27['bg']==btn28['bg']==btn25['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn29['bg']==btn30['bg']==btn31['bg']==btn32['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn33['bg']==btn30['bg']==btn31['bg']==btn32['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn33['bg']==btn34['bg']==btn31['bg']==btn32['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn33['bg']==btn34['bg']==btn35['bg']==btn32['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn36['bg']==btn37['bg']==btn38['bg']==btn39['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn40['bg']==btn37['bg']==btn38['bg']==btn39['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn40['bg']==btn41['bg']==btn38['bg']==btn39['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn40['bg']==btn41['bg']==btn42['bg']==btn39['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1


    elif btn1['bg']==btn8['bg']==btn15['bg']==btn22['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn29['bg']==btn8['bg']==btn15['bg']==btn22['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn29['bg']==btn36['bg']==btn15['bg']==btn22['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn2['bg']==btn9['bg']==btn16['bg']==btn23['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn30['bg']==btn9['bg']==btn16['bg']==btn23['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn30['bg']==btn37['bg']==btn16['bg']==btn23['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn3['bg']==btn10['bg']==btn17['bg']==btn24['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn31['bg']==btn10['bg']==btn17['bg']==btn24['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn31['bg']==btn38['bg']==btn17['bg']==btn24['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn4['bg']==btn11['bg']==btn18['bg']==btn25['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn32['bg']==btn11['bg']==btn18['bg']==btn25['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn32['bg']==btn39['bg']==btn18['bg']==btn25['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn5['bg']==btn12['bg']==btn19['bg']==btn26['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn33['bg']==btn12['bg']==btn19['bg']==btn26['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn33['bg']==btn40['bg']==btn19['bg']==btn26['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn6['bg']==btn13['bg']==btn20['bg']==btn27['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn34['bg']==btn13['bg']==btn20['bg']==btn27['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn34['bg']==btn41['bg']==btn20['bg']==btn27['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn7['bg']==btn14['bg']==btn21['bg']==btn28['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn35['bg']==btn14['bg']==btn21['bg']==btn28['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn35['bg']==btn42['bg']==btn21['bg']==btn28['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1

    elif btn1['bg']==btn9['bg']==btn17['bg']==btn25['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn33['bg']==btn9['bg']==btn17['bg']==btn25['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn33['bg']==btn41['bg']==btn17['bg']==btn25['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn2['bg']==btn10['bg']==btn18['bg']==btn26['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn34['bg']==btn10['bg']==btn18['bg']==btn26['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn34['bg']==btn42['bg']==btn18['bg']==btn26['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn3['bg']==btn11['bg']==btn19['bg']==btn27['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn35['bg']==btn11['bg']==btn19['bg']==btn27['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn4['bg']==btn12['bg']==btn20['bg']==btn28['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn8['bg']==btn16['bg']==btn24['bg']==btn32['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn40['bg']==btn16['bg']==btn24['bg']==btn32['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn15['bg']==btn23['bg']==btn31['bg']==btn39['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1

    elif btn7['bg']==btn13['bg']==btn19['bg']==btn25['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn31['bg']==btn13['bg']==btn19['bg']==btn25['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn31['bg']==btn37['bg']==btn19['bg']==btn25['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn6['bg']==btn12['bg']==btn18['bg']==btn24['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn30['bg']==btn12['bg']==btn18['bg']==btn24['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn30['bg']==btn36['bg']==btn18['bg']==btn24['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn5['bg']==btn11['bg']==btn17['bg']==btn23['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn29['bg']==btn11['bg']==btn17['bg']==btn23['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn4['bg']==btn10['bg']==btn16['bg']==btn22['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn14['bg']==btn20['bg']==btn26['bg']==btn32['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn38['bg']==btn20['bg']==btn26['bg']==btn32['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1
    elif btn21['bg']==btn27['bg']==btn33['bg']==btn39['bg']=='red':
        P1_wins+=1
        Player1_L2['text']=P1_wins
        Playerwin=1

    

    elif btn1['bg']==btn2['bg']==btn3['bg']==btn4['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn5['bg']==btn2['bg']==btn3['bg']==btn4['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn5['bg']==btn6['bg']==btn3['bg']==btn4['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn5['bg']==btn6['bg']==btn7['bg']==btn4['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn8['bg']==btn9['bg']==btn10['bg']==btn11['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn12['bg']==btn9['bg']==btn10['bg']==btn11['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn12['bg']==btn13['bg']==btn10['bg']==btn11['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn12['bg']==btn13['bg']==btn14['bg']==btn11['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn15['bg']==btn16['bg']==btn17['bg']==btn18['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn19['bg']==btn16['bg']==btn17['bg']==btn18['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn19['bg']==btn20['bg']==btn17['bg']==btn18['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn19['bg']==btn20['bg']==btn21['bg']==btn18['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn22['bg']==btn23['bg']==btn24['bg']==btn25['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn26['bg']==btn23['bg']==btn24['bg']==btn25['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn26['bg']==btn27['bg']==btn24['bg']==btn25['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn26['bg']==btn27['bg']==btn28['bg']==btn25['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn29['bg']==btn30['bg']==btn31['bg']==btn32['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn33['bg']==btn30['bg']==btn31['bg']==btn32['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn33['bg']==btn34['bg']==btn31['bg']==btn32['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn33['bg']==btn34['bg']==btn35['bg']==btn32['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn36['bg']==btn37['bg']==btn38['bg']==btn39['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn40['bg']==btn37['bg']==btn38['bg']==btn39['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn40['bg']==btn41['bg']==btn38['bg']==btn39['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn40['bg']==btn41['bg']==btn42['bg']==btn39['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1


    elif btn1['bg']==btn8['bg']==btn15['bg']==btn22['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn29['bg']==btn8['bg']==btn15['bg']==btn22['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn29['bg']==btn36['bg']==btn15['bg']==btn22['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn2['bg']==btn9['bg']==btn16['bg']==btn23['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn30['bg']==btn9['bg']==btn16['bg']==btn23['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn30['bg']==btn37['bg']==btn16['bg']==btn23['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn3['bg']==btn10['bg']==btn17['bg']==btn24['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn31['bg']==btn10['bg']==btn17['bg']==btn24['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn31['bg']==btn38['bg']==btn17['bg']==btn24['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn4['bg']==btn11['bg']==btn18['bg']==btn25['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn32['bg']==btn11['bg']==btn18['bg']==btn25['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn32['bg']==btn39['bg']==btn18['bg']==btn25['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn5['bg']==btn12['bg']==btn19['bg']==btn26['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn33['bg']==btn12['bg']==btn19['bg']==btn26['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn33['bg']==btn40['bg']==btn19['bg']==btn26['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn6['bg']==btn13['bg']==btn20['bg']==btn27['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn34['bg']==btn13['bg']==btn20['bg']==btn27['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn34['bg']==btn41['bg']==btn20['bg']==btn27['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn7['bg']==btn14['bg']==btn21['bg']==btn28['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn35['bg']==btn14['bg']==btn21['bg']==btn28['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn35['bg']==btn42['bg']==btn21['bg']==btn28['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1

    elif btn1['bg']==btn9['bg']==btn17['bg']==btn25['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn33['bg']==btn9['bg']==btn17['bg']==btn25['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn33['bg']==btn41['bg']==btn17['bg']==btn25['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn2['bg']==btn10['bg']==btn18['bg']==btn26['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn34['bg']==btn10['bg']==btn18['bg']==btn26['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn34['bg']==btn42['bg']==btn18['bg']==btn26['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn3['bg']==btn11['bg']==btn19['bg']==btn27['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn35['bg']==btn11['bg']==btn19['bg']==btn27['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn4['bg']==btn12['bg']==btn20['bg']==btn28['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn8['bg']==btn16['bg']==btn24['bg']==btn32['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn40['bg']==btn16['bg']==btn24['bg']==btn32['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn15['bg']==btn23['bg']==btn31['bg']==btn39['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1

    elif btn7['bg']==btn13['bg']==btn19['bg']==btn25['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn31['bg']==btn13['bg']==btn19['bg']==btn25['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn31['bg']==btn37['bg']==btn19['bg']==btn25['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn6['bg']==btn12['bg']==btn18['bg']==btn24['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn30['bg']==btn12['bg']==btn18['bg']==btn24['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn30['bg']==btn36['bg']==btn18['bg']==btn24['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn5['bg']==btn11['bg']==btn17['bg']==btn23['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn29['bg']==btn11['bg']==btn17['bg']==btn23['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn4['bg']==btn10['bg']==btn16['bg']==btn22['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn14['bg']==btn20['bg']==btn26['bg']==btn32['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn38['bg']==btn20['bg']==btn26['bg']==btn32['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1
    elif btn21['bg']==btn27['bg']==btn33['bg']==btn39['bg']=='yellow':
        P2_wins+=1
        Player2_L2['text']=P2_wins
        Playerwin=1

    if Playerwin==1:
        btn1['state']='disabled'
        btn2['state']='disabled'
        btn3['state']='disabled'
        btn4['state']='disabled'
        btn5['state']='disabled'
        btn6['state']='disabled'
        btn7['state']='disabled'
        btn8['state']='disabled'
        btn9['state']='disabled'
        btn10['state']='disabled'
        btn11['state']='disabled'
        btn12['state']='disabled'
        btn13['state']='disabled'
        btn14['state']='disabled'
        btn15['state']='disabled'
        btn16['state']='disabled'
        btn17['state']='disabled'
        btn18['state']='disabled'
        btn19['state']='disabled'
        btn20['state']='disabled'
        btn21['state']='disabled'
        btn22['state']='disabled'
        btn23['state']='disabled'
        btn24['state']='disabled'
        btn25['state']='disabled'
        btn26['state']='disabled'
        btn27['state']='disabled'
        btn28['state']='disabled'
        btn29['state']='disabled'
        btn30['state']='disabled'
        btn31['state']='disabled'
        btn32['state']='disabled'
        btn33['state']='disabled'
        btn34['state']='disabled'
        btn35['state']='disabled'
        btn36['state']='disabled'
        btn37['state']='disabled'
        btn38['state']='disabled'
        btn39['state']='disabled'
        btn40['state']='disabled'
        btn41['state']='disabled'
        btn42['state']='disabled'

#Setting up the tkinter window for the game

game= Tk()
game.title("Connect 4")
game.geometry('1400x800')
game.resizable(0,0)

canvas= Canvas(game,width=1400,height=800)
canvas.pack()

#Creating the game atmosphere

background= (Image.open('Background.png'))
resphoto1=background.resize((1350,750),Image.LANCZOS)
newimage1=ImageTk.PhotoImage(resphoto1)
canvas.create_image(700,400, image=newimage1)

GameBoard= (Image.open("Game Board.png"))
resphoto2=GameBoard.resize((900,650),Image.LANCZOS)
newimage2=ImageTk.PhotoImage(resphoto2)
canvas.create_image(850,400, image=newimage2)

#Creating the required labels

Title= tk.Label(game, text='CONNECT 4', font=('Helvetiva',35,'bold'),fg='White',bg='Brown')
Title.place(x=700,y= 15)

canvas.create_line(300, 50, 300, 750, fill="white", width=6)

Player1= (Image.open("red coin.png"))
resphoto3=Player1.resize((120,100),Image.LANCZOS)
newimage3=ImageTk.PhotoImage(resphoto3)

Player1_L= tk.Label(game, image=newimage3,width=100)
Player1_L.place(x=175,y=100)

Player1_L1= tk.Label(game, text='Player 1',font=('Helvetiva',25,'bold'),fg='White',bg='Brown')
Player1_L1.place(x=40,y=125)

Player1_L2= tk.Label(game, text=P1_wins,font=('Helvetiva',25,'bold'))
Player1_L2.place(x=40,y=190)

Player2= (Image.open("yellow coin.png"))
resphoto4=Player2.resize((120,110),Image.LANCZOS)
newimage4=ImageTk.PhotoImage(resphoto4)

Player2_L= tk.Label(game, image=newimage4,width=100)
Player2_L.place(x=175,y=500)

Player2_L1= tk.Label(game, text='Player 2',font=('Helvetiva',25,'bold'),fg='White',bg='Brown')
Player2_L1.place(x=40,y=535)

Player2_L2= tk.Label(game, text=P2_wins,font=('Helvetiva',25,'bold'))
Player2_L2.place(x=40,y=600)

#Creating the buttons

Startbtn= Button(game, text='Start',width=5,state='normal',font=('Helvetiva',15,'bold'),command=start)
Startbtn.place(x=50,y=350)

Clearbtn= Button(game, text='Clear',state='disabled',width=5,font=('Helvetiva',15,'bold'),command=clear)
Clearbtn.place(x=200,y=350)

Playagainbtn= Button(game, text='Play Again',state='disabled',width=8,font=('Helvetiva',15,'bold'),command=playagain)
Playagainbtn.place(x=50,y=400)

GameOverbtn= Button(game, text='Game Over',state='disabled',width=9,font=('Helvetiva',15,'bold'),command=gameover)
GameOverbtn.place(x=175,y=400)

#Creating all the coin slots 

btn1= Button(game,width=11,state='disabled',height=4,command=btn1_F)
btn1.place(x=425,y=640)

btn2= Button(game,width=11,state='disabled',height=4,command=btn2_F)
btn2.place(x=550,y=640)

btn3= Button(game,width=11,state='disabled',height=4,command=btn3_F)
btn3.place(x=675,y=640)

btn4= Button(game,width=11,state='disabled',height=4,command=btn4_F)
btn4.place(x=800,y=640)

btn5= Button(game,width=11,state='disabled',height=4,command=btn5_F)
btn5.place(x=925,y=640)

btn6= Button(game,width=11,state='disabled',height=4,command=btn6_F)
btn6.place(x=1050,y=640)

btn7= Button(game,width=11,state='disabled',height=4,command=btn7_F)
btn7.place(x=1175,y=640)

btn8= Button(game,width=11,state='disabled',height=4,command=btn8_F)
btn8.place(x=425,y=532)

btn9= Button(game,width=11,state='disabled',height=4,command=btn9_F)
btn9.place(x=550,y=532)

btn10= Button(game,width=11,state='disabled',height=4,command=btn10_F)
btn10.place(x=675,y=532)

btn11= Button(game,width=11,state='disabled',height=4,command=btn11_F)
btn11.place(x=800,y=532)

btn12= Button(game,width=11,state='disabled',height=4,command=btn12_F)
btn12.place(x=925,y=532)

btn13= Button(game,width=11,state='disabled',height=4,command=btn13_F)
btn13.place(x=1050,y=532)

btn14= Button(game,width=11,state='disabled',height=4,command=btn14_F)
btn14.place(x=1175,y=532)

btn15= Button(game,width=11,state='disabled',height=4,command=btn15_F)
btn15.place(x=425,y=424)

btn16= Button(game,width=11,state='disabled',height=4,command=btn16_F)
btn16.place(x=550,y=424)

btn17= Button(game,width=11,state='disabled',height=4,command=btn17_F)
btn17.place(x=675,y=424)

btn18= Button(game,width=11,state='disabled',height=4,command=btn18_F)
btn18.place(x=800,y=424)

btn19= Button(game,width=11,state='disabled',height=4,command=btn19_F)
btn19.place(x=925,y=424)

btn20= Button(game,width=11,state='disabled',height=4,command=btn20_F)
btn20.place(x=1050,y=424)

btn21= Button(game,width=11,state='disabled',height=4,command=btn21_F)
btn21.place(x=1175,y=424)

btn22= Button(game,width=11,state='disabled',height=4,command=btn22_F)
btn22.place(x=425,y=316)

btn23= Button(game,width=11,state='disabled',height=4,command=btn23_F)
btn23.place(x=550,y=316)

btn24= Button(game,width=11,state='disabled',height=4,command=btn24_F)
btn24.place(x=675,y=316)

btn25= Button(game,width=11,state='disabled',height=4,command=btn25_F)
btn25.place(x=800,y=316)

btn26= Button(game,width=11,state='disabled',height=4,command=btn26_F)
btn26.place(x=925,y=316)

btn27= Button(game,width=11,state='disabled',height=4,command=btn27_F)
btn27.place(x=1050,y=316)

btn28= Button(game,width=11,state='disabled',height=4,command=btn28_F)
btn28.place(x=1175,y=316)

btn29= Button(game,width=11,state='disabled',height=4,command=btn29_F)
btn29.place(x=425,y=208)

btn30= Button(game,width=11,state='disabled',height=4,command=btn30_F)
btn30.place(x=550,y=208)

btn31= Button(game,width=11,state='disabled',height=4,command=btn31_F)
btn31.place(x=675,y=208)

btn32= Button(game,width=11,state='disabled',height=4,command=btn32_F)
btn32.place(x=800,y=208)

btn33= Button(game,width=11,state='disabled',height=4,command=btn33_F)
btn33.place(x=925,y=208)

btn34= Button(game,width=11,state='disabled',height=4,command=btn34_F)
btn34.place(x=1050,y=208)

btn35= Button(game,width=11,state='disabled',height=4,command=btn35_F)
btn35.place(x=1175,y=208)

btn36= Button(game,width=11,state='disabled',height=4,command=btn36_F)
btn36.place(x=425,y=100)

btn37= Button(game,width=11,state='disabled',height=4,command=btn37_F)
btn37.place(x=550,y=100)

btn38= Button(game,width=11,state='disabled',height=4,command=btn38_F)
btn38.place(x=675,y=100)

btn39= Button(game,width=11,state='disabled',height=4,command=btn39_F)
btn39.place(x=800,y=100)

btn40= Button(game,width=11,state='disabled',height=4,command=btn40_F)
btn40.place(x=925,y=100)

btn41= Button(game,width=11,state='disabled',height=4,command=btn41_F)
btn41.place(x=1050,y=100)

btn42= Button(game,width=11,state='disabled',height=4,command=btn42_F)
btn42.place(x=1175,y=100)

#Closing the tkinter window

game.mainloop()