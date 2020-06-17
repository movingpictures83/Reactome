import sys
import pypathway
from pypathway import PublicDatabase

class ReactomePlugin:
   def input(self, inputfile):
      self.query = inputfile[inputfile.rfind('/')+1:]

   def run(self):
      self.results = PublicDatabase.search_reactome(self.query)

   def output(self, outputfile):
      outfile = open(outputfile, 'w')
      for reaction in set(self.results):
         outfile.write("***************************************\n")
         outfile.write("DESCRIPTION: "+reaction.description+"\n")
         outfile.write("ORGANISMS: "+str(reaction.list_species())+"\n")
         outfile.write("***************************************\n")
