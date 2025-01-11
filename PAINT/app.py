from tkinter import *

WIDTH, HEIGHT = 500, 500

class PaintApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Paint App")
        
        self.canvas = Canvas(self.root, width=WIDTH, height=HEIGHT, bg="white")
        self.canvas.pack()
        
        self.red_button = Button(self.root, text="Clear", command=self.clear)
        self.red_button.pack(side=LEFT)
        
        self.red_button = Button(self.root, text="Black", command=self.set_black)
        self.red_button.pack(side=LEFT)
        
        self.red_button = Button(self.root, text="Red", command=self.set_red)
        self.red_button.pack(side=LEFT)
        
        self.red_button = Button(self.root, text="Blue", command=self.set_blue)
        self.red_button.pack(side=LEFT)

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)
        
        self.color = "black"
        self.pen_width = 5
        self.last_x = None
        self.last_y = None
        
    def paint(self, event):
        if self.last_x is not None and self.last_y is not None:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill=self.color, width=self.pen_width)
        self.last_x, self.last_y = event.x, event.y
    
    def set_black(self):
        self.color = "black"
        
    def set_red(self):
        self.color = "red"
        
    def set_blue(self):
        self.color = "blue"
    
    def clear(self):
        self.canvas.delete("all")
        
    def reset(self, event):
        self.last_x = None
        self.last_y = None

def main():
    app = PaintApp()
    app.root.mainloop()
    
if __name__ == "__main__":
    main()