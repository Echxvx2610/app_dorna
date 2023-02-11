from tkinter import *
from tkinter import ttk
import tkinter.ttk
from tkinter import filedialog as fd
# from PIL import Image, ImageTk
import webbrowser


class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title('Intrucciones de Trabajo')
        self.raiz.geometry('1920x1080')
        # self.raiz.configure(bg='SeaGreen1')
        # FRAME
        self.f_frame = Frame(self.raiz)  # Creacion del Frame
        self.f_frame.place(x=0, y=690)  # Empaquetamiento del Frame
        self.f_frame.config(bg="azure")  # cambiar color de fondo
        self.f_frame.config(width="300", height="300")  # cambiar tamaño
        self.f_frame.config(bd=20)  # cambiar el grosor del borde
        self.f_frame.config(relief="sunken")  # cambiar el tipo de borde
        self.f_frame.config(cursor="circle")  # cambiar el tipo de cursor
        # SECOND FRAME
        self.s_frame = Frame(self.raiz)  # Creacion del Frame
        self.s_frame.place(x=0, y=0)  # Empaquetamiento del Frame
        self.s_frame.config(bg="azure")  # cambiar color de fondo
        self.s_frame.config(width="1920", height="700")  # cambiar tamaño
        self.s_frame.config(bd=20)  # cambiar el grosor del borde
        self.s_frame.config(relief="sunken")  # cambiar el tipo de borde
        self.s_frame.config(cursor="circle")  # cambiar el tipo de cursor
        # THIRD FRAME
        self.t_frame = Frame(self.raiz)  # Creacion del Frame
        self.t_frame.place(x=300, y=690)  # Empaquetamiento del Frame
        self.t_frame.config(bg="azure")  # cambiar color de fondo
        self.t_frame.config(width="1610", height="300")  # cambiar tamaño
        self.t_frame.config(bd=20)  # cambiar el grosor del borde
        self.t_frame.config(relief="sunken")  # cambiar el tipo de borde
        self.t_frame.config(cursor="circle")  # cambiar el tipo de cursor

        # FUNCIONES
        def obtener_info():
            if self.lista_desplegable.get() == '8428-1A':
                print('se ha seleccionado un ensamble,Valida tu JOB LIST')
                self.top = Toplevel(self.raiz)
                self.top.title('Notas')
                self.top.geometry('300x300')
                self.top.configure(bg='black')
                self.notas = Text(self.top, font=('Calibri', 12), borderwidth=1, relief='solid', bg='white')
                self.notas.place(x=30, y=10, width=240, height=250)
                self.btn_save = Button(self.top, text="Save", fg='black', activebackground='white',
                                       activeforeground='blue', width=5, height=1,
                                       command=save_file)  # definimos el boton save
                self.btn_save.place(x=30, y=265)
                self.btn_exit = Button(self.top, text="Exit", fg='black', activebackground='white',
                                       activeforeground='blue', width=5, height=1,
                                       command=Exit)  # definimos el boton save
                self.btn_exit.place(x=130, y=265)
                self.btn_delete = Button(self.top, text="Delete", fg='black', activebackground='white',
                                         activeforeground='blue', width=5, height=1,
                                         command=delete)  # definimos el boton save
                self.btn_delete.place(x=220, y=265)
                self.raiz.iconify()
            print(
                self.lista_desplegable.get())  # esta funcion es para obtener el valor del item seleccionado en la lista desplegable, usamos .get() para tomar el valor

        def new_window():
            self.top = Toplevel(self.raiz)  # esta funcion es para abrir una nueva ventana al presionar dicho boton
            self.top.title('Notas')
            self.top.geometry('300x300')
            self.top.configure(bg='black')
            self.notas = Text(self.top, font=('Calibri', 12), borderwidth=1, relief='solid', bg='white')
            self.notas.place(x=30, y=10, width=240, height=250)
            self.btn_save = Button(self.top, text="Save", fg='black', activebackground='white', activeforeground='blue',
                                   width=5, height=1, command=save_file)  # definimos el boton save
            self.btn_save.place(x=30, y=265)
            self.btn_exit = Button(self.top, text="Exit", fg='black', activebackground='white', activeforeground='blue',
                                   width=5, height=1, command=Exit)  # definimos el boton save
            self.btn_exit.place(x=130, y=265)
            self.btn_delete = Button(self.top, text="Delete", fg='black', activebackground='white',
                                     activeforeground='blue', width=5, height=1,
                                     command=delete)  # definimos el boton save
            self.btn_delete.place(x=220, y=265)

            self.raiz.iconify()  # minimiza ventana principal

        # Define the function/guardar archivo/abruir archivo
        def open_file():  # funcion para mostrar y ver el contenido del mismo
            f = open('H:/Temporal/Echevarria/estado_robot.txt')  # abre un archivo en modo lectura
            filetypes = (('text files', '*.txt'), ('All files', '*.*'))
            filename = fd.askopenfilename(
                title='Open a file',
                initialdir='/',
                filetypes=filetypes)
            print('Archivo abierto')
            print(f.read())  # read() lee todo el texto como una cadena.

        def save_file():  # funcion para guardar el texto mostrado en la etiqueta de texto
            with open(r'H:/Temporal/Echevarria/estado_robot.txt',
                      'a') as f:  # abre un archivo y lo sobreescribe,si no hay lo crea y escribe
                f.write(self.notas.get(1.0, 'end-1c'))
                f.write('\n')  # salto de linea
            filetypes = (('text files', '*.txt'), ('All files', '*.*'))
            filename = fd.asksaveasfilename(
                title='Save a file',
                initialdir='/',
                filetypes=filetypes)
            print('Archivo Guardado')

        def Exit():  # funcion para cerrar ventana top y volver a maximizar ventana raiz
            self.top.destroy()  # cierra top
            self.raiz.deiconify()  # abre raiz

        def delete():  # borrar contenido de una etiqueta Text
            self.notas.delete('1.0', 'end')

        def about_window():
            dorna_web = webbrowser.open('https://doc.dorna.ai/')

        def bin():
            state = '1'
            print(state)

        # def inst():
        # img = ImageTk.PhotoImage(Image.Open('paso-1'))
        # self.paso = Label(self.S_frame,Image = img)
        # self.paso.pack()
        # i = PhotoImage(file='paso-1.png')#definimos imagen
        # self.image_view = Label(self.s_frame,image = i)#creamos etiqueta para imagen
        # self.image_view.place(x=10,y=20)#posicionamos

        def instruccion():
            self.i = PhotoImage(file='paso-1.png')  # definimos imagen

            self.image_view = Label(self.s_frame, image=self.i)  # creamos etiqueta para imagen
            self.image_view.place(x=10, y=10)

        # MENUS
        self.menu = Menu(self.raiz)
        self.raiz.config(menu=self.menu)
        filemenu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='New window', command=new_window)
        filemenu.add_command(label='Open register..', command=open_file)
        filemenu.add_separator()
        filemenu.add_command(label='Exit',
                             command=self.raiz.destroy)  # definimos que al dar click en exite se cerrara la aplicacion
        helpmenu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='Help', menu=helpmenu)
        helpmenu.add_command(label='About', command=about_window)

        # LSITA DESPLEGABLE
        # etiqueta seleccion
        self.seleccion = Label(self.raiz, text="Seleccione el numero de ensamble", font=('Sans 10 bold'), padx=10)
        self.seleccion.place(x=30, y=725)  # posicionamos
        # lista
        self.lista_desplegable = ttk.Combobox(self.raiz,
                                              width=17)  # si no queremos agregar nuevos items a la lista usamos state='readonly' dentro de los ()
        self.lista_desplegable.place(x=55, y=760)
        opciones = ["8428-1A", "9316-1B", "9435-1C", "27117-1B"]
        self.lista_desplegable['values'] = opciones

        # ETIQUETAS
        self.seleccion = Label(self.raiz, text="Instruccion de Trabajo", font=('Sans 10 bold'), padx=10)
        self.seleccion.place(x=880, y=10)  # posicionamos
        self.seleccion = Label(self.raiz, text="Sensores No.Parte", font=('Sans 10 bold'), padx=10)
        self.seleccion.place(x=480, y=700)  # posicionamos

        # BOTONES
        self.boton_obtener = Button(self.raiz, relief='raised', bd=5, bg='gold', fg='black',
                                    activebackground='spring green', activeforeground='black', text="Seleccionar",
                                    width=8, height=1,
                                    command=obtener_info)  # definimos el boton con el que obtendremos el valor de la lista desplegable
        self.sensor1 = Button(self.raiz, relief='raised', bd=5, bg='IndianRed1', fg='white',
                              activebackground='RoyalBlue1', activeforeground='white', text="Sensor-1", width=8,
                              height=1, command=instruccion)
        self.sensor2 = Button(self.raiz, relief='raised', bd=5, bg='IndianRed1', fg='white',
                              activebackground='RoyalBlue1', activeforeground='white', text="Sensor-2", width=8,
                              height=1, command=bin)
        self.sensor3 = Button(self.raiz, relief='raised', bd=5, bg='IndianRed1', fg='white',
                              activebackground='RoyalBlue1', activeforeground='white', text="Sensor-3", width=8,
                              height=1, command=bin)
        self.sensor4 = Button(self.raiz, relief='raised', bd=5, bg='IndianRed1', fg='white',
                              activebackground='RoyalBlue1', activeforeground='white', text="Sensor-4", width=8,
                              height=1, command=bin)
        self.sensor5 = Button(self.raiz, relief='raised', bd=5, bg='IndianRed1', fg='white',
                              activebackground='RoyalBlue1', activeforeground='white', text="Sensor-5", width=8,
                              height=1, command=bin)
        self.sensor6 = Button(self.raiz, relief='raised', bd=5, bg='IndianRed1', fg='white',
                              activebackground='RoyalBlue1', activeforeground='white', text="Sensor-6", width=8,
                              height=1, command=bin)
        self.sensor7 = Button(self.raiz, relief='raised', bd=5, bg='IndianRed1', fg='white',
                              activebackground='RoyalBlue1', activeforeground='white', text="Sensor-7", width=8,
                              height=1, command=bin)
        self.sensor8 = Button(self.raiz, relief='raised', bd=5, bg='IndianRed1', fg='white',
                              activebackground='RoyalBlue1', activeforeground='white', text="Sensor-8", width=8,
                              height=1, command=bin)
        self.sensor9 = Button(self.raiz, relief='raised', bd=5, bg='IndianRed1', fg='white',
                              activebackground='RoyalBlue1', activeforeground='white', text="Sensor-9", width=8,
                              height=1, command=bin)
        self.sensor10 = Button(self.raiz, relief='raised', bd=5, bg='IndianRed1', fg='white',
                               activebackground='RoyalBlue1', activeforeground='white', text="Sensor-10", width=8,
                               height=1, command=bin)

        # RADIOBOTONES
        # var = BooleanVar()
        # self.radioS1 = Radiobutton(self.raiz,variable = var, value=self.sensor1)
        # self.radioS2 = Radiobutton(self.raiz,variable = var, value=self.sensor2)
        # self.radioS3 = Radiobutton(self.raiz,variable = var, value=self.sensor3)
        # self.radioS4 = Radiobutton(self.raiz,variable = var, value=self.sensor4)
        # self.radioS5 = Radiobutton(self.raiz,variable = var, value=self.sensor5)
        # self.radioS6 = Radiobutton(self.raiz,variable = var, value=self.sensor6)
        # self.radioS7 = Radiobutton(self.raiz,variable = var, value=self.sensor7)
        # self.radioS8 = Radiobutton(self.raiz,variable = var, value=self.sensor8)
        # self.radioS9 = Radiobutton(self.raiz,variable = var, value=self.sensor9)
        # self.radioS10 = Radiobutton(self.raiz,variable = var, value=self.sensor10)

        # Posicionamiento de botones
        self.boton_obtener.place(x=200, y=755)
        self.sensor1.place(x=360, y=790)
        self.sensor2.place(x=460, y=790)
        self.sensor3.place(x=560, y=790)
        self.sensor4.place(x=660, y=790)
        self.sensor5.place(x=360, y=840)
        self.sensor6.place(x=460, y=840)
        self.sensor7.place(x=560, y=840)
        self.sensor8.place(x=660, y=840)
        self.sensor9.place(x=760, y=790)
        self.sensor10.place(x=760, y=840)

        self.raiz.mainloop()


def main():
    app = Aplicacion()
    return 0


if __name__ == '__main__':
    main()
