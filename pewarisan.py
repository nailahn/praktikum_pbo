class A:
 def _init_(self):
   self ._a = 0
 def setA(self, a):
   self ._a = a
 def getA(self):
   return self._a

#mendefinisikan kelas anak	
class B(A):
 def _init_(self):
   self ._b = 0
 def setB(self, b):
   self ._b = b
 def getB(self):
   return self._b

#membuat objek
obj = B()

#memanggil method milik kelas induk
obj.setA(10)
print("Nilai a: %d" % obj.getA())

#memanggil method milik dirinya sendiri
obj.setB(20)
print("Nilai b: %d" % obj.getB())