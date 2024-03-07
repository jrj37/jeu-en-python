import tkinter as tk

class Pong:
    def __init__(self):
        self.__rect=canvas.create_rectangle(500,550,600,600,fill="green")

    def get_rect(self):
        return self.__rect
    

class Balle:
    def __init__(self):
        self.__ball=canvas.create_oval(100,100,200,200,fill="green")

    def bouge(self):
        canvas.move(self.__ball,5,20)
        windows.after(400,self.bouge)

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
    balle=Balle()
    balle.bouge()
    canvas.bind_all('<Left>', lambda event: dir(event,pong))
    canvas.bind_all('<Right>', lambda event:dir(event,pong))
    windows.mainloop()
