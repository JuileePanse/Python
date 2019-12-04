#!/usr/bin/python

# TestMovie.py
from Animal import *
import sys, getopt

def usage():
   print ('Usage: TestMovie.py -h')
   print ('Usage: TestMovie.py -l <Legs>')
   print ('Usage: TestMovie.py --legs=<Legs>')

def main(argv):
   legs = ''

   try:
      opts, args = getopt.getopt(argv,"hl:",["legs="])
   except getopt.GetoptError:
      usage()
      sys.exit(2)

   for opt, arg in opts:
      if opt == '-h':
         usage()
         sys.exit()
      elif opt in ("-l", "--legs"):
         legs = arg

   po = Animal(int(legs))
   print (po.toString())
   po.removeLegs(1)
   if po.isDisable():
      print ("Po is Disabled")
   else:
      print ("Po is not Disabled")

if __name__ == "__main__":
   main(sys.argv[1:])