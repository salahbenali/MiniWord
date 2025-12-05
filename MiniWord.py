from PySide6.QtWidgets import (
    QMainWindow, QApplication, QTextEdit, QFileDialog, QColorDialog, QLabel,
    QMessageBox, QToolBar, QStatusBar, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton
)
from PySide6.QtGui import QAction, QTextDocument
import speech_recognition as sr


class MiniWord(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MiniWord")
        self.resize(800,600)

        self.texto = QTextEdit()
        self.texto.textChanged.connect(self.actualizar_contador)

        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.contador = QLabel("Palabras: 0")
        self.status.addPermanentWidget(self.contador)

        self.crear_panel_buscar()

        contenedor = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(self.texto)
        layout.addWidget(self.panel_buscar)
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

        self.acciones()
        self.menu()
        self.toolbar = QToolBar("Principal")
        self.addToolBar(self.toolbar)
        self.configurar_toolbar()


    def acciones(self):

        self.nuevo = QAction("Nuevo", self)
        self.nuevo.setShortcut("Ctrl+N")
        self.nuevo.triggered.connect(self.nuevo_funcion)

        self.abrir = QAction("Abrir", self)
        self.abrir.setShortcut("Ctrl+O")
        self.abrir.triggered.connect(self.abrir_funcion)

        self.guardar = QAction("Guardar", self)
        self.guardar.setShortcut("Ctrl+S")
        self.guardar.triggered.connect(self.guardar_funcion)

        self.salir = QAction("Salir", self)
        self.salir.setShortcut("Ctrl+Q")
        self.salir.triggered.connect(self.salir_funcion)

        self.deshacer = QAction("Deshacer", self)
        self.deshacer.setShortcut("Ctrl+Z")
        self.deshacer.triggered.connect(self.texto.undo)

        self.rehacer = QAction("Rehacer", self)
        self.rehacer.setShortcut("Ctrl+Y")
        self.rehacer.triggered.connect(self.texto.redo)

        self.copiar = QAction("Copiar", self)
        self.copiar.setShortcut("Ctrl+C")
        self.copiar.triggered.connect(self.texto.copy)

        self.cortar = QAction("Cortar", self)
        self.cortar.setShortcut("Ctrl+X")
        self.cortar.triggered.connect(self.texto.cut)

        self.pegar = QAction("Pegar", self)
        self.pegar.setShortcut("Ctrl+V")
        self.pegar.triggered.connect(self.texto.paste)

        self.colorFondo = QAction("Color de fondo", self)
        self.colorFondo.triggered.connect(self.cambiar_color_fondo)

        self.buscar_accion = QAction("Buscar", self)
        self.buscar_accion.setShortcut("Ctrl+F")
        self.buscar_accion.triggered.connect(self.toggle_panel_buscar)

        self.nuevo_toolbar = QAction("📝", self)
        self.nuevo_toolbar.triggered.connect(self.nuevo_funcion)
        self.abrir_toolbar = QAction("📂", self)
        self.abrir_toolbar.triggered.connect(self.abrir_funcion)
        self.guardar_toolbar = QAction("💾", self)
        self.guardar_toolbar.triggered.connect(self.guardar_funcion)
        self.deshacer_toolbar = QAction("↩️", self)
        self.deshacer_toolbar.triggered.connect(self.texto.undo)
        self.rehacer_toolbar = QAction("↪️", self)
        self.rehacer_toolbar.triggered.connect(self.texto.redo)
        self.copiar_toolbar = QAction("📋", self)
        self.copiar_toolbar.triggered.connect(self.texto.copy)
        self.pegar_toolbar = QAction("📌", self)
        self.pegar_toolbar.triggered.connect(self.texto.paste)
        self.cortar_toolbar = QAction("✂️", self)
        self.cortar_toolbar.triggered.connect(self.texto.cut)
        self.buscar_toolbar = QAction("🔍", self)
        self.voz_toolbar = QAction("🎙️", self)
        self.voz_toolbar.triggered.connect(self.dictar_por_voz)

        self.buscar_toolbar.triggered.connect(self.toggle_panel_buscar)


    def menu(self):
        menu = self.menuBar()
        archivo = menu.addMenu("Archivo")
        archivo.addActions([self.nuevo, self.abrir, self.guardar, self.salir])
        editar = menu.addMenu("Editar")
        editar.addActions([self.deshacer, self.rehacer, self.copiar, self.cortar, self.pegar, self.buscar_accion])
        personalizar = menu.addMenu("Personalizar")
        personalizar.addAction(self.colorFondo)


    def configurar_toolbar(self):
        self.toolbar.addAction(self.nuevo_toolbar)
        self.toolbar.addAction(self.abrir_toolbar)
        self.toolbar.addAction(self.guardar_toolbar)
        self.toolbar.addAction(self.deshacer_toolbar)
        self.toolbar.addAction(self.rehacer_toolbar)
        self.toolbar.addAction(self.copiar_toolbar)
        self.toolbar.addAction(self.cortar_toolbar)
        self.toolbar.addAction(self.pegar_toolbar)
        self.toolbar.addAction(self.buscar_toolbar)
        self.toolbar.addAction(self.voz_toolbar)

    
    
    def crear_panel_buscar(self):
        self.panel_buscar = QWidget()
        self.panel_buscar.setFixedWidth(250)
        self.panel_buscar.setVisible(False)
        layout = QVBoxLayout()

        self.caja_buscar = QLineEdit()
        self.caja_buscar.setPlaceholderText("Buscar...")

        self.caja_reemplazar = QLineEdit()
        self.caja_reemplazar.setPlaceholderText("Reemplazar...")

        boton_buscar = QPushButton("Siguiente")
        boton_anterior = QPushButton("Anterior")
        boton_todo = QPushButton("Todos")
        boton_reemplazar = QPushButton("Reemplazar")
        boton_reemplazar_todo = QPushButton("Reemplazar todos")

        boton_buscar.clicked.connect(self.buscar_siguiente)
        boton_anterior.clicked.connect(self.buscar_anterior)
        boton_todo.clicked.connect(self.buscar_todo)
        boton_reemplazar.clicked.connect(self.reemplazar_siguiente)
        boton_reemplazar_todo.clicked.connect(self.reemplazar_todo)


        layout.addWidget(self.caja_buscar)
        layout.addWidget(self.caja_reemplazar)
        layout.addWidget(boton_buscar)
        layout.addWidget(boton_anterior)
        layout.addWidget(boton_todo)
        layout.addWidget(boton_reemplazar)
        layout.addWidget(boton_reemplazar_todo)
        layout.addStretch()

        self.panel_buscar.setLayout(layout)


    def nuevo_funcion(self):
        self.texto.clear()
        self.status.showMessage("Nuevo documento creado", 2000)

    def abrir_funcion(self):
        nombre, _ = QFileDialog.getOpenFileName(self, "Abrir archivo")
        if nombre:
            with open(nombre, "r", encoding="utf-8") as f:
                self.texto.setText(f.read())
            self.status.showMessage("Archivo abierto correctamente", 2000)

    def guardar_funcion(self):
        nombre, _ = QFileDialog.getSaveFileName(self, "Guardar archivo")
        if nombre:
            with open(nombre, "w", encoding="utf-8") as f:
                f.write(self.texto.toPlainText())
            self.status.showMessage("Archivo guardado correctamente", 2000)

    def salir_funcion(self):
        QApplication.quit()

    def cambiar_color_fondo(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.texto.setStyleSheet(f"background-color: {color.name()};")

    def actualizar_contador(self):
        texto = self.texto.toPlainText()
        palabras = len(texto.split())
        self.contador.setText(f"Palabras: {palabras}")


    def toggle_panel_buscar(self):
        self.panel_buscar.setVisible(not self.panel_buscar.isVisible())

    def buscar_siguiente(self):
        texto = self.caja_buscar.text()
        if texto:
            if not self.texto.find(texto):
                self.status.showMessage("No se encontró más coincidencias.", 2000)

    def buscar_anterior(self):
        texto = self.caja_buscar.text()
        if texto:
            if not self.texto.find(texto, QTextDocument.FindFlag.FindBackward):
                self.status.showMessage("No se encontró coincidencia anterior.", 2000)

    def buscar_todo(self):
        texto = self.caja_buscar.text()
        if not texto:
            return
        contenido = self.texto.toPlainText()
        cantidad = contenido.count(texto)
        QMessageBox.information(self, "Buscar todo", f"Se encontraron {cantidad} coincidencias.")

    def reemplazar_siguiente(self):
        texto = self.caja_buscar.text()
        nuevo = self.caja_reemplazar.text()
        if texto:
            cursor = self.texto.textCursor()
            if cursor.hasSelection() and cursor.selectedText() == texto:
                cursor.insertText(nuevo)
            self.buscar_siguiente()

    def reemplazar_todo(self):
        texto = self.caja_buscar.text()
        nuevo = self.caja_reemplazar.text()
        contenido = self.texto.toPlainText()
        nuevo_texto = contenido.replace(texto, nuevo)
        self.texto.setPlainText(nuevo_texto)
        QMessageBox.information(self, "Reemplazar todo", "Todas las coincidencias fueron reemplazadas.")

    def reconocer_voz(self):
        recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as source:                
                recognizer.adjust_for_ambient_noise(source, duration=0.6)
                recognizer.pause_threshold = 1.2
                recognizer.non_speaking_duration = 0.6
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            return ""
        except Exception as e:
            return None

        try:
            texto = recognizer.recognize_google(audio, language="es-ES")
            return texto.strip()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return ""

    def procesar_texto_de_voz(self, texto):
        if texto:
            self.texto.insertPlainText(texto + " ")
            cursor = self.texto.textCursor()
            self.texto.setTextCursor(cursor)

    def dictar_por_voz(self):
        texto = self.reconocer_voz()
        if texto:
            self.texto.insertPlainText(texto)


if __name__ == "__main__":
    app = QApplication([])
    ventana = MiniWord()
    ventana.show()
    app.exec()
