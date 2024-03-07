import tkinter as tk

class Pong:
    def __init__(self):
        self.__rect=canvas.create_rectangle(500,550,600,600,fill="green")

    def get_rect(self):
        return self.__rect
    

class Balle:
    def __init__(self,pong):
        self.__ball=canvas.create_oval(100,100,200,200,fill="green")
        self.__dir=1
        self.__pong=pong

    def touche(self):
        x1_pong, y1_pong, x2_pong, y2_pong = canvas.coords(self.__pong)
        x1_balle, y1_balle, x2_balle, y2_balle = canvas.coords(self.__ball)
        print("pong: "+str(x1_pong)+ " "+str(y1_pong)+" "+str(x2_pong)+ " "+str(y2_pong))
        print("balle: "+str(x1_balle)+ " "+ str(y1_balle)+" "+str(x2_balle)+ " "+str(y2_balle))
        print(balle.get_dir())
        
        if (y2_balle >= y1_pong) and (y1_balle <= y2_pong) and (x2_balle >= x1_pong) and (x1_balle <= x2_pong):
            self.set_dir(-1)  # Reverse the direction
 

    def bouge(self):
        self.touche()
        if self.__dir==1:
            canvas.move(self.__ball,5,20)
        if self.__dir==-1:
           canvas.move(self.__ball,-5,-20)
        windows.after(400,self.bouge)

    def get_ball(self):
        return self.__ball
    
    def get_dir(self):
        return self.__dir
    
    def set_dir(self,direction):
        self.__dir=direction

def stop(pong):
    x1, y1, x2, y2 = canvas.coords(pong.get_rect())
    if  x2 >= 600:  # Si le rectangle dépasse les limites horizontales
        return 1
    elif x1 <= 0:
        return 2
    else:
        return 0
 
   
def dir(event,pong):
    if stop(pong)==1:
        if event.keysym == 'Left':
            canvas.move( pong.get_rect(),-10,0)
    if stop(pong)==2:
        if event.keysym == 'Right':
            canvas.move( pong.get_rect(),10,0)
    if stop(pong)==0:
        if event.keysym == 'Right':
            canvas.move( pong.get_rect(),10,0)
        if event.keysym == 'Left':
            canvas.move( pong.get_rect(),-10,0)
            
if __name__=="__main__":
    windows=tk.Tk()
    canvas=tk.Canvas(windows,width=600,height=600)
    canvas.pack()
    windows.title("Pong")
    pong=Pong()
    balle=Balle(pong.get_rect())
    balle.bouge()
    canvas.bind_all('<Left>', lambda event: dir(event,pong))
    canvas.bind_all('<Right>', lambda event:dir(event,pong))
    windows.mainloop()