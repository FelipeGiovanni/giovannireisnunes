#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from time import sleep
from sys import stdout

print("Este programa contará até 100.")

contador = 0
while contador < 100:
    print (".", end="")
    stdout.flush() # força a atualização da tela.
    contador += 1
    sleep(.03125) # espera 1/32 segundos.

print (" FIM!")
    
