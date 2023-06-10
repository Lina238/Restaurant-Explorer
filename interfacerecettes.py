from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from aima.logic import *
from aima.utils import *
x,y,z,w = symbols('x,y,z,w')
k = FolKB()
k.tell(expr('Restaurant(y,z)'))
k.tell(expr('Plat(y,z)'))
k.tell(expr('Restaurant(Bistroquet,Français)'))
k.tell(expr('Restaurant(Linaresto,Algerien)'))
k.tell(expr('Restaurant(Brasserie,Français)'))
k.tell(expr('Restaurant(Gourmet ,Français)'))
k.tell(expr('Restaurant(Casbah,Algerien)'))
k.tell(expr('Restaurant(Wok,Chinois)'))
k.tell(expr('Restaurant(Pizzeria,Italien)'))
k.tell(expr('Adresse(Linaresto,Amizour_Bejaia)'))
k.tell(expr('Restaurant(Wok,Alger)'))
k.tell(expr('Adresse(Brasserie,Jijel)'))
k.tell(expr('Adresse(Bistroquet,Bejaia)'))
k.tell(expr('Adresse(Wok,Alger)'))
k.tell(expr('Adresse(Gourmet,Annaba)'))
k.tell(expr('Adresse(Casbah,ALger)'))
k.tell(expr('Adresse(Pizzeria,Alger)'))
k.tell(expr('Plat(Bistroquet,Steak_frites)'))
k.tell(expr('Plat(Wok,Riz_cantonais)'))
k.tell(expr('Plat(Linaresto,Adesss)'))
k.tell(expr('Plat(Casbah,Salade_mechouia)'))
k.tell(expr('Plat(Casbah,Méchoui)'))
k.tell(expr('Plat(Casbah,Chakhchoukha)'))
k.tell(expr('Plat(Casbah,Basboussa)'))
k.tell(expr('Plat(Brasserie,Moules_marinières)'))
k.tell(expr('Plat(Brasserie,Escargots_à_la_provençale)'))
k.tell(expr('Plat(Brasserie,Cassoulet)'))
k.tell(expr('Plat(Brasserie,Crème_caramel)'))
k.tell(expr('Plat(Gourmet,Tartare_de_saumon)'))
k.tell(expr('Plat(Gourmet,Foie_gras_poêlé)'))
k.tell(expr('Plat(Gourmet,Coquilles_Saint-Jacques)'))
k.tell(expr('Plat(Linaresto,Zitoun)'))
k.tell(expr('Plat(Wok,Nouilles_sautées)'))
k.tell(expr('Plat(Pizzeria,Pizza_pepperoni)'))
k.tell(expr('Plat(Pizzeria,Pizza_margherita)'))
k.tell(expr('Plat(Bistroquet,Boeuf_bourguignon)'))
k.tell(expr('Restaurant(y,z) ==>Preference(x,z,y)'))
k.tell(expr('Restaurant(y,z) ==>Adresse(y,w)'))
k.tell(expr('Restaurant(y,z)==>Plat(y,w) '))
root = tk.Tk()
root.title("Recettes")
root.geometry('1000x600+300+200')
root.configure(bg="#fff")
root.resizable(False, False)
img = tk.PhotoImage(file='cuisinier.png')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
frame_width = int(screen_width * 0.9)
frame_height = int(screen_height * 0.9)
x_margin = int((screen_width - frame_width) / 2)
y_margin = int((screen_height - frame_height) / 2)
frame = tk.Frame(root, width=frame_width, height=frame_height, bg="#fff",
                 highlightbackground="#F9A826", highlightthickness=3)
frame.pack(fill=tk.BOTH, padx=10, pady=10)
label_img = tk.Label(frame, image=img, width=400, height=400, bg="#fff")
label_img.place(x=550, y=30)
heading = tk.Label(frame, text='Que vais-je manger aujourd\'hui?', fg='#000', bg='white', font=("Helvetica", 25))
heading.place(x=69, y=0)
style = ttk.Style(frame)
button_frame = tk.Frame(frame, bg="#fff", width=500, height=300)
button_frame.place(x=110, y=120)
style.theme_create('custom', parent='alt', settings={
    "TCombobox": {
        "configure": {"foreground": "#000", "background": "#fff", "bordercolor": "#F9A826", "arrowcolor": "#000"},
        "padding": 5,
        "bordercolor": "#F9A826",
        "arrowcolor": "#000"
    }
})
style.theme_use('custom')
label1 = tk.Label(button_frame, text="Votre nom:")
label1.pack()
entry1 = tk.Entry(button_frame)
entry1.pack()
label2 = tk.Label(button_frame, text="Votre Type selon la région:")
label2.pack()
entry2 = tk.Entry(button_frame)
entry2.pack()
text_area = tk.Text(button_frame, height=10, width=60)
text_area.pack()
def display_selected_ele():
    selected_elements = []
    restaurant_dishes = {}  
    nom = entry1.get()
    region = entry2.get()
    suggestions = fol_fc_ask(k, expr(f"Preference({nom},{region},y)"))
    for s in list(suggestions):
        for key, value in s.items():
            if str(value)!= str(entry1.get()):
              print(value)
              Menu = fol_fc_ask(k, expr(f"Plat({value},w)"))
              Adresse = fol_fc_ask(k, expr(f"Adresse({value},w)"))
              for ss in list(Adresse):
               for kk, val in ss.items():
                 val=f"{value} qui se situe à {val}"
              restaurant_dishes[val] = [] 
              for res in list(Menu):
                for a, v in res.items():
                    if str(v) != "w" and str(v)!=str(value):
                        restaurant_dishes[val].append(v)  
    text_area.delete(1.0, tk.END)
    for restaurant, dishes in restaurant_dishes.items():
        selected = ",".join(str(dish) for dish in dishes)
        selected_elements.append(f"{restaurant}: {selected}")
    selected_elements_str = F"bonjour {nom} voici les restaurants avec leurs menues :): \n"+"\n".join(selected_elements)
    text_area.insert(tk.END, selected_elements_str)
button = tk.Button(button_frame, text="Afficher", command=display_selected_ele, width=14, height=1, bg="#F9A826", fg="#fff", font=("Helvetica", 14, "bold"))
button.pack(side=tk.BOTTOM, pady=20)
root.mainloop()
