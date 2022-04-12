from tkinter import *
from tkinter import ttk,filedialog
from PIL import ImageGrab
import os

class Operations:
    def __init__(self):
        try:
            self.Loc=os.environ['USERPROFILE'].replace("\\","/")
            self.i=1

            self.root=Tk()
            self.root.title("ScreenShot")
            self.root.config(bg="#222222")
            self.root.resizable(0,0)
            # main frame
            MainFrame=Frame(self.root,bg="#222222",highlightthickness=1,highlightcolor="yellow",highlightbackground="yellow")
            # save location
            SaveLocation=Button(MainFrame,text="Location",font=("arial",15,"bold"),bg="yellow",fg="#222222",cursor="hand2",activebackground="red",activeforeground="yellow",borderwidth=0,command=self.Location_change)
            SaveLocation.grid(row=0,column=0,padx=2,pady=2,sticky="nswe")
            # View
            View=Button(MainFrame,text="View",font=("arial",15,"bold"),bg="yellow",fg="#222222",cursor="hand2",activebackground="red",activeforeground="yellow",borderwidth=0,command=self.View_Button)
            View.grid(row=0,column=1,padx=2,pady=2,sticky="nswe")
            # Save
            Saveas=Button(MainFrame,text="Save",font=("arial",15,"bold"),bg="yellow",fg="#222222",cursor="hand2",activebackground="red",activeforeground="yellow",borderwidth=0,command=self.save_image)
            Saveas.grid(row=0,column=2,padx=2,pady=2,sticky="nswe")
            # location
            self.Location=Label(MainFrame,text=f"{self.Loc}",font=("arial",15,"bold"),bg="#222222",fg="yellow")
            self.Location.grid(row=1,columnspan=3,padx=2,pady=2,sticky="nswe")
            MainFrame.pack(fill=BOTH,expand=True,padx=4,pady=4)
            self.root.bind("<Return>",self.save_image)
            self.root.bind("<F1>",self.View_Button)
            self.root.mainloop()
        except:
            pass
        pass
    def Location_change(self,*args):
        try:
            self.Loc=filedialog.askdirectory()
            self.Location.config(text=f"{self.Loc}")
        except:
            pass
        pass
    def View_Button(self,*args):
        try:
            self.img=ImageGrab.grab()
            self.img.show()
        except:
            pass
        pass
    def save_image(self,*args):
        try:
            self.img=ImageGrab.grab()
            os.chdir(self.Loc)
            self.img.save(f"Screen {self.i}.jpg")
            self.i=self.i+1
        except:
            pass
        pass
    pass
App=Operations()