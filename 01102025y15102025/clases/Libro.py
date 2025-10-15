

class Libro:

    # Constructor con metodo dunder
    def __init__(self, titulo, autor):
        
        # Atributos (título, autor y estado (prestado/disponible).)
        self.__titulo = titulo
        self.__autor = autor
        self.__estado = "DISPONIBLE"

    # Getters
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def autor(self):
        return self.__autor
    
    @property
    def estado(self):
        return self.__estado
    
    # Setters
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    # Metodo dunder para mostrar datos de libro
    def __str__(self):
        return f"Titulo: {self.__titulo}, Autor: {self.__autor}, Estado: {self.__estado}"
    
    def reservarLibro(self):
        self.__estado = "PRESTADO"

    def disponibilizarLibro(self):
        self.__estado = "DISPONIBLE"

    