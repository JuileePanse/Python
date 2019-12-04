#!/usr/bin/python

# AlienTest.py
from Alien import *
from Eye import *
from Nose import *
from Mouth import *
from Head import *
import sys, getopt

if __name__ == '__main__':

      eyeLeft1 = Eye(2)
      eyeRight1 = Eye(2)
      nose = Nose(3, 3, 2)
      mouth = Mouth(5, 2)
      
      eyeLeft2 = Eye(2)
      eyeRight2 = Eye(3)
      normalHead = Head(100, 4, eyeLeft1, eyeRight1, nose, mouth)
      abnormalHead = Head(100, 4, eyeLeft2, eyeRight2, nose, mouth)

      print("Normal Head", normalHead.toString())
      print("\n\nAbnormal Head", abnormalHead.toString())

      normalHead.getLeft().close()
      normalHead.getRight().close()
      normalHead.getMouth().close()

      if normalHead.headAche():
         print("\nHead Ache")
      else:
         print("\nNo Head Ache")