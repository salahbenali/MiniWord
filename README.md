MiniWord

**MiniWord** es un editor de texto ligero y funcional desarrollado en Python utilizando la librería gráfica **PySide6**. 
Este proyecto busca replicar las funcionalidades esenciales de un procesador de textos en una interfaz limpia y amigable.

**Características**

El editor incluye las siguientes herramientas:

# Gestión de Archivos:
- Crear nuevo documento.
- Abrir archivos de texto existentes.
- Guardar cambios en el disco.
    
# Edición de Texto:
- Deshacer (Undo) y Rehacer (Redo).
- Copiar, Cortar y Pegar.
    
# Herramientas Visuales:
- **Contador de palabras** en tiempo real en la barra de estado.
- Personalización del **color de fondo** del editor.
    
# Búsqueda y Reemplazo Avanzado:
- Buscar texto (Siguiente, Anterior y contar coincidencias).
- Reemplazar texto (Uno a uno o todos a la vez).
    
# Interfaz:
- Barra de herramientas con iconos de acceso rápido.
- Atajos de teclado estándar (Ctrl+C, Ctrl+V, Ctrl+S, etc.).


# Imagen del programa:    
<img width="999" height="782" alt="imagen" src="https://github.com/user-attachments/assets/db9acb17-d458-40bc-969f-36a1c2894db6" />


# Crear exe:
<img width="1182" height="643" alt="Captura de pantalla (378)" src="https://github.com/user-attachments/assets/002c5a48-d50a-4a4c-a0ad-44f480c0eb33" />


# Firma del exe:
<img width="1142" height="611" alt="Captura de pantalla (381)" src="https://github.com/user-attachments/assets/5d747ac1-4481-4345-93a1-41d298da78a5" />


# Generar instalador:
<img width="1424" height="753" alt="Captura de pantalla (384)" src="https://github.com/user-attachments/assets/0f9fb0c4-c0aa-47d5-acbf-fb01d71b59f8" />
<img width="960" height="459" alt="Captura de pantalla (386)" src="https://github.com/user-attachments/assets/e0df7a24-e6a7-426a-99b2-7acebd316abc" />
<img width="822" height="629" alt="Captura de pantalla (387)" src="https://github.com/user-attachments/assets/91c2a119-1b8a-44ce-a583-65851b571f64" />
<img width="865" height="699" alt="Captura de pantalla (389)" src="https://github.com/user-attachments/assets/74ef48d4-4d8c-46b8-890d-6d862a45a62d" />

## Señales en PySide6

Las señales permiten que los componentes se comuniquen entre sí. En este caso, el widget "WordCounterWidget" emite una señal cada vez que se actualiza el conteo.

El `WordCounterWidget` es un componente que muestra en tiempo real:
- Contador de palabras
- Contador de caracteres
- Tiempo estimado de lectura

Declaración de la señal:
```python
from PySide6.QtCore import Signal

class WordCounterWidget(QWidget):
    conteoActualizado = Signal(int, int)
```

Emisión de la señal:
```python
def update_from_text(self, text: str):
    palabras = len(re.findall(r"\b\w+\b", text))
    caracteres = len(text)
    
    self.lblP.setText(f"Palabras: {palabras}")
    self.lblC.setText(f"Caracteres: {caracteres}")
    self.lblT.setText(f"Lectura: {seg}s" if seg < 60 else f"Lectura: {round(seg/60)} min")

    self.conteoActualizado.emit(palabras, caracteres)
```



