#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("movies_.xml")
collection = DOMTree.documentElement

# Get all the movies in the collection
movies = collection.getElementsByTagName("movie")

# Print detail of each movie.
for movie in movies:
   print ("*****Movie*****")

   title = movie.getElementsByTagName('title')[0]
   print ("Title: %s" % title.childNodes[0].data)
   year = movie.getElementsByTagName('year')[0]
   print ("Year: %s" % year.childNodes[0].data)
   country = movie.getElementsByTagName('country')[0]
   print ("Country: %s" % country.childNodes[0].data)
   genre = movie.getElementsByTagName('genre')[0]
   print ("Genre: %s" % genre.childNodes[0].data)
   summary = movie.getElementsByTagName('summary')[0]
   print ("summary: %s" % summary.childNodes[0].data + "\n")

   if movie.getElementsByTagName("actor"):
      print ("*****Actor*****")
      last_name = movie.getElementsByTagName('last_name')[0]
      print ("Last Name: %s" % last_name.childNodes[0].data)
      first_name = movie.getElementsByTagName('first_name')[0]
      print ("First Name %s" % first_name.childNodes[0].data)
      birth_date = movie.getElementsByTagName('birth_date')[0]
      print ("Birth Date: %s" % birth_date.childNodes[0].data)
      role = movie.getElementsByTagName('role')[0]
      print ("Role: %s" % role.childNodes[0].data + "\n")

   if movie.getElementsByTagName("director"):
      print ("*****Director*****")
      last_name = movie.getElementsByTagName('last_name')[0]
      print ("Last Name: %s" % last_name.childNodes[0].data)
      first_name = movie.getElementsByTagName('first_name')[0]
      print ("First Name %s" % first_name.childNodes[0].data)
      birth_date = movie.getElementsByTagName('birth_date')[0]
      print ("Birth Date: %s" % birth_date.childNodes[0].data + "\n")
   
   