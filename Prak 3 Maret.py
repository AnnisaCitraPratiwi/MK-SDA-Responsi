# -*- coding: utf-8 -*-
"""Prak 3 maret.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fG7I7pHj_2MCrT9kOxGiYh8UpHVDmiNr

#PRAK SDA 3 MARET 2023
"""

class Bunga :
  a = "Bunga Bangkai"
  b = "Bunga Tulip"
  c = "Bunga Mawar"
  d = "Bunga Melati"
  e = "Bunga Anggrek"

#base kelas itu bunga
#mawar tulip dsb itu anak kelas

bunga1 = Bunga()
print(bunga1.a)
print(bunga1.b)
print(bunga1.c)
print(bunga1.d)
print(bunga1.e)

class Person :
  #itu adalah parent class nya
  def __init__ (self,name,idNumber,salary) :
    #yang di dalam kurung itu parameter yg dibutuhin 
    self.name = name
    self.idNumber = idNumber
    self.salary = salary

  def display(self) :
    #ini buat nampilih karena manggil nama sama idNumber
    print(self.name)
    print(self.idNumber)
    print(self.salary)

class Employee(Person) :
  def __init__(self,name,idNumber,salary) :
    self.salary = salary

    Person. __init__(self,name,idNumber,salary)
a = Employee('Zidan',2157,200000 )
a.display()

class Person :
  #itu adalah parent class nya
  def __init__ (self,name,idNumber,salary) :
    #yang di dalam kurung itu parameter yg dibutuhin 
    self.name = name
    self.idNumber = idNumber
    self.salary = salary

  def display(self) :
    #ini buat nampilih karena manggil nama sama idNumber
    print("Nama      : ", self.name)
    print("Id Number : ", self.idNumber)
    print("Gaji      : ", self.salary)

class Employee(Person) :
  def __init__(self,name,idNumber,salary) :
    self.salary = salary

    Person.__init__(self,name,idNumber,salary)
a = Employee('Zidan',2157,200000 )
b = Employee ('Annisa', 2158,300000)
a.display()
print()
b.display()