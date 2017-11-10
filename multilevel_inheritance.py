# -*- coding: utf-8 -*-
class Grandpa:
     def show(self):
         print("parent1")
class Parent(Grandpa):
     def show(self):
         print("parent2")
     def _protectedmemeber(self):
        print("printing protected member")

class Child(Parent):
     def show(self):
         print("parent3")

parobj=Grandpa()
parobj.show()
#parobj=Parent()
#parobj.show()
#parobj=Child()
#parobj.show()
ch=Child()
ch._protectedmemeber()

         
          