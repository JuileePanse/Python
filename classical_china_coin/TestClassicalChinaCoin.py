#!/usr/bin/python

# TestClassicalChinaCoin.py
from ClassicalChinaCoin import *
from Square import *
from Metal import *
from AncientObject import *
import sys, getopt

def usage():
   print ('Usage: TestClassicalChinaCoin.py -h')
   print ('Usage: TestClassicalChinaCoin.py -r <radius> -s <side> -a <age> -m <material>')
   print ('Usage: TestClassicalChinaCoin.py --radius=<radius> --side=<side> --age=<age> --material <material>')

def main(argv):
   radius = ''
   side = ''
   age = ''
   material = ''
 
   try:
      opts, args = getopt.getopt(argv,"hr:s:a:m:",["radius=", "side=", "age=", "material="])
   except getopt.GetoptError:
      print("Error")
      usage()
      sys.exit(2)

   for opt, arg in opts:
      if opt == '-h':
         usage()
         sys.exit()
      elif opt in ("-r", "--radius"):
         radius = int(arg)
      elif opt in ("-s", "--side"):
         side = int(arg)
      elif opt in ("-a", "--age"):
         age = int(arg)
      elif opt in ("-m", "--material"):
         material = str(arg)
   
   square = Square(side)
   metal = Metal(material)
   ancientObject = AncientObject(age, metal)
   myCoin = ClassicalChinaCoin(radius, square, ancientObject)
   print(myCoin.toString())

   if myCoin.isValid():
      print("\nCoin is Valid")
   else:
      print("\nCoin is Invalid")

   square.setSide(2)
   metal.setMaterial("gold")
   ancientObject.setAge(700)
   ancientObject.setMetal(metal)
   myCoin.setRadius(5)
   myCoin.setSquare(square)
   myCoin.setAncientObject(ancientObject)

   print("\n" + myCoin.toString())

   ancientObject.destroy()
   print("\nCoin Destroyed\n\n" +myCoin.toString())

if __name__ == '__main__':
   main(sys.argv[1:])