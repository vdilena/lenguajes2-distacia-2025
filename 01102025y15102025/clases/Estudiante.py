
from clases.Usuario import Usuario


class Estudiante(Usuario):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        self.__libreta = None
        self.__resumen = None

    # Getters
    @property
    def libreta(self):
        return self.__libreta
    
    @property
    def resumen(self):
        return self.__resumen
    
    # Setters
    @libreta.setter
    def libreta(self, libreta):
        self.__libreta = libreta

    @resumen.setter
    def resumen(self, resumen):
        self.__resumen = resumen

    def dejarResumen(self):
        return self.__resumen

    # Implemento el metodo abstracto
    def cumpleCondicionParaRetirarLibro(self):
        return self.__libreta is not None
    
    def tieneDocumentoParaRegistrarse(self):
        return self.__libreta is not None