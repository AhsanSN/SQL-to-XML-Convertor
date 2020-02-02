'''
you must pip install a number of libraries.
pip install:
lxml
bs4
dicttoxml
mysql-connector
'''


import mysql.connector
from mysql.connector import Error
from dicttoxml import dicttoxml
from bs4 import BeautifulSoup

def convertToXML(inp):
    xml_outp = dicttoxml(inp, custom_root='test', attr_type=False)    
    return (xml_outp)

def beautifyXML(inp):
    bs = BeautifulSoup(inp, 'lxml')
    return (bs.prettify())

def establishConnection():
    mainArr = []
    try:
        print("Attempting establishing connection with the remote server")
        connection = mysql.connector.connect(host='85.10.205.173',
                                             database='anomoz',
                                             user='anomoz_user',
                                             password='anomoz_user')

        sql_select_Query = "select * from testTable"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("Total number of rows is: ", cursor.rowcount)

        print("\nPrinting each record")
        
        for row in records:
            print("=>", row[0], row[1], row[2], row[3])
            respSingle = {
             'id': row[0],
             'col1': row[1],
             'col2': row[2],
             'col3': row[3],
            }

            mainArr.append(respSingle)

        xml_outp = convertToXML(mainArr)
        xml_outp_formatted = beautifyXML(xml_outp)
        print("------UNFORMATTED------------")
        print(xml_outp)
        print("--------FORMATTED------------")
        print(xml_outp_formatted)
        print("-------------------")
        
    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

def main():
    establishConnection()


main()
