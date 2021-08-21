import tkinter
import codecs

from tkinter import *
from tkinter.filedialog import askopenfile, askopenfilename, asksaveasfile, asksaveasfilename # сохранить как, открыть как
from tkinter.messagebox import showerror # показ всех ошибок
from tkinter import messagebox #уведомление приложений


class Text_editor():
    def __init__(self,text2):
        self.file_name= tkinter.NONE
        self.text=text2

    def new_file(self):
        self.file_name= 'Безымянный'
        self.text.delete('1.0',tkinter.END)

    def open_file(self):
        inp = askopenfilename()
        if inp is None:
            return
        with codecs.open(inp,encoding='utf-8') as name:
            data = name.read() 
            self.text.delete('1.0',tkinter.END)
            self.text.insert('1.0',data)

    def save_file(self):
        data = self.text.get('1.0', tkinter.END)
        with open(self.file_name, 'w', encoding='utf-8') as output:
            output.write(data)
        

    def save_as_file(self):
        output = asksaveasfilename()
        data = self.text.get('1.0', tkinter.END)
        try:
            with open(output+'.txt','w',encoding='utf-8') as file:
                file.write(data.rstrip())
        except Exception:
            showerror(title="Ошибка", message="Ошибка сохранения файла")    

    def get_info(self):
        messagebox.showinfo("Справка", "Информацция о нашем приложении! Спасибо, что его используете")