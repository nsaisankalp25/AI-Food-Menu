import tkinter, json 
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
rt = Tk()
rt.geometry("750x550")
rt.title("AI FOOD MENU")
rt.configure(background = '#FFFCC4')
with open(r"C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Ai school project\reqs\menu_items.json") as file_open:
    data_raw = json.load(file_open)
recipies, all_ingrns = {}, []
for i in data_raw.items():
    recipies[i[0].lower().strip()] = i[1]
    for ii in i[1]: all_ingrns.append(ii)
all_ingrns = list(dict.fromkeys(all_ingrns))
def all_white_bg():
    for i in rt.winfo_children():
        try:i.configure(bg = '#FFFCC4')
        except: pass
def show_pics():
    apple = ImageTk.PhotoImage(Image.open(r"C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Ai school project\reqs\apple.png").resize((63,60), Image.ANTIALIAS))
    cauli = ImageTk.PhotoImage(Image.open(r"C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Ai school project\reqs\cauli.png").resize((63,60), Image.ANTIALIAS))
    cherry = ImageTk.PhotoImage(Image.open(r"C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Ai school project\reqs\cherry.png").resize((63,60), Image.ANTIALIAS))
    kiwi = ImageTk.PhotoImage(Image.open(r"C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Ai school project\reqs\kiwi.png").resize((63,60), Image.ANTIALIAS))
    orange = ImageTk.PhotoImage(Image.open(r"C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Ai school project\reqs\orange.png").resize((63,60), Image.ANTIALIAS))
    pears = ImageTk.PhotoImage(Image.open(r"C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Ai school project\reqs\pears.png").resize((63,60), Image.ANTIALIAS))
    pineapple = ImageTk.PhotoImage(Image.open(r"C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Ai school project\reqs\pineapple.png").resize((63,60), Image.ANTIALIAS))
    chilli = ImageTk.PhotoImage(Image.open(r"C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Ai school project\reqs\chilli.png").resize((63,60), Image.ANTIALIAS))
    cords = [[10, 30],[10, 150], [10, 260], [10, 350], [600, 10], [600, 150], [600, 250], [600, 350]]
    imgs_list = [apple, cauli, cherry, kiwi, orange, pears, pineapple, chilli]
    for num,i in enumerate(imgs_list):
        img_show = Label(image = i, borderwidth = 0)
        img_show.image = i
        img_show.place(x = cords[num][0], y = cords[num][1])
        
show_pics()
def clear_all():
    for i in rt.winfo_children():i.destroy()
def show_dishes(dishes_names: tuple, color_fg):
    clear_all()
    Label(rt, text = "All the Dishes & Beverages available.", font = ("cambria", 28), fg = '#FF0093').place(x = 100, y = 25)
    a = 50
    x1 = 30
    for num, i in enumerate(dishes_names):
        a += 30
        if a >= 300 and a < 340:
            x1 = 200
            a -= 240
        Label(rt, text = f"{num+1}) {i.capitalize()}",
        font = ("calibri", 18), fg = color_fg).place(x = x1, y = a)
    def show_ingrs():
        clear_all()
        Label(rt, text = "All the Ingredients used", font = ("cambria", 24),
         fg = "#000000").place(x = 200, y = 25)
        ingrs_dict = {}
        y_val, x = 50, 80
        for num, i in enumerate(all_ingrns):
            y_val += 32
            if num == 11:
                x += 200
                y_val -= 355
            elif num == 22:
                y_val -= 355
                x += 200
            ingrs_dict[i] = BooleanVar()
            Checkbutton(rt, text = f"{num+1}) {i}", fg = '#002EFF', 
            font = ('calibri', 14), variable = ingrs_dict[i], activebackground = "white",
            activeforeground = "#002EFF").place(x = x, y = y_val)
        all_white_bg()
        def remove_items():
            clear_all()
            rem_lst = []
            remdishlst = []
            rem_lst.clear()
            remdishlst.clear()
            for i in ingrs_dict.items():
                ing = bool(i[1].get())
                if ing == True: rem_lst.append(i[0])
            for i in recipies.items():
                for ii in rem_lst: 
                    if ii in i[1]: remdishlst.append(i[0])
            a = []
            for i in recipies.keys():
                if i not in remdishlst: a.append(i)
                else: pass
            show_dishes(tuple(a), "#FF0074")
        Button(rt, text = "Exclude Selected Ingredients and Update Menu", 
        font = ("montserrat", 14), fg = "#2FC400",command = remove_items).place(x = 100, y = 450)
        all_white_bg()
    Button(rt, text = "View and Exclude ingredients", font = ("Dubai Medium", 15 ), 
    command = show_ingrs, fg = "#20AB0F", pady = None, borderwidth=2).place(x = 80, y = 380)
    all_white_bg()
intro = Label(rt, text = "Welcome to The\nHelvets Hotel!",
 font = ("Georgia", 35, "bold"), fg = '#ed5057').place(x =150, y = 80)
s = ttk.Style()
s.configure('my.TButton', font=('lucida sans', 15))
menu_view_b = ttk.Button(rt, text = "View Dishes",style='my.TButton', 
 command = lambda: show_dishes(tuple(recipies.keys()), '#3346FF')).place(x = 280, y = 230)
all_white_bg()
rt.mainloop()