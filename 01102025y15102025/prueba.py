from clases.Libro import Libro
from clases.PublicoGeneral import PublicoGeneral
from clases.Estudiante import Estudiante
from clases.Docente import Docente
from clases.Biblioteca import Biblioteca

# Pruebas de objetos

# Creo libros
unLibro = Libro("1984", "Orwell")
#print(unLibro)
unLibro.titulo = "Cronicas de una muete anunciada"
unLibro.autor = "Garcia Marquez"
unLibro.estado = "PRESTADO"
#print(unLibro)
otroLibro = Libro("1984", "Orwell")
unLibroMas = Libro("Mi Libro", "Oscar Gomez")

# Creo estudiantes
unUsuarioGeneral = PublicoGeneral("Juan Perez", 9000.00)
unEstudiante = Estudiante("Carolina Gimenez")
unEstudiante.libreta = 54654221
unDocente = Docente("Oscar Gomez")

# Creo biblioteca, cargo libros y usuarios
biblioteca = Biblioteca()
biblioteca.registrarLibro(unLibro)
biblioteca.registrarLibro(otroLibro)
biblioteca.registrarLibro(unLibroMas)

biblioteca.registrarUsuario(unUsuarioGeneral)
biblioteca.registrarUsuario(unEstudiante)
biblioteca.registrarUsuario(unDocente)

# Antes de reserva
biblioteca.mostrarUsuarios()
biblioteca.mostrarLibros()

biblioteca.prestarLibro(otroLibro, unEstudiante)

# Despues de reserva
biblioteca.mostrarUsuarios()
biblioteca.mostrarLibros()

