#uso de if __name__=='__main__'
#alt + click izquierdo(selecionar con el click las lineas en donde vamos a escribir simultaneamente)
#ctrl + f (buscamos una palabra en todo el codigo)/con vs code
#ctrl + h (elegimos si queremos cambiar la palabra buscada por una nueva palabra)/con vs code
#t = texto.get(1.0,'end-1c')/tomar texto
#t = texto.delete(1.0,'end-1c')/borrar texto
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import webbrowser
#from lector_csv import table_example

class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title('APP DORNA')
        self.raiz.geometry("770x700")
        self.raiz.configure(background = 'white')
        self.raiz.resizable(width=False,height=False)

        #Funciones
        def obtener_info():
            if self.lista_desplegable.get() == '8428-1A': #esta funcion es para obtener el valor del item seleccionado en la lista desplegable, usamos .get() para tomar el valor
                    table_example()
            else:
                print(self.lista_desplegable.get())

        def new_window():
            self.top = Toplevel(self.raiz) #esta funcion es para abrir una nueva ventana al presionar dicho boton
            self.top.title('Notas')
            self.top.geometry('300x300')
            self.top.configure(bg='black')
            self.notas = Text(self.top,font = ('Calibri',12),borderwidth=1,relief='solid',bg='white')
            self.notas.place(x = 30,y = 10,width=240,height=250)
            self.btn_save = Button(self.top, text= "Save", fg='black',activebackground = 'white',activeforeground = 'blue',width = 5,height = 1,command = save_file) #definimos el boton save
            self.btn_save.place(x=30,y=265)
            self.btn_exit = Button(self.top, text= "Exit", fg='black',activebackground = 'white',activeforeground = 'blue',width = 5,height = 1,command=Exit) #definimos el boton save
            self.btn_exit.place(x=130,y=265)
            self.btn_delete = Button(self.top,text= "Delete", fg='black',activebackground = 'white',activeforeground = 'blue',width = 5,height = 1,command = delete) #definimos el boton save
            self.btn_delete.place(x=220,y=265)
            self.raiz.iconify() #minimiza ventana principal

        #Define the function/guardar archivo/abruir archivo
        def open_file():#funcion para mostrar y ver el contenido del mismo
            f = open('H:/Temporal/Echevarria/estado_robot.txt')#abre un archivo en modo lectura
            filetypes=(('text files','*.txt'),('All files','*.*'))
            filename= fd.askopenfilename(
                title='Open a file',
                initialdir='/',
                filetypes=filetypes)
            print('Archivo abierto')
            print(f.read()) #read() lee todo el texto como una cadena.

        def save_file(): #funcion para guardar el texto mostrado en la etiqueta de texto
            with open(r'H:/Temporal/Echevarria/estado_robot.txt','a') as f: #abre un archivo y lo sobreescribe,si no hay lo crea y escribe
                f.write(self.notas.get(1.0,'end-1c'))
                f.write('\n') #salto de linea
            filetypes=(('text files','*.txt'),('All files','*.*'))
            filename= fd.asksaveasfilename(
                title='Save a file',
                initialdir='/',
                filetypes=filetypes)
            print('Archivo Guardado')
            

        def Exit(): #funcion para cerrar ventana top y volver a maximizar ventana raiz
            self.top.destroy() #cierra top
            self.raiz.deiconify() #abre raiz
            
        def delete(): #borrar contenido de una etiqueta Text
            self.notas.delete('1.0','end')

        def about_window():
            dorna_web = webbrowser.open('https://doc.dorna.ai/')



        
        #Menus
        self.menu = Menu(self.raiz)
        self.raiz.config(menu=self.menu)
        filemenu = Menu(self.menu,tearoff=0)
        self.menu.add_cascade(label='File',menu=filemenu)
        filemenu.add_command(label='New window',command=new_window)
        filemenu.add_command(label='Open register..',command=open_file)
        filemenu.add_separator()
        filemenu.add_command(label='Exit',command=self.raiz.destroy)#definimos que al dar click en exite se cerrara la aplicacion
        helpmenu = Menu(self.menu,tearoff=0)
        self.menu.add_cascade(label='Help',menu=helpmenu)
        helpmenu.add_command(label='About',command=about_window)

        #Etiquetas
        self.error=Label(self.raiz,text= 'Visualizacion de Errores\n(Try and Except)',fg='white',bg='black',font=('Calibri',20),width=31,height=7) #definmos etiqueta y tamano
        self.error.place(x=300,y=35) #posicionamos
        imagen = PhotoImage(file=r'app_dorna\dorna.png')#definimos imagen
        self.robot_view = Label(self.raiz,image = imagen,width=440,height=380)#creamos etiqueta para imagen 
        self.robot_view.place(x=300,y=280)#posicionamos
        #lista desplegable

        #etiqueta seleccion
        self.seleccion = Label(self.raiz, text="Seleccione un programa", font= ('Helvetica 10 bold'),padx=20)
        self.seleccion.place(x=30,y=55) #posicionamos
        self.lista_desplegable = ttk.Combobox(self.raiz,width=17)#si no queremos agregar nuevos items a la lista usamos state='readonly' dentro de los ()
        self.lista_desplegable.place(x=65,y=85)
        opciones = ["8428-1A","9316-1B","9435-1C","27117-1B"]
        self.lista_desplegable['values']=opciones
        
        #valor predeterminado
        #lista_desplegable.set('8428-1A') #se utiliza set para definir un valor predeterminado
        #barra velocidad
        self.vel = Label(self.raiz,text='Velocidad', font= ('Helvetica 10 bold'),padx=60)
        self.vel.place(x=30,y=205) #posicionamos
        self.v = Scale(self.raiz,from_ = 0, to = 50, orient = HORIZONTAL) #definimos una escala para la velocidad que vaya de 0 a 255
        self.v.place(x=65,y=230) #posicionamos (agreagamos a pantalla)
        
        #barra acceleracion
        self.accel = Label(self.raiz,text='Acceleracion', font= ('Helvetica 10 bold'),padx=60)
        self.accel.place(x=30,y=275) #posicionamos
        self.a = Scale(self.raiz,from_ = 0, to = 40, orient = HORIZONTAL) #definimos una escala para la velocidad que vaya de 0 a 255
        self.a.place(x=65,y=300) #posicionamos(agreagamos a pantalla)
        
        #barra Torque
        self.tor = Label(self.raiz,text='Torque', font= ('Helvetica 10 bold'),padx=60)
        self.tor.place(x=30,y=345) #posicionamos
        self.t = Scale(self.raiz,from_ = 0, to = 20, orient = HORIZONTAL) #definimos una escala para la velocidad que vaya de 0 a 255
        self.t.place(x=65,y=370) #posicionamos (agreagamos a pantalla)
        
        #Botones
        self.button_start = Button(self.raiz,relief='raised',bd=5,bg='green',fg='white',activebackground = 'white',activeforeground = 'green',text = 'Start',font = ('DS-Digital 12'),width = 6,height = 2) #definimos el boton start
        self.button_stop= Button(self.raiz,relief='raised',bd=5,bg='orange',fg='white',activebackground = 'white',activeforeground = 'orange',text = 'Stop',font = ('DS-Digital 12'),width = 6,height = 2)#definimos el boton stop
        self.button_reset = Button(self.raiz,relief='raised',bd=5,bg='red',fg='white',activebackground = 'white',activeforeground = 'red',text = 'Reset',font = ('DS-Digital 12'),width = 6,height = 2) #definimos el boton reset
        self.button_zero_set = Button(self.raiz,relief='raised',bd=5,bg='blue',fg='white',activebackground = 'white',activeforeground = 'blue',text = 'Zero',font = ('DS-Digital 12'),width = 6,height = 2) #definimos el boton reset
        self.button_set_vel = Button(self.raiz,relief='raised',bd=5,bg='cyan',fg='black',activebackground = 'white',activeforeground = 'blue',text = 'Set',font = ('DS-Digital 12'),width = 5,height = 1)#,command = lambda:set_scale(v)) #definimos el boton set velocidad
        self.button_set_acc = Button(self.raiz,relief='raised',bd=5,bg='cyan',fg='black',activebackground = 'white',activeforeground = 'blue',text = 'Set',font = ('DS-Digital 12'),width = 5,height = 1) #definimos el boton set acceleracion
        self.button_set_tor = Button(self.raiz,relief='raised',bd=5,bg='cyan',fg='black',activebackground = 'white',activeforeground = 'blue',text = 'Set',font = ('DS-Digital 12'),width = 5,height = 1) #definimos el boton set torque
        #self.btn_save = Button(self.raiz, text= "Save", fg='black',activebackground = 'white',activeforeground = 'blue',width = 5,height = 1)#,command= lambda:save_file()) #definimos el boton save
        self.boton_obtener = Button(self.raiz, text= "seleccionar", fg='black',activebackground = 'white',activeforeground = 'red',width = 8,height = 1,command=obtener_info) #definimos el boton con el que obtendremos el valor de la lista desplegable
        #self.boton_min = Button(self.raiz, text="Minimizar", command=self.raiz.iconify) #boton para minimizar

        #separador
        self.sep = ttk.Separator(self.raiz,orient='horizontal')
        self.sep.place(x=30,y=10)
        #Posicionamiento
        self.button_start.place(x = 30,y = 450)
        self.button_stop.place(x = 110,y = 450)
        self.button_reset.place(x = 190,y = 450)
        self.button_zero_set.place(x = 110,y = 500)
        self.button_set_vel.place(x = 190,y = 235)
        self.button_set_acc.place(x = 190,y = 305)
        self.button_set_tor.place(x = 190,y = 375)
        #self.btn_save.place(x=115,y=505) 
        self.boton_obtener.place(x=210,y=80) 
        #self.boton_min.place(x=700,y=0) #boton para minimar app con iconify,util cuando se va a trabajar con varias ventanas deiconify(opuesto a iconify)
        self.raiz.mainloop()


def main():
    mi_app = Aplicacion()
    return 0


if __name__=='__main__':
        main()

