from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def main(text_to_translate="text",text_lang="English",trans_lang="Hindi"):
    trans = Translator(service_urls=['translate.googleapis.com'])
    trans_text = trans.translate(text_to_translate,src=text_lang,dest=trans_lang)
    return trans_text.text

def change():
    s = combo_sor.get()
    d = combo_dest.get()
    translated_text.config(state=NORMAL)
    text = text_to_trans.get(1.0,END)
    text_get = main(text,s,d)
    translated_text.delete(1.0,END)
    translated_text.insert(END,text_get)
    translated_text.config(state=DISABLED)

root = Tk()
root.geometry("500x575")
root.resizable(0,0)
root.config(bg="blue")
root.title("Translator - By Omkara Bajpai")
root.iconbitmap('logo_root.ico')

label = Label(root,text="Translator",font=('Time New Roman',40,"bold"))
label.place(x=100,y=40,height=50,width=300)

frame = Frame(root).pack(side=BOTTOM)

label2 = Label(root,text="Text to Translate",font=('Time New Roman',20,"bold"),bg="blue")
label2.place(x=100,y=100,height=20,width=300)

text_to_trans = Text(frame,font=('Time New Roman',20,"bold"),wrap=WORD)
text_to_trans.place(x=10,y=130,height=150,width=480)

languages = list(LANGUAGES.values())
list_text = []
for language in languages:
    list_text.append(str(language[0].upper()+language[1:]))


combo_sor = ttk.Combobox(frame,values=list_text)
combo_sor.place(x=10,y=300,height=40,width=150)
combo_sor.set("English")

button_change = Button(frame,text="Translate",relief=RAISED, command=change)
button_change.place(x=170,y=300,height=40,width=150)

combo_dest = ttk.Combobox(frame,values=list_text)
combo_dest.place(x=330,y=300,height=40,width=150)
combo_dest.set("Hindi")

label2 = Label(root,text="Translated Text",font=('Time New Roman',20,"bold"),bg="blue")
label2.place(x=100,y=360,height=20,width=300)

translated_text = Text(frame,font=('Time New Roman',20,"bold"),wrap=WORD,state=DISABLED)
translated_text.place(x=10,y=400,height=150,width=480)

root.mainloop()
# main(text_input,text_lang_input,trans_lang_input)