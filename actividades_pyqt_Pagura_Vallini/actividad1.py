# Práctico PyQt5: Construcción guiada de una interfaz completa
# ------------------------------------------------------------
#
# Objetivo: Construir paso a paso un formulario de registro moderno y funcional.
# Cada ejercicio suma widgets y lógica, guiando al alumno en el uso de PyQt5 y QGridLayout.
#
# -----------------------------------------------------------------------------
# Ejercicio 1: Estructura básica y primer campo
# -----------------------------------------------------------------------------
# Teoría:
# - QLabel muestra texto en la interfaz.
# - QLineEdit permite ingresar texto.
# - QGridLayout organiza los widgets en filas y columnas.
#
# Consigna:
# - Ventana 400x300, título “Registro de Usuario”.
# - QLabel grande y centrado: “Formulario de Registro”.
# - QLabel “Nombre:” y QLineEdit al lado, usando QGridLayout.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout , QRadioButton, QComboBox , QCheckBox , QPushButton , QMessageBox 
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtWidgets import QButtonGroup

class Ventana(QWidget):
    def __init__(self):
        #EJERCICIO 1
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 400, 300)
        layout = QGridLayout()
        self.setLayout(layout)
        titulo= QLabel("Formulario Registro") 
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setFont(QFont('Arial', 30, QFont.Bold))
        layout.addWidget(titulo, 0, 0, 1, 2)
        nombre_label = QLabel("Nombre:")
        nombre_input = QLineEdit()
        layout.addWidget(nombre_label, 1, 0)
        layout.addWidget(nombre_input, 1, 1)


        # COMPLETAR: Crear QLabel grande y centrado ("Formulario de Registro")
        # COMPLETAR: Crear QLabel "Nombre:" y QLineEdit al lado
        # layout.addWidget(...)


# -----------------------------------------------------------------------------
# Ejercicio 2: Más campos de texto
# -----------------------------------------------------------------------------
# Teoría:
# - QLineEdit puede usarse para email y contraseña.
# - setEchoMode(QLineEdit.Password) oculta el texto del input.
#
# Consigna:
# - Agregar debajo los campos “Email:” y “Contraseña:” (QLabel + QLineEdit).
# - El campo contraseña debe ocultar el texto.



        email_label = QLabel("Email:")
        """email_label.setFont(QFont('Italic', 16))""" #no funciona
        font_email_italic = QFont()
        font_email_italic.setItalic(True)
        font_email_italic.setPointSize(16)
        email_label.setFont(font_email_italic)
        email_input = QLineEdit()
        email_input.setStyleSheet("background-color: #FFFF00")
        contraseña_label = QLabel("Contraseña:")
        font_italic = QFont()
        font_italic.setItalic(True)
        font_italic.setPointSize(16)
        contraseña_label.setFont(font_italic)
        contraseña_input = QLineEdit()
        contraseña_input.setEchoMode(QLineEdit.Password)
        contraseña_input.setStyleSheet("background-color: #FFFF00")
        layout.addWidget(email_label, 2, 0)
        layout.addWidget(email_input, 2, 1)
        layout.addWidget(contraseña_label, 3, 0)
        layout.addWidget(contraseña_input, 3, 1)


# -----------------------------------------------------------------------------
# Ejercicio 3: Selección de género
# -----------------------------------------------------------------------------
# Teoría:
# - QRadioButton permite seleccionar una opción.
# - QButtonGroup agrupa los radio buttons para que solo uno esté activo.
#
# Consigna:
# - Agregar dos QRadioButton: “Masculino” y “Femenino”, en la misma fila.
# - Usar QButtonGroup para agruparlos.

        gen_masculino = QRadioButton("Masculino")
        gen_femenino = QRadioButton("Femenino") 
        layout.addWidget(gen_masculino, 4, 0)
        layout.addWidget(gen_femenino, 4, 1)


# -----------------------------------------------------------------------------
# Ejercicio 4: Selección de país
# -----------------------------------------------------------------------------
# Teoría:
# - QComboBox permite elegir una opción de una lista desplegable.
#
# Consigna:
# - Agregar QLabel “País:” y QComboBox con al menos 5 países.

        pais_label = QLabel("País:")
        combo_paises= QComboBox()
        combo_paises.addItems(["Argentina", "Venezuela", "Chile", "Uruguay", "España"])
        layout.addWidget(pais_label, 5, 0)
        layout.addWidget(combo_paises, 5, 1)


# -----------------------------------------------------------------------------
# Ejercicio 5: Checkbox de términos
# -----------------------------------------------------------------------------
# Teoría:
# - QCheckBox permite aceptar o rechazar condiciones.
#
# Consigna:
# - Agregar QCheckBox: “Acepto los términos y condiciones”.

        terminos_check = QCheckBox('Acepto los terminos y condiciones')
        layout.addWidget(terminos_check, 6, 0, 1, 2)

# -----------------------------------------------------------------------------
# Ejercicio 6: Botón de envío y validación
# -----------------------------------------------------------------------------
# Teoría:
# - QPushButton ejecuta una función al hacer clic.
# - QMessageBox muestra mensajes emergentes.
#
# Consigna:
# - Agregar QPushButton “Registrarse”.
# - Al hacer clic, validar que todos los campos estén completos y el checkbox marcado.
# - Mostrar mensaje de éxito o error.
        boton_registrar = QPushButton("Registrarse")
        layout.addWidget(boton_registrar, 7, 0, 1, 2)

        def registrar():
            if (not nombre_input.text().strip() or not email_input.text().strip() or not contraseña_input.text().strip() or not (gen_masculino.isChecked() or gen_femenino.isChecked()) or combo_paises.currentIndex() == -1 or not terminos_check.isChecked()):
                QMessageBox.warning(self, "Error", "Por favor, complete todos los campos y acepte los términos.")
            else:
                QMessageBox.information(self, "Éxito", "¡Registro exitoso!")

        boton_registrar.clicked.connect(registrar)
# -----------------------------------------------------------------------------
# Ejercicio 7: Personalización visual
# -----------------------------------------------------------------------------
# Consigna:
# - Cambiar colores de fondo, fuentes y tamaño de los widgets.
# - Centrar el formulario en la ventana.
        paleta = QPalette()
        paleta.setColor(QPalette.Window, QColor("#0099FF"))
        self.setPalette(paleta)
        self.setAutoFillBackground(True)
        layout.setAlignment(Qt.AlignCenter)

# cambie fuentes, fondos y tamaños arriba

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())