from tkinter import *

dic_alumnos = {} 

def no_es_letra(palabra):
        return any(not letra.isalpha() for letra in palabra)

class Aplicacion(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=400, height=300)
        self.master = master
        self.pack()
        self.create_widgets()

    def mostrar_alumnos(self):
        if len(dic_alumnos) <= 0:
            print("Aún no hay alumnos en la lista\n")
        else:
            for clave in dic_alumnos:
                print(f"El alumno {clave}, está inscripto en esta cantidad de cursos: {dic_alumnos.get(clave)}")
            print("\n")

    def agregar_alumno(self):
        try:
            self.n1 = self.txt_alum.get().title()
            self.n2 = int(self.txt_curso.get())
            
            if no_es_letra(self.n1) == True ^ (len(self.n1) <=0 or len(str(self.n2)) <=0):
                print("Por favor, vuelve a ingresar los datos correctamente\n")
            else: 
                dic_alumnos[self.n1] = self.n2
                print("¡El alumno fue añadido!")
                
        except ValueError:
            print("Por favor, vuelve a ingresar los datos correctamente\n")

    def buscar(self):
        clave = self.txt_alum.get().title()
        
        try:
            if clave in dic_alumnos:
                print("La cantidad de cursos del alumno es de: ", dic_alumnos.get(clave))
            elif clave not in dic_alumnos:
                print("Lo siento, el nombre no se encuentra en la base de datos")
                
        except TypeError:
            print("Por favor, ingresa el nombre del alumno")

    def create_widgets(self):
        self.btn_alum = Button(self, text="Ver lista de alumnos", command = self.mostrar_alumnos)
        self.btn_alum.place(x=10, y=10)
        
        self.nom_alum = Label(self, text="Nombre Alumno:")
        self.nom_alum.place(x=10,y=55,width=100, height=30)
        
        self.txt_alum = Entry(self)
        self.txt_alum.place(x=120, y=60)
        
        self.curso_label = Label(self, text="Cursos:")
        self.curso_label.place(x=10, y=100)
        
        self.txt_curso = Entry(self)
        self.txt_curso.place(x=120, y=100)
        
        self.btn_agreg_list = Button(self, text="Agregar a la lista", command = self.agregar_alumno)
        self.btn_agreg_list.place(x=10, y=150)
        self.btn_cant_cursos = Button(self, text="Ver cantidad de cursos", command = self.buscar)
        self.btn_cant_cursos.place(x=120, y=150)

if __name__ == '__main__':
    root = Tk()
    root.wm_title("Universidad - EducacionIT")
    app = Aplicacion(root) 
    app.mainloop()