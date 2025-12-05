        self.voz_toolbar = QAction("🎙️", self)
        self.voz_toolbar.triggered.connect(self.dictar_por_voz)