from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        cnx= get_connection()  #viene aperta la connessione con il database
        if cnx is None:
            return None

        cursor = cnx.cursor(dictionary=True) #cursore dizionario
        query = "SELECT * FROM strumento"
        cursor.execute(query)  #estratta tutta la tabella strumento

        strumenti = []
        for riga in cursor:  #per ogni riga (dizionario), creo un oggetto strumento
            s=Strumento(
                codice=riga["codice"],
                tipo=riga["tipo"],
                marca=riga["marca"],
                anno_acquisto=riga["anno_acquisto"],
                valore=riga["valore"],
                disponibile=bool(riga["disponibile"])
            )

            #aggiungo l'oggetto alla lista:
            strumenti.append(s)

        cursor.close()
        cnx.close()

        return strumenti


    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        cnx=get_connection()
        if cnx is None:
            return None

        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM strumento WHERE tipo = %s"
        cursor.execute(query, (tipo, ))  #il parametro tipo si trova dentro un tupla

        strumenti_trovati=[]
        for riga in cursor:
            s=Strumento(
                codice=riga["codice"],
                tipo=riga["tipo"],
                marca=riga["marca"],
                anno_acquisto=riga["anno_acquisto"],
                valore=riga["valore"],
                disponibile=bool(riga["disponibile"])
            )
            strumenti_trovati.append(s)

            cursor.close()
            cnx.close()
            return strumenti_trovati
