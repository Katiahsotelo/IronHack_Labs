
import random as random


# Soldier

class Soldier:
    
    def __init__(self, health, strength):
        self.h= health
        self.s=strength  
 
    def attack(self):
        return self.s
    
    def receive_damage(self,damage):
        self.h = self.h - damage 
        #return self.h
           
    pass

# Viking


class Viking(Soldier):
    
    def __init__(self,name,health,strength):
        super().__init__(health,strength) # esta funcion es para hacer inherit en clases 
        #Soldier.__init__(self,health,strength)
        self.n = name
       

    def receive_damage(self,damage):
            self.h= self.h - damage
            if self.h > 0:
                return f'{self.n} has recieved {damage} points of damage'
            else:
                  return f'{self.n} has died in act of combat'
      
    
    def battle_cry(self):
        return f'Odin Owns You All'
        
    pass

 #Saxon


class Saxon(Soldier):
     
    def __init__(self,health,strength):
        super().__init__(health,strength)
        #Soldier.__init__(self,health,strength) 
        
        
    def receive_damage(self,damage):
        self.h = self.h - damage
        if self.h > 0:
            return f'A Saxon has recieved {damage} points of damage'
        else:
            return f'A Saxon has died in combat'
  
  
        
    
    pass

#War



class War:# Peguntar si es correcto poner estas dos clase aqui
    
    def __init__(self): 
        #super.__init__(health,strength) 
        self.viking_army = []
        self.saxon_army = []
     
        
    def add_viking(self,Viking): #este vikingo es una nueva variable
        self.viking_army.append(Viking)
    
    def add_saxon(self,Saxon): #este sajón es una nueva variable 
        self.saxon_army.append(Saxon)
                    
 # Ataque Vikingos 
    def viking_attack(self):
        S = random.choice(self.saxon_army) 
        V = random.choice(self.viking_army).s # Este strenght no estoy segura si es s
        outcome = S.receive_damage(V)
        if S.h <= 0: 
            self.saxon_army.remove(S)
        return outcome                    
                   
 #Ataque Saxons
    def saxon_attack(self):
        V = random.choice(self.viking_army)
        S = random.choice(self.saxon_army).s #Este stranght no estoy segura si es s 
        outcome = V.receive_damage(S)
        if V.h <= 0: 
            self.viking_army.remove(V)#Viking cual
        return outcome
    
    def show_status(self):
        if len(self.saxon_army) == 0:
            return f'Vikings have won the war of the century!'
        elif len(self.vinking_army)== 0 : 
            return f'Saxons have fought for their lives and survive another day...'
        else: 
            return f'Vikings and Saxons are still in the thick of battle'
        
       
        
    pass
