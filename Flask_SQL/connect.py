import json

import mysql.connector
from mysql.connector import MySQLConnection, Error


class Author:
    def __init__(self, id1, author1, author2, id2, hoc_vi, co_quan, linh_vuc, num_co_operate, num_newspaper):
        self.id1 = id1
        self.author1 = author1
        self.author2 = author2
        self.id2 = id2
        self.hoc_vi = hoc_vi
        self.co_quan = co_quan
        self.linh_vuc = linh_vuc
        self.num_co_operate = num_co_operate
        self.num_newspaper = num_newspaper

    def get_dict(self):
        dict_data = {"id1": self.id1,
                     "author1": self.author1}
        return dict_data


try:
    connection = mysql.connector.connect(host='sql12.freemysqlhosting.net',
                                         database='sql12315812',
                                         user='sql12315812',
                                         password='4Zsklrwgqp')
    cursor = connection.cursor()
    cursor.callproc('GetRelationTG', [1, ])

    # list chứa dữ liệu cả bảng

    list_data = []
    for result in cursor.stored_results():
        for row in result.fetchall():
            list_data.append(Author(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))


except mysql.connector.Error as error:
    print("Failed")


def learn():
    print("learn")
