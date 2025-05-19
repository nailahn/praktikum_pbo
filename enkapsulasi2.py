# enkapsulasi dengan private access modifier
class pegawai:
    def __init__(self, nama, salary):
        self.nama=nama
        self.gaji=salary
        self.__gaji_final= self.gaji - (0.2 * self.gaji)

    def showGajiFinal(self):
        return self.__gaji_final

obj1=pegawai("Agus", 1000)
print(obj1.showGajiFinal())