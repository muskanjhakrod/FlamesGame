from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root=Tk()
root.geometry("1500x800+0+0")

def calCount():
    n1 = entry1.get().strip().lower()
    n2 = entry2.get().strip().lower()
    
    if not n1 or not n2:
        messagebox.showerror("Input Error", "Both names must be provided!")
        return None
    
    n1 = list(n1.replace(" ",""))
    n2 = list(n2.replace(" ",""))
    
    temp=n1
    for i in temp:
        if i in n2:
            n1.remove(i)
            n2.remove(i)
    count=len(n1)+len(n2)
    return count

def calFlames(count):
    flames=['Friends','Love','Affection','Marriage','Enemy','Siblings']
    while len(flames) > 1:
        result = (count % len(flames)) - 1
        if result >= 0 :
            right = flames[result+1:]
            left = flames[:result]
            flames= right + left
        else:
            flames.pop()
    return flames[0]

def Flames():
    count = calCount()
    if count is None:
        return
    print(count)
    flame = calFlames(count)
    print(flame)
    result.config(text=flame, fg="#AA336A")
    if flame == "Love":
        new_img = Image.open("C:/users/hp/OneDrive/Documents/Programing_and_collage/python/flames_Calculator/Love.jpg")
        new_img = new_img.resize((1600, 800))
        new_bg_image = ImageTk.PhotoImage(new_img)
        canvas.itemconfig(image_id, image=new_bg_image)
        canvas.image = new_bg_image
        canvas.itemconfig(FlameText, fill="White")
    elif flame == "Enemy":
        new_img = Image.open("C:/users/hp/OneDrive/Documents/Programing_and_collage/python/flames_Calculator/enemy.jpg")
        new_img = new_img.resize((1600, 800))
        new_bg_image = ImageTk.PhotoImage(new_img)
        canvas.itemconfig(image_id, image=new_bg_image)
        canvas.image = new_bg_image
        canvas.itemconfig(FlameText, fill="White")
        

img=Image.open("C:/users/hp/OneDrive/Documents/Programing_and_collage/python/flames_Calculator/background.jpg")
img = img.resize((1600, 800))
bg_image = ImageTk.PhotoImage(img)

canvas = Canvas(root, width=1500, height=800)
canvas.pack(fill="both", expand=True)

# Add the image to the canvas
image_id = canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Add text directly to the canvas (no background)
FlameText = canvas.create_text(800, 80, text="FLAMES", fill="#AA336A", font=("JUST Sans bold", 40))

frame = Label(root,width=100,height=25)
frame.place(x=440,y=220)

name1 = Label(frame,text="Enter First person name :",font=("Arial",15))
name1.place(x=45,y=50)
entry1 = Entry(frame,width=50,font=("Arial",16),bd=1,fg="#5A5A5A")
entry1.place(x=45,y=90)

name2 = Label(frame,text="Enter second person name :",font=("Arial",15))
name2.place(x=45,y=150)
entry2 = Entry(frame,width=50,font=("Arial",16),bd=1,fg="#5A5A5A")
entry2.place(x=45,y=190)

button = Button(frame,width=54,text="Find Relationship",font=("Arial",15),bd=1,bg="#AA336A",fg="white",command=Flames)
button.place(x=45,y=250)

result = Label(root, text="Result will appear here", font=("Arial", 15), fg="gray")
result.place(x=700, y=650)

root.mainloop()