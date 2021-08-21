import tkinter


from tkinter import *
from setting import *
from Text_Editor import *

app = tkinter.Tk() #Создаю окно нашего приложения
app.title(APP_NAME)
app.minsize(width=WIDTH, height=HEIGHT)
app.maxsize(width=WIDTH, height=HEIGHT)

text = tkinter.Text(app, width=WIDTH-100, height=HEIGHT, wrap='word') #создали поле текс
scroll= Scrollbar(app, orient=VERTICAL, command=text.yview) #ссоздали скролл
scroll.pack(side="right", fill="y") # разместили скролл
text.configure(yscrollcommand=scroll.set) #связь текста со скроллом
text.pack() #разместили поле с текстом

editor=Text_editor(text)

menuBar= tkinter.Menu(app) #основное меню
app_menu = tkinter.Menu(menuBar) #выпадающее меню
ap_menu=tkinter.Menu(menuBar)
app_menu.add_command(label="Новый файл", command=editor.new_file)
app_menu.add_command(label="Открыть",command= editor.open_file)
app_menu.add_command(label="Сохранить", command=editor.save_file)
app_menu.add_command(label="Сохранить как", command=editor.save_as_file)

ap_menu.add_command(label="Отменить")
ap_menu.add_command(label="Вырезать")
ap_menu.add_command(label="Копировать")
ap_menu.add_command(label="Вставить")

menuBar.add_cascade(label="Файл", menu = app_menu)
menuBar.add_cascade(label="Правка", menu = ap_menu)
menuBar.add_cascade(label="Справка",command=editor.get_info)
menuBar.add_cascade(label="Выход", command=app.quit)

app.configure(menu=menuBar) #публикуем меню в нашем окне

app.mainloop() # бесконечный цикл нашего приложения