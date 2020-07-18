from Var import *
from Classe import Bottiglia
def conn():

    global mariadb_connection,cursor
    try:
        mariadb_connection = mariadb.connect(user=utente,password=password,host=host,database=db)
        cursor = mariadb_connection.cursor()
    except mariadb.Error as error:
        return error

def getBottiglie():
    global cursor, Bottiglie
    cursor.execute(select_all)
    for Codice,Nome,Quantita,P_acqusito,P_vendita,D_acquisto in cursor:
        Bottiglie[Codice]=Bottiglia(Codice,Nome,Quantita,P_acqusito,P_vendita,D_acquisto)

def insertBottiglia(data):
    global cursor
    try:
        cursor.execute(aggiunta,(data[0],data[1],data[2],data[3],data[4],data[5]))
        cursor.commit()
        return 0
    except mariadb.Error as error:
        return error
