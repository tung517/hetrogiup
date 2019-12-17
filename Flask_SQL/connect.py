import json
import mysql.connector
from mysql.connector import MySQLConnection, Error
import numpy as np
from sklearn import linear_model
from author import Author1

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
            list_data.append(Author1(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

    model_data_x = []
    model_data_y = []
    # lấy dữ liệu mẫu
    for row in list_data:
        # nếu số lần hợp tác > 0
        if row.num_co_operate > 0:
            # chạy từ lần hợp tác thứ 0 đến num - 1
            for i in range(row.num_co_operate):
                # tạo ra tập dữ liệu mẫu
                data_x = [row.hoc_vi, row.co_quan, row.linh_vuc, i, row.num_newspaper - row.num_co_operate + i]
                model_data_x.append(data_x)
                model_data_y.append(1)
        else:
            data_x = [row.hoc_vi, row.co_quan, row.linh_vuc, row.num_co_operate, row.num_newspaper]
            model_data_x.append(data_x)
            model_data_y.append(0)

    # đã lấy được tập điều kiện và kết quả mẫu
    X = np.array(model_data_x)
    Y = np.array(model_data_y)

    # training
    model = linear_model.LinearRegression()
    model.fit(X, Y)
    # đã training xong

    # dự đoán với bảng data ban đầu
    # tạo bảng dữ liệu điều kiện để cho vào dự đoán
    X_new = []
    for row in list_data:
        data_x = [row.hoc_vi, row.co_quan, row.linh_vuc, row.num_co_operate, row.num_newspaper]
        X_new.append(data_x)
    # đã lấy tập điều kiện xong

    # dưa tập điều kiện vào để dự đoán kết quả
    Y_new = model.predict(X_new)

    # kết quả dự đoán sau khi training
    print(Y_new)

    # Viết API trả về bảng dữ liệu và đã sắp xếp



except mysql.connector.Error as error:
    print("Failed")
