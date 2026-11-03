import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    def handle_mostra_strumenti(self):
        lista_strum=self._model.get_strumenti()
        self._view.lista_strumenti.controls.clear()

        if lista_strum is None:
            self._view.show_alert("Errore di connessione al database!")
        elif len(lista_strum) == 0:
            self._view.lista_strumenti.controls.append(ft.Text("Nessun strumento presente nel deposito."))
        else:
            for s in lista_strum:
                self._view.lista_strumenti.controls.append(ft.Text(str(s)))

        self._view.update()

    def handle_cerca_tipo(self, e):
        tipo_cercato = self._view.input_tipo_strumento.value.strip()

        if tipo_cercato == "":  #ha premuto cerca, ma la barra è vuota:
            self._view.show_alert("Inserisci un tipo di strumento per cercare!")
            return

        #cerca nel database:
        lista_trovati = self._model.cerca_strumenti_per_tipo(tipo_cercato)
        self._view.lista_strumenti_ricerca.controls.clear()

        #gestione dei risultati:
        if lista_trovati is None:
            self._view.show_alert("Errore di connessione al database!")
        elif len(lista_trovati) == 0:
            self._view.lista_strumenti_ricerca.controls.append(ft.Text(f"Nessun strumento di tipo '{tipo_cercato}' trovato."))
        else:
            for s in lista_trovati:
                self._view.lista_strumenti_ricerca.controls.append(ft.Text(str(s)))

        #aggionarno la UI:
        self._view.upodate()














