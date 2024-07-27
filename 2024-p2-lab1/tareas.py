import csv
import os

class Tarea: # Creamos el objeto de clase Tarea
    def __init__(self, id, descripcion, prioridad, categoria = "General"): # Creamos el constructor del objeto de clase Tarea con los parámetros self, id, descripcion, prioridad y categoria
        # En el caso de que el usuario no cargue un valor str en el parametro categoria la misma va a tener como valor "General"
        self.id = id # Guardamos el parametro id en la variable self.id
        self.descripcion = descripcion # Guardamos el parametro descripcion en la variable self.descripcion
        self.prioridad = prioridad # Guardamos el parametro prioridad en la variable self.prioridad
        self.completada = False # Creamos una variable llamada self.completada donde cada nuevo objeto de la clase Tarea siempre va a empezar a tener como valor en dicha variable el valor False
        self.categoria = categoria # Guardamos el parametro categoria en la variable self.categoria

class Nodo: # Creamos el objeto de clase Nodo
    def __init__(self, tarea): # Creamos el constructor del objeto de clase Nodo con los parámetros self y tarea
        self.tarea = tarea # Guardamos el parametro tarea en la variable self.tarea
        self.siguiente = None # Creamos una variable llamada self.siguiente donde cada nuevo objeto de la clase Nodo siempre va a empezar a tener como valor en dicha variable el valor None

