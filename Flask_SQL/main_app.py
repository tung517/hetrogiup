from builtins import float, print
from itertools import product

import mysql.connector
from flask import Flask, request, jsonify
from author import Author2, Author1
import numpy as np
from sklearn import linear_model, preprocessing

app = Flask(__name__)


# kết nối DB
def get_connection():
    connection = None
    try:
        connection = mysql.connector.connect(host='sql12.freemysqlhosting.net',
                                             database='sql12315812',
                                             user='sql12315812',
                                             password='4Zsklrwgqp')
        if connection.is_connected():
            return connection
    except mysql.connector.Error as error:
        print("Failed")
        return connection


# Lấy ra danh sách tất cả các tác giả
@app.route("/list_author", methods=['GET'])
def get_list_author():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT tac_gia.id,tac_gia.ten,tac_gia.hoc_vi,nganh.ten as 'nganh',co_quan.ten as 'co_quan'\
                    FROM tac_gia,nganh,co_quan \
                    WHERE tac_gia.nganh_id = nganh.id and tac_gia.co_quan_id = co_quan.id \
                    ORDER BY tac_gia.id asc")
    # danh sách các tác giả
    list_data = []
    for row in cursor.fetchall():
        author = Author2(row[0], row[1], row[2], row[3], row[4])
        list_data.append(author.get_dict())

    # tạo json từ danh sách các tác giả
    return jsonify(list_data)


@app.route("/list_suggest", methods=['POST'])
def get_list_suggest():
    id = request.json['id']
    connection = get_connection()
    cursor = connection.cursor()
    cursor.callproc('GetRelationTG', [id, ])
    # lấy dữ liệu từ DB
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

    # chuẩn hóa tập điều kiện và kết quả
    model_data_x = preprocessing.normalize(model_data_x, norm="l1")

    # đã lấy được tập điều kiện và kết quả mẫu
    x = np.array(model_data_x)
    y = np.array(model_data_y)

    # training
    model = linear_model.LinearRegression()
    model.fit(x, y)

    x_new = []
    for row in list_data:
        data_x = [row.hoc_vi, row.co_quan, row.linh_vuc, row.num_co_operate, row.num_newspaper]
        x_new.append(data_x)

    # đưa tập điều kiện vào để dự đoán kết quả -> trả về tập kết quả dự đoán
    y_new = model.predict(x_new)

    # cập nhật point cho các đối tượng
    i = 0
    for row in list_data:
        row.point = y_new[i]
        i += 1

    # sắp xếp mảng theo point tăng dần
    list_data.sort(key=lambda author: author.point)

    # đảo ngược mảng
    list_data = list_data[::-1]

    list_json_data = []
    # trả về json
    for row in list_data:
        list_json_data.append(row.get_dict())
    return jsonify(list_json_data)


if __name__ == "__main__":
    app.run(debug=True)
