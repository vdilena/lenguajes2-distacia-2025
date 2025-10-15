from clases.Usuario import Usuario


class PublicoGeneral(Usuario):

    def __init__(self, nombre, credito):
        super().__init__(nombre)
        self.__dni = None
        self.__credito = credito

    # Getters
    @property
    def dni(self):
        return self.__dni
    
    @property
    def credito(self):
        return self.__credito
    
    # Setters
    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    @credito.setter
    def credito(self, credito):
        self.__credito = credito

    # Implemento el metodo abstracto
    def cumpleCondicionParaRetirarLibro(self):
        return self.__credito >= 500.00
    
    def tieneDocumentoParaRegistrarse(self):
        return self.__dni is not None