#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 22:06:08 2023

@author: jacobeimont
"""

import random

def powerball():
  numbers = list(range(1, 69))
  draw = random.sample(numbers, 5)
  powerball = random.randint(1, 26)

  print("The numbers drawn are: ", draw)
  print("The Double Play is: ", powerball)

powerball()