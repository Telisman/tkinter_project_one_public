import  tkinter
import sqlite3


#Connection with sqlite3 database python
konekcijaSaBazom = sqlite3.connect("baza_primedbi.db")
kursor = konekcijaSaBazom.cursor()
kursor.execute("SELECT * FROM osobe")

#Main Tkinter Window
mainProzor = tkinter.Tk()

#Window Title
listNaslov = tkinter.Label(mainProzor, text="Lista Primedbi")
listNaslov.grid(row=0, column=0,sticky=tkinter.W, columnspan=3, padx=2, pady=2)


#Listbox tkinter
lista = tkinter.Listbox(mainProzor, height=10, width=70)
lista.grid(column=0, columnspan=3, padx=2, pady=2)

#ime Label
ime = tkinter.Label(mainProzor, text="Unesite vase ime:")
ime.grid(columnspan=3,sticky=tkinter.W, padx=2, pady=2)

#entry box imeEntry - username
imeEntry = tkinter.Entry(mainProzor,width=69)
imeEntry.grid(column=0, columnspan=3, padx=2, pady=2)

#Task label
primedba = tkinter.Label(mainProzor, text="Unesite primedbu:")
primedba.grid(columnspan=3,sticky=tkinter.W, padx=2, pady=2)

#Task entry - primedbaText
primedbaText = tkinter.Text(mainProzor,height=5, width=52)
primedbaText.grid(column=0, columnspan=3, padx=2, pady=2)


#Geting data from sqlite3
for row in kursor:
        lista.insert(tkinter.END, str.format("{}", row[2]))


#Delete task from sqlite3
def ObrisiKomentar():
    selekcija = lista.get(lista.curselection()) #curselection for primedbaText
    print(selekcija)
    konekcijaSaBazom.execute(str.format("DELETE FROM osobe WHERE primedba='{}'", selekcija))
    konekcijaSaBazom.commit()


#Execute entry of username-imeEntry and Task - primedbaText
def dodajOsobuUBazu():
        kursor.execute(str.format("INSERT INTO osobe (ime, primedba) VALUES ('{}','{}')", imeEntry.get(),primedbaText.get("1.0", tkinter.END)))
        konekcijaSaBazom.commit()
        imeEntry.delete("0", tkinter.END)
        primedbaText.delete(1.0, tkinter.END)
        print("Podaci uneti u bazu")

#Refresh sqlite3 base function
def RefreshData():
    lista.delete(0, tkinter.END)
    kursor.execute("SELECT * FROM osobe")
    for row in kursor:
            lista.insert(tkinter.END, str.format("{}", row[2]))



#Add button command
buttonDodaj = tkinter.Button(mainProzor, text="Dodaj sadrzaj", command=dodajOsobuUBazu)
buttonDodaj.grid(row=10, column=0, padx=2, pady=2)

#Delete button command
Obrisi = tkinter.Button(mainProzor, text="Obrisi primedbu", command=ObrisiKomentar)
Obrisi.grid(row=10, column=1, padx=2, pady=2)

#Refresh sqlite3 and tkinter
Osvezi = tkinter.Button(mainProzor, text="Refresh", command=RefreshData)
Osvezi.grid(row=10, column=2, padx=2, pady=2)



mainProzor.mainloop()

