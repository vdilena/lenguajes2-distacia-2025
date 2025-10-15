
from typing import List
from clases.Libro import Libro
from clases.Usuario import Usuario


class Biblioteca:
    
    def __init__(self):
        self.__libros: List[Libro] = []
        self.__usuarios: List[Usuario] = []

    def registrarLibro(self, libro: Libro):
        self.__libros.append(libro)

    def registrarUsuario(self, usuario: Usuario):

        if usuario.tieneDocumentoParaRegistrarse():
            self.__usuarios.append(usuario)

    def obtenerLibro(self, libro: Libro):
        for l in self.__libros:
            if libro.titulo == l.titulo:
                return l
            
    def obtenerUsuario(self, usuario: Usuario):
        for u in self.__usuarios:
            if usuario.nombre == u.nombre:
                return u

    def prestarLibro(self, libro: Libro, usuario: Usuario):

        usuarioEncontrado = self.obtenerUsuario(usuario)
        libroEncontrado = self.obtenerLibro(libro)
        if usuarioEncontrado is not None and libroEncontrado is not None and libroEncontrado.estado == "DISPONIBLE":
            usuarioEncontrado.pedirUnLibro(libroEncontrado)

    def devolverLibro(self, libro: Libro, usuario: Usuario):

        usuarioEncontrado = self.obtenerUsuario(usuario)
        libroEncontrado = self.obtenerLibro(libro)
        if usuarioEncontrado is not None and libroEncontrado is not None:
            libroEncontrado.disponibilizarLibro()
            usuarioEncontrado.devolverLibro(libroEncontrado)

    def mostrarUsuarios(self):
        for usuario in self.__usuarios:
            print(usuario)

    def mostrarLibros(self):
        for libro in self.__libros:
            print(libro)