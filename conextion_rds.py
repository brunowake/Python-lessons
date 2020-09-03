import mysql.connector
from mysql.connector import Error
import json

try:
    connection = mysql.connector.connect(host='user.cygtocg84pbo.eu-west-2.rds.amazonaws.com',
                                         database='user',
                                         user='admin',
                                         password='brunowake1')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        lista = []
        print(type(cursor.execute("select * from User")))
        for x in cursor:
            lista.append({
                'idUser': x[0],
                'idDepartment': x[1],
                'name': x[2],
                'email': x[3],
                'password': x[4],
                'birthday': x[5],
                'phone': x[6]
            })
            print('adicionado registro a lista: {}  '.format(x))
        my_json = json.dumps(lista, indent=7)
        record = cursor.fetchone()
        print("You're connected to database: ", record)

        for x in lista:
            print('nomes de usuarios: {}'.format(x['name']))
        print(my_json)
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")