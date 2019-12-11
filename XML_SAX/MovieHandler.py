#!/usr/bin/python

import xml.sax

class MovieHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.title = ""
      self.year = ""
      self.country = ""
      self.genre = ""
      self.summary = ""
      self.director = ""
      self.last_name = ""
      self.first_name = ""
      self.birth_date = ""
      self.role = ""

   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "movie":
         print ("\n*****Movie*****")
      elif tag == "director":
         print ("\n*****Directors*****")
      elif tag == "actor":
         print ("\n*****Actor*****")

   # Call when an elements ends
   def endElement(self, tag):
      if self.CurrentData == "title":
         print ("Title:", self.title)
      elif self.CurrentData == "year":
         print ("Year:", self.year)
      elif self.CurrentData == "country":
         print ("Country:", self.country)
      elif self.CurrentData == "genre":
         print ("Genre:", self.genre)
      elif self.CurrentData == "summary":
         print ("Summary:", self.summary)
      elif self.CurrentData == "director":
         print ("Director:", self.director)
      elif self.CurrentData == "last_name":
         print ("Last Name:", self.last_name)
      elif self.CurrentData == "first_name":
         print ("First Name:", self.first_name)
      elif self.CurrentData == "birth_date":
         print ("Birth Date:", self.birth_date)
      elif self.CurrentData == "role":
         print ("Role:", self.role)
      self.CurrentData = ""

   # Call when a character is read
   def characters(self, content):
      if self.CurrentData == "title":
         self.title = content
      elif self.CurrentData == "year":
         self.year = content
      elif self.CurrentData == "country":
         self.country = content
      elif self.CurrentData == "genre":
         self.genre = content
      elif self.CurrentData == "summary":
         self.summary = content
      elif self.CurrentData == "director":
         self.director = content
      elif self.CurrentData == "last_name":
         self.last_name = content
      elif self.CurrentData == "first_name":
         self.first_name = content
      elif self.CurrentData == "birth_date":
         self.birth_date = content
      elif self.CurrentData == "role":
         self.role = content
  
if ( __name__ == "__main__"):
   
   # create an XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = MovieHandler()
   parser.setContentHandler( Handler )
   
   parser.parse("movies_.xml")