from abc import ABC, abstractmethod
from typing import List
from clases.Libro import Libro

# La defino como clase abstracta
class Usuario(ABC):

    # dunder constructor
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__libro = None

    # Getters
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def libro(self):
        return self.__libro
    
    # Setters
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @libro.setter
    def libro(self, libro):
        self.__libros= libro

    def pedirUnLibro(self, libro: Libro):
        if self.cumpleCondicionParaRetirarLibro():
            libro.reservarLibro()
            self.__libro = libro
    
    def devolverLibro(self, libro):
        self.__libro = None

    # Defino un metodo abstracto
    @abstractmethod
    def cumpleCondicionParaRetirarLibro(self):
        return True

    @abstractmethod
    def tieneDocumentoParaRegistrarse(self):
        pass

    def __str__(self):
        return f"Nombre: {self.__nombre}, Libro reservado: {"" if self.__libro is None else  self.__libro }"
    