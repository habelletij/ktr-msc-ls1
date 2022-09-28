import tkinter as tk
from os import read
import csv
from functools import partial








#l'interface d'accueil
def home_interface():

    window = tk.Tk()

    #caracteristiques de l'interface
    window.title("business card manager")
    window.geometry("360x360")
    window.config(background='#4065A4')

    #creer les deux champs identifiant et mots de passe utilisateur
    id = tk.Label(window, text = "id")
    id.pack(pady=5)
    id_input = tk.Entry(window)
    id_input.pack()
    password = tk.Label(window, text = "password")
    password.pack(pady=5)
    password_input = tk.Entry(window)
    password_input.pack()
    
    #creer les boutons
    login_button = tk.Button(window ,text="log in", command=partial(login, id_input, password_input, window), font=("Arial", 25))
    login_button.pack(pady=25, fill=tk.X) 
    Create_account_button = tk.Button(window ,text="Create account", command=partial(create_account, window))
    Create_account_button.pack(pady=80)

    window.mainloop()  



def user_interface(row):
    window = tk.Tk()
    
    window.title(row[0])
    window.geometry("480x360")
    window.config(background='#4065A4')
    
    t = tk.Label(window, text = "Welcome in your account space!")
    t.pack(pady=25)
    t.place(x=150, y=40)
    
    logout_button = tk.Button(window ,text="Logout", command=partial(logout, window))
    logout_button.place(x=400, y=0)
    library = tk.Button(window ,text="library",command=partial(library_interface, window, row))
    library.pack(pady=150, fill=tk.X)

    


def library_interface(window0, row):
    window0.destroy()
    window = tk.Tk()

    #caracteristiques de l'interface
    window.title(row[0])
    window.geometry("480x360")
    window.config(background='#4065A4')

    #afficher les cartes bisiness de l'utilisateur
    data(row[0], window)
    
    t = tk.Label(window, text = "Your business cards:")
    t.pack(pady=25)
    t.place(x=150, y=20)
    
    
    #creer les boutons
    new_card = tk.Button(window ,text="new business card",command=partial(add_card, window, row))
    new_card.pack(side=tk.BOTTOM)
    retourner = tk.Button(window ,text="retour",command=partial(return1, window, row))
    retourner.place(x=0, y=0)
    
    
    
def create_account_interface():
    window = tk.Tk()

    #caracteristiques de l'interface
    window.title("Create account")
    window.geometry("480x360")
    window.config(background='#4065A4')

    #creer les deux champs identifiant et mots de passe utilisateur
    id = tk.Label(window, text = "id")
    id.pack(pady=5)
    id_input = tk.Entry(window)
    id_input.pack()
    password = tk.Label(window, text = "password")
    password.pack(pady=5)
    password_input = tk.Entry(window)
    password_input.pack()
    
    #creer les boutons
    create_button = tk.Button(window ,text="create", command=partial(create_user, id_input, password_input, window))
    create_button.pack(pady=35)
    retourner = tk.Button(window ,text="retour",command=partial(return3, window))
    retourner.place(x=0, y=0)



def add_card(window0, row):
    window0.destroy()
    window = tk.Tk()

    #caracteristiques de l'interface
    window.title(row[0])
    window.geometry("480x360")
    window.config(background='#4065A4')

    #creer les champs pour l'insertion des donnees par l'utilisateur
    name = tk.Label(window, text = "Name")
    name.pack(pady=5)
    name_input = tk.Entry(window)
    name_input.pack()
    company = tk.Label(window, text = "Company Name")
    company.pack(pady=5)
    company_input = tk.Entry(window)
    company_input.pack()
    email = tk.Label(window, text = "Email address")
    email.pack(pady=5)
    email_input = tk.Entry(window)
    email_input.pack()
    telephone = tk.Label(window, text = "Telephone number")
    telephone.pack(pady=5)
    telephone_inpute = tk.Entry(window)
    telephone_inpute.pack()
    
    add_button = tk.Button(window ,text="add",command=partial(create_card, row, name_input, company_input, email_input, telephone_inpute, window))
    add_button.pack(pady=25)
    retourner = tk.Button(window ,text="retour",command=partial(return2, window, row))
    retourner.place(x=0, y=0)
 
#creer un utilisateur   
def create_user(id_input, password_input, window):
    with open('account.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id_input.get(),password_input.get()])
    file.close()
    f = open(id_input.get()+'.csv', 'a+')
    f.close()
    window.destroy()
    home_interface()

#creer une carte business
def create_card(row, name_input, company_input, email_input, telephone_inpute, window):
    with open(row[0]+'.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name_input.get(),company_input.get(),
        email_input.get(), telephone_inpute.get()
        ])
    file.close()
    library_interface(window, row)



#recuperer les donnees du fichier csv
def data(id,window):
    with open(id+'.csv', 'r',) as file:
        reader = csv.reader(file, delimiter=',')
        
        for row in reader:
            frame = tk.Frame(window, bg='grey', bd=1)
            card = tk.Label(frame, text = "name: "+row[0]+" company: "+row[1]+" email: "+row[2]+" telephone: "+row[3])
            card.pack()
            frame.pack(expand=tk.YES)
            
    file.close()

# ouvrir l'interface create account   
def create_account(window):
    window.destroy()
    create_account_interface()
    
def return1(window, row):
    window.destroy()
    user_interface(row)
    
def return2(window, row):
    library_interface(window, row)
    
def return3(window):
    window.destroy()
    home_interface()

# se connecter à son compte
def login(id_input, password_input, window):
    with open('account.csv', 'r',) as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if id_input.get() == row[0] and password_input.get() == row[1]:
               window.destroy()
               user_interface(row)
    file.close()


# se deconnecter
def logout(window):
    window.destroy()
    home_interface()

home_interface()
