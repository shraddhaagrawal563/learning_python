# -*- coding: utf-8 -*-
class A_parent:
    def __init__(self):
        self._myvar=0
    def _printA(self):
        print("protected member of A")
        
        
class B_child(A_parent):
    def __init__(self):
        #call parent constructor
        A_parent.__init__(self)
        #super(B_child,self). __init__()
        self._myvar+=1
    def show(self):
        print("_myvar:",self._myvar)
        
ch=B_child()
print(ch._myvar)
ch.show()
ch._printA()
#use 1 underscore to declare protected member