class ListaEnlazada: # Creamos el objeto de clase ListaEnlaazada
    def __init__(self): # Creamos el constructor del objeto de clase ListaEnalazada con el parametro self
        self.cabeza = None # Creamos una variable llamada self.cabeza donde cada nuevo objeto de la clase ListaEnalazada siempre va a empezar a tener como valor en dicha variable el valor None
        self.id_actual = 1 # Creamos una variable llamada self.id_actual donde cada nuevo objeto de la clase ListaEnalazada siempre va a empezar a tener como valor en dicha variable el valor 1
        self.contador_total = 0 # Agregamos una variable self.contador_total que guarda el valor int 0
        self.contador_prioridad1 = 0 # Agregamos una variable self.contador_prioridad1 que guarda el valor int 0
        self.contador_prioridad2 = 0 # Agregamos una variable self.contador_prioridad2 que guarda el valor int 0
        self.contador_prioridad3 = 0 # Agregamos una variable self.contador_prioridad3 que guarda el valor int 0
        self.contador_tareas_pendientes = 0 # Agregamos una variable self.contador_tareas_pendientes que guarda el valor int 0

    # Metodo que devuelve si la lista esta vacia o no
    def esta_vacia(self): # Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada esta_vacia pasandole como parametro self
        return self.cabeza is None # Retorna si self.cabeza es None, devolviendo True o False

    # Metodo para crear y guradar una tarea
    def agregar_tarea(self, descripcion, prioridad, categoria): # Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada agregar_tarea pasandole como parametro self, descripcion, prioridad y categoria
        if categoria != "": # Compara si el parametro categoria es distinto o no de string vacio. En el caso de que la condicion se cumpla ingresa al if
            tarea = Tarea(self.id_actual, descripcion, prioridad, categoria) # Guardamos en la variable tarea el objeto de la clase Tarea donde le pasamos los parametros self.id_actual, descripcion, prioridad y categoria
        else: #En el caso de que la condiion anterior no se cumpla, ingresa al else
            tarea = Tarea(self.id_actual, descripcion, prioridad) # Se crea una variable llamada tarea donde en este caso creamos el objeto de la clase Tarea pero excluyendo el parametro categoria
        nuevo_nodo = Nodo(tarea) # Guardamos en la variable nuevo_nodo el objeto de la clase Nodo pasandole como parámetro la variable tarea (es decir, el objeto creado de la clase Tarea)
        self.id_actual += 1 # Se incrementa el valor de self.id_actual que pertenece al constructor del objeto de la clase ListaEnlazada a +1

        if self.esta_vacia() or tarea.prioridad > self.cabeza.tarea.prioridad: # Se crea una condicion donde primero accede al metodo esta_vacia, devolviendo un Bool; la otra condicion es si la prioridad de la tarea creada es mayor a la prioridad de la tarea que se encuentra en la cabeza del objeto de la clase ListaEnlazada
            # Si alguna de las dos condiciones explicadas anteriormente dan como valor booleano True, ingresa al condicional if
            nuevo_nodo.siguiente = self.cabeza # En la variable nuevo_nodo que dentro del mismo esta guardado el objeto de la clase Nodo guarda en el self.siguiente el valor de self.cabeza
            self.cabeza = nuevo_nodo # En self.cabeza se guarda el objeto que se encuentra dentro de la variable nuevo_nodo 
        else: # Si ambas condiciones del if dan False, accede al else
            actual = self.cabeza # Creamos una variable actual donde guardamos self.cabeza
            while actual.siguiente is not None and actual.siguiente.tarea.prioridad >= tarea.prioridad: # Creamos un bucle cuando mientras el siguiente del valor de actual no sea None y que la prioridad de la tarea del siguiente de actual sea mayor o igual a la prioridad de la nueva tarea
                actual = actual.siguiente # Pisamos la variable actual donde ahora en vez de valer self.cabeza va a valer actual.siguiente (self.siguiente perteneciente a la clase Nodo)  
            nuevo_nodo.siguiente = actual.siguiente # En el siguiente del nuevo nodo que creamos guardamos el valor de la variable actual.siguiente
            actual.siguiente = nuevo_nodo # En actual.siguiente guardamos el valor del objeto nuevo_nodo
        
        self.contador_total += 1 # Se incrementa el valor guardado en self.contador_total a +1
        self.contador_tareas_pendientes += 1 # Se incrementa el valor guardado en self.contador_tareas_pendientes a +1
        
        if tarea.prioridad == 1: # Si la prioridad de la tarea es igual al valor 1 ingresa al if
            self.contador_prioridad1 += 1  # Se incrementa el valor de la variable self.contador_prioridad1 a +1
        elif tarea.prioridad == 2: # Si no se cumple el if anterior pero la prioridad de la tarea es igual al valor 2 ingresa al elif
            self.contador_prioridad2 += 1 # Se incrementa el valor de la variable self.contador_prioridad2 a +1
        else: # Si no se cumple tanto el if como el elif ingresa al else
            self.contador_prioridad3 += 1 # Se incrementa el valor de la variable self.contador_prioridad3 a +1
        print("Tarea agregada con éxito.") # Se muestra en pantalla el string "Tarea agregada con exito"
    
    # Metodo para buscar una tarea por su descrpcion, esto nos devuelve true o false para saber si la tarea ya fue creada
    def buscar_tarea_descripcion(self,text)->True: # Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada buscar_tarea_descripcion pasandole como parametro self y text
        actual = self.cabeza # Creamos la variable actual donde guardamos self.cabeza perteneciente de la clase ListaEnlazada
        encontrada = False # Creamos una variable encontrada donde guardamos como valor el booleano False
        while actual is not None: # En el ciclo while compara si actual no es None , es decir, si la lista no esta vacia. Si es true entra en el bucle
            if actual.tarea.descripcion.lower() == text.lower(): # Convierte el str del texto ingresado por el usuario y el str de la descripcion de la tarea en minusculas y lo compara. Si da True ingresa al if
                encontrada = True # Actualizamos el valor de la variable encontrada por el booleano True
            actual = actual.siguiente # Actualizamos el valor de la variable actual con el valor de actual.siguiente para que luego vuelva al ciclo while con el nuevo valor
        return encontrada # Cuando el ciclo while de false, se retorna el valor de la variable encontrada, de los cuales la misma puede ser True o False
    
    # Metodo para marcar una tarea como completada
    def completar_tarea(self, id): # Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada completar_tarea pasandole como parametro self e id 
        actual = self.cabeza # En la variable actual guardamos el valor de self.cabeza (siendo que aquí adentro tendremos guardado un objeto de clase Nodo)
        while actual is not None: # En el ciclo while compara si actual no es None, es decir, si la lista no esta vacia. Si es true entra en el bucle
            if actual.tarea.id == id: # Compara si el id de la tarea que se encuentra en self.cabeza es igual al id que le pasa el usuario
                actual.tarea.completada = True # Si se entra al condicional de la linea anterior se reemplaza el valor que se encuentra en la variable completada del objeto de la clase Tarea por True
                if actual.tarea.prioridad == 1: # Si la prioridad de la tarea guardada en la variable actual es igual a 1 ingresa al if
                    self.contador_prioridad1 -= 1 # Decrece el valor de la variable self.contador_prioridad1 a -1
                elif actual.tarea.prioridad == 2: # Si el if anterior no se cumple y el valor de la prioridad de la tarea es igual al 2 ingresa al elif
                    self.contador_prioridad2 -= 1 # Decrece el valor de la variable self.contador_prioridad2 a -1  
                else: # Si no se cumple tanto el if como el elif ingresa al else
                    self.contador_prioridad3 -= 1 # Decrece el valor de la variable self.contador_prioridad3 a -1
                self.contador_tareas_pendientes -= 1 # Decrece el valor de la variable self.contador_tareas_pendientes a -1
                return # Se utiliza el return para finalizar el método
            actual = actual.siguiente # Si el condicional de la linea 59 da como booleano False, cambia el valor de actual por el siguiente Nodo 
        print(f"Tarea con ID {id} no encontrada.") # En el caso de que el while de false, imprime en pantalla que la tarea con el id que le pasó el usuario no fue encontrada

    # Metodo para eliminar tareas
    def eliminar_tarea(self, id): # Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada eliminar_tarea pasandole como parametro self e id
        actual = self.cabeza # En la variable actual guardamos el valor de self.cabeza (siendo que aquí adentro tendremos guardado un objeto de clase Nodo)
        previo = None # Se crea la variable previo donde se guarda el valor None
        while actual is not None: # En el ciclo while compara si actual no es None, es decir, si self.cabeza no esta vacia. Si es true entra en el ciclo, si es False lo saltea
            if actual.tarea.id == id: # En el condicional if compara si el id de la tarea que se encuentra en self.cabeza es igual al id ingresado por el usuario. En el caso de que de True entra a este condicional
                if previo is None: # Se vuelve a crear un condicional donde compara si el valor de la variable previo es None. En el caso de que sea True entra en el condicional
                    self.cabeza = actual.siguiente # Ahora en self.cabeza guardamos el valor de actual.siguiente
                else: # Si la condicion mas cercana da como booleano False, ingresa al else
                    previo.siguiente = actual.siguiente # Actualizamos el valor de previo.siguiente y guardamos el valor de actual.siguiente
                self.contador_total -= 1 # Decrece el valor de la variable self.contador_total a -1
                
                if actual.tarea.completada == False: # Si el valor de la variable completada de la tarea es igual a False, ingresa al if
                    if actual.tarea.prioridad == 1: # Si la prioridad de la tarea guardada en la variable actual es igual a 1 ingresa al if
                        self.contador_prioridad1 -= 1 # Decrece el valor de la variable self.contador_prioridad1 a -1
                    elif actual.tarea.prioridad == 2: # Si el if anterior no se cumple y el valor de la prioridad de la tarea es igual al 2 ingresa al elif
                        self.contador_prioridad2 -= 1 # Decrece el valor de la variable self.contador_prioridad2 a -1  
                    else: # Si no se cumple tanto el if como el elif ingresa al else
                        self.contador_prioridad3 -= 1 # Decrece el valor de la variable self.contador_prioridad3 a -1
                    self.contador_tareas_pendientes -= 1 # Decrece el valor de la variable self.contador_tareas_pendientes a -1
                
                print(f"Tarea eliminada: {actual.tarea.descripcion}") # Imprimimos que la tarea fue eliminada con su respectiva descripcion
                return # Se utiliza el return para finalizar el método
            previo = actual # Se actualiza el valor de la variable previo por el valor de actual (siendo el nodo que se encuentra en self.cabeza) 
            actual = actual.siguiente # Actualiza el valor de actual con el valor de actual.siguiente (siendo actual un objeto de la clase Nodo)
        print(f"Tarea con ID {id} no encontrada.") # En el caso de que el ciclo while de false, imprime en pantalla que la tarea con el id que le pasó el usuario no fue encontrada

    # Metodo para mostrar todas las tareas creadas    
    def mostrar_tareas(self): # Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada mostrar_tareas pasandole como parametro self
        print("\n*** TAREAS ***") # Se imprime en pantalla el string *** TAREAS ***
        actual = self.cabeza # En la variable actual guardamos el valor de self.cabeza (siendo que aquí adentro tendremos guardado un objeto de clase Nodo)
        control = False # Se crea una variable llamada control donde guardamos el valor booleano False
        while actual is not None: # En el ciclo while compara si actual no es none, es decir, si la lista no esta vacia. Si es true entra en el bucle
            estado = "Completada" if actual.tarea.completada else "Pendiente" # Guarda el string "Completada" en la variable estado si el valor de la tarea completada en self.cabeza es True, en caso contrario guarda el str "Pendiente"
            print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}, Estado: {estado}") # Si se cumple la condicion de la linea anterior imprime todos los atributos de la clase tarea que se encuentran en el nodo, incluyendo la variable estado
            actual = actual.siguiente # Se reemplaza el valor de actual con el valor de actual.siguiente
            control = True # Se actualiza el valor de la variable control por el booleano True
        if control == False: # Se compara si el booleano de la variable control es False. Si dicha condicion da True, ingresa al if; si no, lo saltea
            print("No hay tareas existentes.") # Se imprime en la pantalla el str no hay tareas pendientes en el caso de que se haya ingresado al condicional de la linea anterior

    # Metodo para mostrar las tareas pendientes
    def mostrar_tareas_pendientes(self): # Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada mostrar_tareas_pendientes pasandole como parametro self
        print("\n*** TAREAS PENDIENTES ***") # Se imprime en pantalla el string *** TAREAS PENDIENTES ***
        actual = self.cabeza # En la variable actual guardamos el valor de self.cabeza (siendo que aquí adentro tendremos guardado un objeto de clase Nodo)
        control = False # Se crea una variable llamada control donde guardamos el valor booleano False
        while actual is not None: # En el ciclo while compara si actual no es none, es decir, si la lista no esta vacia. Si es true entra en el bucle
            if actual.tarea.completada == False: # Compara si el valor de la variable del objeto Tarea guardada en el Nodo en self.cabeza es igual a False. Si dicha condicion dd True, ingresa. Si no, la saltea
                print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}") # Si se cumple la condicion de la linea anterior imprime todos los atributos de la clase tarea que se encuentran en el nodo
                control = True # Se actualiza el valor de la variable control por el booleano True    
            actual = actual.siguiente # Se reemplaza el valor de actual con el valor de actual.siguiente
        if control == False: # Se compara si el booleano de la variable control es False. Si dicha condicion da True, ingresa al if; si no, lo saltea
            print("No hay tareas pendientes.") # Se imprime en la pantalla el str no hay tareas pendientes en el caso de que se haya ingresado al condicional de la linea anterior

    # Metodo para buscar tareas por su descripcion
    def mostrar_tareas_descripcion(self,text)->None: # Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada mostrar_tareas_descripcion pasandole como parametro self y text
        print("\n*** TAREAS ***") # Se imprime en pantalla el string *** TAREAS ***
        actual = self.cabeza # En la variable actual guardamos el valor de self.cabeza (siendo que aquí adentro tendremos guardado un objeto de clase Nodo)
        control = False # Se crea una variable llamada control donde guardamos el valor booleano False
        while actual is not None: # En el ciclo while compara si actual no es none, es decir, si la lista no esta vacia. Si es true entra en el bucle
            if actual.tarea.descripcion.lower() == text.lower(): # Convertimos los str del texto ingresado por el usuario y la descripcion de la tarea en la variable actual en minusculas. Si son iguales entra en el if
                print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Categoría: {actual.tarea.categoria}") # Si se cumple la condicion de la linea anterior imprime todos los atributos de la clase tarea que se encuentran en el nodo
                control = True # Se actualiza el valor de la variable control por el booleano True     
            actual = actual.siguiente # Se reemplaza el valor de actual con el valor de actual.siguiente
        if control == False: # Se compara si el booleano de la variable control es False. Si dicha condicion da True, ingresa al if; si no, lo saltea
            print(f"No existen tareas con descripcion {text}") # Se imprime en la pantalla el str no hay tareas existentes con la descripcion escrita por el usuario
    
    def mostrar_tareas_categoria(self,text)->None: # Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada mostrar_tareas_categoria pasandole como parametro self y text
        print("\n*** TAREAS ***") # Se imprime en pantalla el string *** TAREAS ***
        actual = self.cabeza # En la variable actual guardamos el valor de self.cabeza (siendo que aquí adentro tendremos guardado un objeto de clase Nodo)
        control = False # Se crea una variable llamada control donde guardamos el valor booleano False
        while actual is not None: # En el ciclo while compara si actual no es none, es decir, si la lista no esta vacia. Si es true entra en el bucle
            if actual.tarea.categoria.lower() == text.lower(): # Convertimos los str del texto ingresado por el usuario y la categoria de la tarea en la variable actual en minusculas. Si son iguales entra en el if
                estado = "Completada" if actual.tarea.completada else "Pendiente" # Guarda el string "Completada" en la variable estado si el valor de la tarea completada en self.cabeza es True, en caso contrario guarda el str "Pendiente"
                print(f"ID: {actual.tarea.id}, Descripción: {actual.tarea.descripcion}, Prioridad: {actual.tarea.prioridad}, Estado: {estado}") # Si se cumple la condicion de la linea anterior imprime todos los atributos y el estado
                control = True # Se actualiza el valor de la variable control por el booleano True     
            actual = actual.siguiente # Se reemplaza el valor de actual con el valor de actual.siguiente
        if control == False: # Se compara si el booleano de la variable control es False. Si dicha condicion da True, ingresa al if; si no, lo saltea
            print(f"No existen tareas con categoria {text}") # Se imprime en la pantalla el str no hay tareas existentes con la categoria escrita por el usuario
    
    # Metodo contar tareas pendientes lineal
    def contar_tareas_pendientes_lineal(self)->int: # Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada contar_tareas_pendientes (siendo de notacion O(n)) pasandole como parametro self
        actual = self.cabeza # En la variable actual guardamos el valor de self.cabeza (siendo que aquí adentro tendremos guardado un objeto de clase Nodo)
        contador_pendiente = 0 # Creamos la variable contador donde le asginamos dentro de la misma el valor entero 0
        while actual is not None: # En el ciclo while compara si actual no es none, es decir, si la lista no esta vacia. Si es true entra en el bucle
            if actual.tarea.completada == False: # Compara si el valor de la variable del objeto Tarea guardada en el Nodo en self.cabeza es igual a False. Si dicha condicion dd True, ingresa. Si no, la saltea
                contador_pendiente += 1 # En el caso de que el if de la linea anterior cumpla la condicion, se le suma a la variable contador_pendiente +1          
            actual = actual.siguiente # Se reemplaza el valor de actual con el valor de actual.siguiente
        return contador_pendiente # Cuando el ciclo while de False, retorna el valor de la variable contador_pendiente
    
    # Metodo contar tareas pendientes constante
    def contar_tareas_pendientes(self)->int: # Creamos un metodo dentro del objeto de la clase ListaEnlazada llamada contar_tareas_pendientes (siendo de notacion O(cte)) pasandole como parametro self
        return self.contador_tareas_pendientes # Retorna el valor de la variable self.contador_tareas_pendientes

    # Metodo para mostrar estadisticas
    def mostrar_estadisticas(self)->None: # Creamos el metodo mostrar_estadisticas dentro del objeto de la clase ListaEnlazada, pasandole como parametro self
        tareas_pendientes = self.contar_tareas_pendientes() # Guardamos en la variable tareas_pendientes el valor que devuelva el metodo contar_tareas_pendientes
        tareas_completadas = (100 * (self.contador_total - tareas_pendientes)) / self.contador_total # En la variable tareas_completadas guardamos el valor de la operacion 
        print(f"El porcentaje de las tareas completadas es: {tareas_completadas}%") # Se imprime en pantalla el str del porcentaje de las tareas completadas con su valor respectivo
        print(f"La cantidad de tareas pendientes es: \n- De prioridad 1: {self.contador_prioridad1} tarea/s.\n- De prioridad 2: {self.contador_prioridad2} tarea/s.\n- De prioridad 3: {self.contador_prioridad3} tarea/s.") # Se imprime en pantalla la cantidad de tareas pendientes con su respectiva prioridad
       
    # Carga y guardado de archivos
    def guardar_en_csv(self, archivo):
        with open(archivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            actual = self.cabeza
            while actual is not None:
                writer.writerow([actual.tarea.id, actual.tarea.descripcion, actual.tarea.prioridad, actual.tarea.categoria, actual.tarea.completada])
                actual = actual.siguiente
        print(f"Tareas guardadas en {archivo} con éxito.")

    def cargar_desde_csv(self, archivo):
        if not os.path.exists(archivo):
            print(f"Archivo {archivo} no encontrado.")
            return
        with open(archivo, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                id, descripcion, prioridad, categoria, completada = int(row[0]), row[1], int(row[2]), row[3], row[4] == 'True'
                tarea = Tarea(id, descripcion, prioridad, categoria)
                tarea.completada = completada
                self.agregar_tarea_existente(tarea)
            print(f"Tareas cargadas desde {archivo} con éxito.")
    
    # Metodo que sera utilizado por el cargar desde csv para crear nodos donde se guardaran las tareas y se agregaran a la lista enlazada
    def agregar_tarea_existente(self, tarea): # Se crea el metodo agregar_tarea_existente en el objeto de la clase ListaEnlazada donde recibe como parametros self y tarea
        nuevo_nodo = Nodo(tarea) # Se guarda en la variable nuevo_nodo el objeto de clase Nodo con el parametro tarea 
        if self.esta_vacia() or tarea.prioridad > self.cabeza.tarea.prioridad: # Accede al metodo self.esta_vacia devolviendo un booleano y compara si la prioridad de la tea es mayor a la prioridad de la tarea en self.cabeza
            # Si alguna de los booleanos da True, ingresa al if
            nuevo_nodo.siguiente = self.cabeza # En el siguiente de la variable nuevo_nodo se guarda el nodo de self.cabeza 
            self.cabeza = nuevo_nodo # En self.cabeza se guarda el objeto que se encuentra dentro de la variable nuevo_nodo
        else: # Si ambas condiciones del if dan False, ingresa al else
            actual = self.cabeza # En la variable actual guardamos el valor de self.cabeza
            while actual.siguiente is not None and actual.siguiente.tarea.prioridad >= tarea.prioridad: # Mientras el siguiente no sea None y la prioridad de la tarea en actual.siguiente sea mayor o igual a la prioridad de la nueva tarea, ingresa al ciclo while 
                actual = actual.siguiente # Se pisa la variable actual teniendo como nuevo valor el siguiente (self.siguiente)
            # Cuando el ciclo while de False, sale del mismo y sigue con las lineas del codigo que se encuentran dentro del metodo
            nuevo_nodo.siguiente = actual.siguiente # El valor del siguiente del nuevo_nodo es el valor del siguiente de la variable actual
            actual.siguiente = nuevo_nodo # El valor del siguiente del actual es ahora el nuevo_nodo
        
        if tarea.id >= self.id_actual: # Compara si el id de la tarea es mayor o igual al valor de la variable del constructor de la clase ListaEnlazada. Si da true ingresa al if
            self.id_actual = tarea.id + 1 # Se cambia el valor de la variable self.id_actual utilizando el valor del id de la tarea + 1
        
        self.contador_total += 1 # Se incrementa el valor de la variable self.contador_total a +1
        
        if nuevo_nodo.tarea.completada == False: # Si el valor de la variable completada de la tarea es igual a False, ingresa al if 
            if nuevo_nodo.tarea.prioridad == 1: # Si la prioridad de la tarea es igual al valor ingresa al if
                self.contador_prioridad1 += 1 # Se incrementa el valor de la variable self.contador_prioridad1 a +1
            elif nuevo_nodo.tarea.prioridad == 2: # Si no ingresa al if pero el valor de la prioridad es igual a 2 ingresa al elif
                self.contador_prioridad2 += 1 # Se incrementa el valor de la variable self.contador_prioridad2 a +1  
            else: # Si no se cumple las condiciones tanto del if como del elif ingresa al else
                self.contador_prioridad3 += 1 # Se incrementa el valor de la variable self.contador_prioridad3 a +1
            self.contador_tareas_pendientes += 1 # Se incrementa el valor de la variable self.contador_tareas_pendientes a +1

# Menu para el usuario
def menu(): # Definimos en el main del programa el procedimiento menu donde no se le pasa ningun parametro
    print("\nMenú:") # Imprime en pantalla el str Menú
    print("1. Agregar tarea") # Imprime en pantalla el str 1. Agregar tarea
    print("2. Completar tarea") # Imprime en pantalla el str 2. Completar tarea
    print("3. Eliminar tarea") # Imprime en pantalla el str 3. Eliminar tarea
    print("4. Mostrar todas las tareas") # Imprime en pantalla el str "4. Mostrar todas las tareas"
    print("5. Mostrar tareas pendientes") # Imprime en pantalla el str "5. Mostrar tareas pendientes"
    print("6. Mostrar tareas por descripcion") # Imprime en pantalla el str "6. Mostrar tareas por descripcion"
    print("7. Mostrar tareas por categoria") # Imprime en pantalla el str "7. Mostrar tareas por categoria"
    print("8. Contar tareas pendientes") # Imprime en pantalla el str "8. Contar tareas pendientes"
    print("9. Estadisticas") # Imprime en pantalla el str "9. Estadisticas"
    print("10. Guardar tareas en archivo CSV") # Imprime en pantalla el str "10. Guardar tareas en archivo CSV"
    print("11. Cargar tareas desde archivo CSV") # Imprime en pantalla el str "11. Cargar tareas desde archivo CSV" 
    print("12. Salir") # Imprime en pantalla el str "12. Salir"

# Segun la opcion que ingrese el usuario se ejecutara el medoto correspondiente

def main(): # Definimos en el main del programa el procedimiento main donde no se le pasa ningun parametro
    lista_tareas = ListaEnlazada() # Se guarda en la variable lista_tareas el objeto de la clase ListaEnlazada, donde no se le pasa ningun parametro
    archivo_csv = 'tareas.csv' # Se guarda en la variable archivo_csv el str tareas.csv

    # Cargar tareas desde CSV si el archivo existe
    lista_tareas.cargar_desde_csv(archivo_csv) # Crea una lista enlazada

    while True:
        menu()
        opcion = input("Seleccione una opción: ") # Se imprime por pantalla que ingrese una de las opciones anteriores
        
        if opcion == "1": # Si ingresa la opcion 1 entra al if
            control = False # Creamos la variable control con el valor false
            while control == False: # Si control es igual a false entra a la while
                descripcion = input("Ingrese la descripción de la tarea: ") # Mediante un input le pedimos al usuario que ingrese la descripcion de la tarea
                if descripcion != "": # Si la descripcion es distinto a un str vacio entra al if
                    if lista_tareas.buscar_tarea_descripcion(descripcion) == False: # Mediante el metodo buscar_tarea_descripcion busca si la tarea ya no fue creada si es false entra al if
                        error = True # Creamos la variable error y le guardamos el valor true
                        while error == True: # Si error es igual a true entra al  while                         
                            try: # Colocamos un try para manejar el error si el usuario ingresa un valor que no se pueda convertir en un int
                                prioridad = int(input("Ingrese la prioridad de la tarea (1 = baja, 2 = media, 3 = alta): ")) # Creamos la variable prioridad y le pedimos al usuario que ingrese 1, 2 o 3
                                while prioridad <= 0 or prioridad >= 4: # Si el numero ingresado es monor o ilgual a 0 y mayor igual que 4 ingresa al while
                                    prioridad = int(input("Numero no valido. Ingrese la prioridad de la tarea (1 = baja, 2 = media, 3 = alta):  ")) # Le imprime al usuario que el numero ingreso no es valido y que debe ingresar de nuevo el valor
                                categoria = input("Ingrese la categoría de la tarea: ") # Creamos la variable categoria y pedimos al usuario que ingrese la categoria de la tarea
                                lista_tareas.agregar_tarea(descripcion, prioridad, categoria) # Se llama al metodo agregar_tarea y se le pasan los parametros descripcion, prioridad, categoria
                                control = True # A la variable control le cambiamos el valor por true
                                error = False  # A la variable error le cambiamos el valor por false              
                            except ValueError: # Si la variable prioridad da un error ValueError ingresa
                                print("Debes ingresar una prioridad") # Se le imprime por pantalla que debe ingresar una prioridad
                    else: # Si no se cumple el ultimo if mas cercano, ingresa al else
                        des_existente = input(f"Tarea con descripcion {descripcion} ya existente. ¿Desea agregar una tarea? Responda con SI o NO: ") # Se le pide al usuario que ingrese un str y lo guarda en la variable des_existente
                        while des_existente.lower() != "si" and des_existente.lower() != "no": # Ingresa al ciclo while mientras el valor str de la variable des_existente (convirtiendolo en minuscula en minuscula) no sea ni si ni no
                            des_existente = input("Texto no valido. Debe escribir SI o NO: ") # Se le pide al usuario que ingrese un nuevo str actualizandose el valor de des_existente
                        if des_existente.lower() == "no": # Cuando sale del ciclo while compara si el str guardado en la variable des_existente (convirtiendolo en minuscula) es igual a no. Si da True ingresa al if
                            break # Finaliza el ciclo while
                else: # Si no ingresa al if de la misma sangria, ingresa al else
                    opcion_tarea = input("Debe escribir la descripcion de la tarea. ¿Desea agregar una tarea? Responda con SI o NO: ") # Se le pide al usuario que ingrese un valor str que sera guardado en la variable opcion_tarea
                    while opcion_tarea.lower() != "si" and opcion_tarea.lower() != "no": # Ingresa al ciclo while mientras el valor str de la variable opcion_tarea (convirtiendolo en minuscula en minuscula) no sea ni si ni no
                            opcion_tarea = input("Texto no valido. Debe escribir SI o NO: ") # Se le pide al usuario que ingrese un nuevo str actualizandose el valor de opcion_tarea
                    if opcion_tarea.lower() == "no": # Cuando sale del ciclo while compara si el str guardado en la variable opcion_tarea (convirtiendolo en minuscula en minuscula) es igual a no. Si da True ingresa al if
                        break # Finaliza el ciclo while
        
        elif opcion == "2": # Si ingresa la opcion 2 entra al elif
            control = False # Se declara una variable llamada "control"
            while control == False: # Se declara un ciclo while que compara si "control es igual a False"
                try: # Colocamos un try para manejar el error si el usuario ingresa un valor que no se pueda convertir en un int
                    id_tarea = int(input("Ingrese el ID de la tarea a completar: ")) # Se declara la variable id_tarea que guarda el input y lo convierte en un int
                    lista_tareas.completar_tarea(id_tarea) # Se llama a la lista enlazada con el metodo completar tarea y se le pasa el id_tarea
                    control = True # Se declara la variable control con un valor True
                    print("Tarea completada") # Se imprime en pantalla "Tarea completada"
                except ValueError: # Si la variable id_tarea da un error de tipo ValueError entra
                    print("No ingresaste un numero") # Se imprime por pantalla "No ingresaste un numero"
        
        elif opcion == "3": # Si el usuario ingresa la opcion 3, ingresa a este elif
            control = False # La variable control va a tener de valor booleano False
            while control == False: # Ingresa al ciclo while en el caso de que el valor de control sea igual a False
                try: # Colocamos un try para manejar un posible error en el caso de que el usuario ingrese un valor que no pueda ser convertido en un int
                    id_tarea = int(input("Ingrese el ID de la tarea a eliminar: ")) # En la variable id_tarea se le pide al usuario que ingrese un valor y se transforma en un entero
                    lista_tareas.eliminar_tarea(id_tarea) # Se invoca al metodo eliminar tarea de la clase ListaEnlazada pasandole el parametro id_tarea
                    control = True # Se cambia el valor de control pasando de False a True
                except ValueError: # Si la variable id_tarea da un error de tipo ValueError ingresa al except
                    print("No ingresaste un numero") # Imprime en pantalla el str de que el usuario no ingreso un numero y volviendo al ciclo while
        
        elif opcion == "4": # Si la opcion que ingresa el usuario es igual a 4, ingresa a este elif
            lista_tareas.mostrar_tareas() # Se llama al metodo mostrar_tareas de la clase ListaEnlazada
        
        elif opcion == "5": # Si la opcion que ingresa el usuario es igual a 5, ingresa a este elif
            lista_tareas.mostrar_tareas_pendientes() # Se llama al metodo mostrar_tareas_pendientes de la clase ListaEnlazada
        
        elif opcion == "6": # Si ingresa la opcion 6 entra al elif
            texto= input("Ingrese la descripcion de la tarea: ") # Se declara la variable texto que guarda un input 
            lista_tareas.mostrar_tareas_descripcion(texto) # Se llama a la lista enlazada y se ingresa al metodo mostrar_tareas_descripcion y se le pasa la variable texto
        
        elif opcion == "7": # Si la opcion que ingresa el usuario es igual a 7, ingresa a este elif
            texto= input("Ingrese la categoria de la tarea: ") # Se declara la variable texto que guarda un input 
            lista_tareas.mostrar_tareas_categoria(texto) # Se llama a la lista enlazada y se ingresa al metodo mostrar_tareas_categoria y se le pasa la variable texto

        elif opcion == "8": # Si la opcion que ingresa el usuario es igual a 8, ingresa a este elif
            total = lista_tareas.contar_tareas_pendientes() # Se llama al metodo contar_tareas_pendientes de la clase ListaEnlazada y se guarda su valor en la variable total
            print(f"Cantidad pendiente: {total} tarea/s.") # Imprime en pantalla el str de la cantidad de las tareas pendientes con el valor que se encuentra en la variable total
        
        elif opcion == "9": # Si ingresa la opcion 9 entra en el elif
            lista_tareas.mostrar_estadisticas() # Se llama a la lista enlazada y entra en el metodo de mostrar_estadisticas
        
        elif opcion == "10": # Si la opcion ingresada es 10 entra en el elif
            lista_tareas.guardar_en_csv(archivo_csv) # Llama al metodo guardar_en_csv y guarda todas las tareas creadas en el csv
        
        elif opcion == "11": # Si ingresa la opcion 11 entra en el elif
            lista_tareas.cargar_desde_csv(archivo_csv) #  Se llama a la lista enlazada y entra en el metodo cargar_desde_csv y se le pasa archivo_csv
        
        elif opcion == "12": # Si la opcion ingresada es 12 entra en el elif
            print("Saliendo del sistema de gestión de tareas.") # Imprime por pantalla que se esta saliendo del sistema
            break # Finaliza el while del menu
        
        else: # Si la opcion ingresada no es igual a ninguna de las anteriores ingresa al else
            print("Opción no válida. Por favor, seleccione una opción válida.") # Imprime por pantalla que la opcion no es valida


if __name__ == "__main__":
    main()
