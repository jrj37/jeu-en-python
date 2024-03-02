import tkinter as tk

class Element:
    def __init__(self,x1,y1,x2,y2):
        self.__x1=x1
        self.__y1=y1
        self.__x2=x2
        self.__y2=y2
        self.__figure=canvas.create_rectangle(x1,y1,x2,y2, fill="green")
    
    def get_x1(self):
        return self.__x1
    
    def get_x2(self):
        return self.__x2
    
    def get_y1(self):
        return self.__y1
    
    def get_y2(self):
        return self.__y2
    
    def get_figure(self):
        return self.__figure
    
    def bouge(self):
            canvas.move(self.__figure,20,0)
            window.after(400, self.bouge)
            
class Serpent:
    def __init__(self,liste_elem):
        self.__list_elem=[liste_elem]
    
    def get_list_elem(self):
        return self.__list_elem
    
    def ajout(self):
        last_element = self.__list_elem[-1]
        x1, y1, x2, y2 = canvas.coords(last_element.get_figure())
            
        element = Element(x2+100,y1,x2, y2)  # Adjust width to maintain size
        self.__list_elem.append(element)

    def bouge(self):
        for i in range(len(self.__list_elem)):
            self.__list_elem[i].bouge()
    
    def collision(self):
        for i in range(len(self.__list_elem)):
            x1, y1, x2, y2 = canvas.coords(self.__list_elem[i].get_figure())
            print(x1)
            if x1 < 0 or y1 < 0 or x2 > 600 or y2 > 600:
                return True
        return False
 
                
if __name__=="__main__":
    window = tk.Tk()
    window.title("Rectangle en Tkinter")
    window.geometry("600x600")
    canvas = tk.Canvas(window, width=600, height=600)
    canvas.pack()
    x1=200
    y1=200
    x2=300
    y2=250
    element=Element(x1,y1,x2,y2)
    snake =Serpent(element)
    snake.ajout()
    #snake.ajout()
    snake.bouge()
    if (snake.collision()==True):
        print("collision")
    window.mainloop()