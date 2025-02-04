import pygame
from pygame.locals import *
import numpy as np

class Poisson:
    
    
    def __init__(self,window,x,y):
        self.window=window
        self.x=x
        self.y=y
        
        self.vx=1
        self.vy=1
        
        self.seuil_repulsion=30
        self.seuil_allignement=100
        self.seuil_attraction=200
        
    def spawn(self):
        pygame.draw.circle(self.window,(200,20,20),(self.x,self.y),5)


    def update(self):
     
        
        return 0
    
    def distance(self,poisson):
        return np.sqrt((self.x-poisson.x)**2 + (self.y-poisson.y)**2)
    
    
    def repulsion(self,poissons):
        fx=0
        fy=0
        d=0
        for poisson in poissons:
            d=self.distance(poisson)
            if self!=poisson and d<self.seuil_repulsion:
                fx=self.x-poisson.x
                fy=self.x-poisson.y
            self.x+=fx*0.001
            self.y-=fy*0.001
            
      
    
    def attraction(self,poissons):
        fx=0
        fy=0
        d=0
        for poisson in poissons:
            d=self.distance(poisson)
            if self!=poisson and self.seuil_allignement<d<self.seuil_attraction:
                fx=self.x-poisson.x
                fy=self.x-poisson.y
            self.x-=fx*0.001
            self.y+=fy*0.001
    
    def allignement(self):
        return 1
    
    
    
    
    

class Environnement:
    def __init__(self,n):
        pygame.init() # initialisation de pygame
        self. height=720
        self.width=1080
        self.nombre_poisson=n
        
        self.window=pygame.display.set_mode((self.width,self.height)) # creation de la fenetre
        self.background_color=(28, 107, 160)
        pygame.display.set_caption("Simulation de l'évolution des bancs de poisson")
        
        self.list_poisson=[]
        for i in range(self.nombre_poisson):
            
            self.x_r=np.random.randint(0,self.width)
            self.y_r=np.random.randint(0,self.height)
            self.list_poisson.append(Poisson(self.window,self.x_r,self.y_r))
        
        
   
    def draw_background(self):
        self.window.fill(self.background_color)
                
    def run(self):
        running=True 
        while running == True: # tant que le code run
            for event in pygame.event.get(): 
                if event.type== pygame.QUIT:
                    running=False
                    
            self.draw_background()
            for poisson in self.list_poisson:
                poisson.spawn()
          
            for poisson in self.list_poisson:
                poisson.repulsion(self.list_poisson)
                poisson.attraction(self.list_poisson)
          
          
            pygame.display.flip()
     
        pygame.quit() # fermer la fenetre pygames

def main():
    n=50
    e=Environnement(n)
    e.run()
    return 0
  
   
if __name__ == "__main__":
    main()
        