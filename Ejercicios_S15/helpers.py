# -*- coding: utf-8 -*-
"""

@author: maril
"""

import os

def gotoxy(x,y):
    print("%c[%d;%df"%(0x1B,y,x),end="")

def borrarPantalla():
    os.system("cls") 

def mensaje(msg,f,c):
    pass