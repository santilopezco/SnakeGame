class Animal:
    
    def _init_(self):   #Así construyo el constructor, con la variable def y el método sefl
        self.num_ojos = 2
        
    def respirar(self):
        print("Inhale, exhale")
        

class Pez(Animal):
    
    def _init_(self):
        super()._init_()  #super me ayuda a agregar el constructuro de Animal
    
    def respirar(self):
        super().respirar()
        print("glu glu")
        
    def nadar (self):
        print("Nadaremos nadaremos en el mar")
        
nemo = Pez()   # Le digo que nemo es un objeto de la clase Pez
    
    