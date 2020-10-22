from tkinter import *
  
# Create a GUI window   
root = Tk() 
  
# Create a text area box    
# for filling or typing the information. 
text = Text(root) 

  
text.insert(END, "Pandemic has resulted in economic slowdown worldwide\n") 
text.insert(END, "Pandemic has resulted in economic slowdown worldwide\n") 
text.insert(END, "Pandemic has resulted in economic slowdown worldwide\n") 
text.insert(END, "Pandemic has resulted in economic slowdown worldwide") 
text.insert(END, "Pandemic has resulted in economic slowdown worldwide") 
text.insert(END, "Pandemic has resulted in economic slowdown worldwide") 
text.insert(END, "Pandemic has resulted in economic slowdown worldwide") 
  
text.pack(expand=1, fill=BOTH) 
  
# add tag using indices for the 
# part of text to be highlighted 
text.tag_add("start", "2.20", "2.23") 
  
#configuring a tag called start 
text.tag_config("start", background="black", 
                 foreground="red") 
  
# start the GUI 
root.mainloop() 