#DEFINIZIONI VARIABILI#
import mysql.connector as mariadb
from credenziali import *
select_all ="""SELECT Cod_Bottiglia, nome, quantita ,P_acquisto, P_vendita, Data_Acqusito
            from bottiglie
            order by P_Vendita
        """
vendita=""" insert into vendite(Data_vendita,quantita,id_bottiglia)
           Values(%s,%s,%s);
        """
vendita_2="""
            update bottiglie set quantita=quantita-%s where Cod_Bottiglia =%s
        """
inserimento="""update bottiglie set quantita=quantita+%s where Cod_bottiglia=%s
        """

aggiunta="""insert into bottiglie
            values(%s,%s,%s,%s,%s,%s,%s,%s)"""
SQL_tipi=""" select * from tipi
     """
SQL_fornitori="""select Partita_IVA,Nome from foritori"""
<<<<<<< HEAD
=======
utente = "antonio"
db="test_bottiglie"
password="antonio"
host="192.168.1.106"
>>>>>>> dada2cccb9db8ace0bcde723c81553587048714f
codice_in = ""
Bottiglie = {}
Cod_quantita = {}
tipi={}
fornitori = {}
mariadb_connection = ""
cursor = ""

#Funzione per prendere il valore della chiave dal' elemento
def get_key(my_dict,val):
    for key, value in my_dict.items():
         if val == value:
             return key
