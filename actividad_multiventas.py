import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton, QVBoxLayout, QDateEdit, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette

class VentanaFormulario(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Afiliados - Chacarita Juniors")
        self.setGeometry(100, 100, 500, 350)
        layout = QGridLayout()
        self.setLayout(layout)
        tittle = QLabel("Formulario de Afiliación")
        tittle.setAlignment(Qt.AlignCenter)
        layout.addWidget(tittle, 0, 0, 1, 2)
        self.name_label = QLabel("Nombre:")
        self.lastname_label = QLabel("Apellido:")
        self.dni_label = QLabel("DNI:")
        self.birthday_label = QLabel("Fecha de nacimiento:")
        self.name_input = QLineEdit()
        self.lastname_input = QLineEdit()
        self.dni_input = QLineEdit()
        self.birthday_date = QDateEdit()

        layout.addWidget(self.name_label, 1, 0)
        layout.addWidget(self.name_input, 1, 1)  
        layout.addWidget(self.lastname_label, 2, 0)
        layout.addWidget(self.lastname_input, 2, 1)
        layout.addWidget(self.dni_label, 3, 0)
        layout.addWidget(self.dni_input, 3, 1)
        layout.addWidget(self.birthday_label, 4, 0)
        layout.addWidget(self.birthday_date, 4, 1)   

        #patron de colores de chacarita, detallito para el profe je
        self.name_input.setStyleSheet("background-color: #000000; color: white;")
        self.lastname_input.setStyleSheet("background-color: #000000; color: white;")
        self.dni_input.setStyleSheet("background-color: #000000; color: white;")
        self.birthday_date.setStyleSheet("background-color: #000000; color: white;")

        tittle.setFont(QFont('Arial', 24, QFont.Bold))
        self.name_label.setFont(QFont('Arial', 12))
        self.lastname_label.setFont(QFont('Arial', 12))
        self.dni_label.setFont(QFont('Arial', 12))
        self.birthday_label.setFont(QFont('Arial', 12))

        paleta = QPalette()
        paleta.setColor(QPalette.Window, Qt.red)
        self.setAutoFillBackground(True)
        self.setPalette(paleta) 

    def mostar_datos(self):
        datos = (
            f"Nombre: {self.name_input.text()}\n"
            f"Apellido: {self.lastname_input.text()}\n"
            f"DNI: {self.dni_input.text()}\n"
            f"Fecha de nacimiento: {self.birthday_date.date().toString('dd/MM/yyyy')}"
        )
        QMessageBox.information(self, "Datos del afiliado", datos)

    def cerrar(self):
        self.close()


class VentanaHerramientas(QWidget):
    def __init__(self, ventana_formulario): 
        super().__init__()
        self.ventana_formulario = ventana_formulario 
        self.setWindowTitle("Herramientas")
        self.setGeometry(650, 100, 200, 300)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.guardar = QPushButton('guardar')
        self.abrir = QPushButton('abrir')
        self.buscar = QPushButton('buscar')
        self.salir = QPushButton('salir')
        layout.addWidget(self.guardar)
        layout.addWidget(self.abrir) 
        layout.addWidget(self.buscar)
        layout.addWidget(self.salir)

        self.guardar.clicked.connect(self.guardar_datos)  
        self.salir.clicked.connect(self.cerrar)
        self.buscar.clicked.connect(self.buscar_mensaje)

        self.guardar.setStyleSheet("background-color: #000000; color: white;")
        self.abrir.setStyleSheet("background-color: #000000; color: white;")
        self.buscar.setStyleSheet("background-color: #000000; color: white;")
        self.salir.setStyleSheet("background-color: #000000; color: white;")

        paleta = QPalette()
        paleta.setColor(QPalette.Window, Qt.red)
        self.setAutoFillBackground(True)
        self.setPalette(paleta) 

    def buscar_mensaje(self):
        mensaje= "no sea malo profe..."
        QMessageBox.information(self, "Buscar", mensaje)

    def check(self):

        if (not self.ventana_formulario.name_input.text().strip() or 
            not self.ventana_formulario.lastname_input.text().strip() or 
            not self.ventana_formulario.dni_input.text().strip()):
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos obligatorios.")
            return False
        return True

    def guardar_datos(self):
        if self.check():
            self.ventana_formulario.mostar_datos()

    def cerrar(self):
        self.ventana_formulario.close()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana_form = VentanaFormulario()
    ventana_herr = VentanaHerramientas(ventana_form) 
    ventana_herr.show()
    ventana_form.show()
    sys.exit(app.exec_())


# Práctico PyQt5: Uso de múltiples ventanas (Herramientas y Contexto)
# -------------------------------------------------------------------
#
# Objetivo: Aprender a crear y manejar dos ventanas simultáneas en PyQt5.
# Una ventana será de herramientas (con botones como Guardar, Abrir, Buscar, etc.)
# y la otra mostrará el contexto: un formulario de afiliados al Club Atlético Chacarita Juniors.
#
# Cada ejercicio suma widgets y lógica, guiando al alumno en el uso de PyQt5, QGridLayout y manejo de ventanas.
#
# -----------------------------------------------------------------------------
# Ejercicio 1: Crear la ventana de contexto (formulario de afiliados)
# -----------------------------------------------------------------------------
# Teoría:
# - QWidget es la base para crear ventanas.
# - QGridLayout organiza los widgets en filas y columnas.
# - QLabel y QLineEdit permiten mostrar e ingresar datos.
#
# Consigna:
# - Crear una ventana principal (QWidget) de 500x350, título "Afiliados - Chacarita Juniors".
# - Agregar QLabel grande y centrado: "Formulario de Afiliación".
# - Agregar QLabel y QLineEdit para Nombre, Apellido, DNI y Fecha de nacimiento.
#
# -----------------------------------------------------------------------------
# Ejercicio 2: Crear la ventana de herramientas
# -----------------------------------------------------------------------------
# Teoría:
# - Otra instancia de QWidget puede funcionar como ventana secundaria.
# - QPushButton permite crear botones de acción.
# - QVBoxLayout organiza widgets en columna.
#
# Consigna:
# - Crear una ventana secundaria de 200x300, título "Herramientas".
# - Agregar botones: "Guardar", "Abrir", "Buscar", "Salir".
#
# -----------------------------------------------------------------------------
# Ejercicio 3: Mostrar ambas ventanas a la vez
# -----------------------------------------------------------------------------
# Teoría:
# - Puedes crear y mostrar varias ventanas instanciando varias clases QWidget.
# - show() en cada ventana las hace visibles simultáneamente.
#
# Consigna:
# - Modifica el script para que ambas ventanas se muestren al ejecutar el programa.
#
# -----------------------------------------------------------------------------
# Ejercicio 4: Conectar botones de herramientas con el formulario
# -----------------------------------------------------------------------------
# Teoría:
# - Los botones pueden ejecutar funciones que interactúan con la otra ventana.
# - Puedes pasar referencias entre ventanas para manipular datos.
#
# Consigna:
# - Haz que el botón "Guardar" muestre un mensaje con los datos ingresados en el formulario.
# - El botón "Salir" debe cerrar ambas ventanas.
#
# -----------------------------------------------------------------------------
# Ejercicio 5: Personalización visual y validaciones
# -----------------------------------------------------------------------------
# Consigna:
# - Cambia colores, fuentes y tamaño de los widgets para una interfaz moderna.
# - Valida que los campos obligatorios estén completos antes de guardar.
#
# -----------------------------------------------------------------------------
# Sugerencia:
# - Usa QDateEdit para la fecha de nacimiento.
# - Usa QMessageBox para mostrar mensajes.
#
# -----------------------------------------------------------------------------
# Esqueleto inicial:
