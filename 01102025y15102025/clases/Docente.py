
from clases.Usuario import Usuario


class Docente(Usuario):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        self.__credencial = None
        self.__libroPersonal = None
        self.__fechaClaseParticular = None
        self.__libreParaDarClases = True

    # Getters
    @property
    def credencial(self):
        return self.__credencial
    
    @property
    def libroPersonal(self):
        return self.__libroPersonal
    
    @property
    def fechaClaseParticular(self):
        return self.__fechaClaseParticular
    
    @property
    def libreParaDarClases(self):
        return self.__libreParaDarClases
    
    # Setters
    @credencial.setter
    def credencial(self, credencial):
        self.__credencial = credencial

    @libroPersonal.setter
    def libroPersonal(self, libroPersonal):
        self.__libroPersonal = libroPersonal

    @fechaClaseParticular.setter
    def fechaClaseParticular(self, fechaClaseParticular):
        self.__fechaClaseParticular = fechaClaseParticular

    @fechaClaseParticular.setter
    def libreParaDarClases(self, libreParaDarClases):
        self.__fechaClaseParticular = libreParaDarClases

    def ofrecerClaseParticular(self, fechaClase):
        self.__fechaClaseParticular = fechaClase
        self.__libreParaDarClases = False

    # Implemento el metodo abstracto
    def cumpleCondicionParaRetirarLibro(self):
        return self.__credencial is not None
    
    def tieneDocumentoParaRegistrarse(self):
        return self.__credencial is not None