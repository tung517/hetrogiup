import json

import numpy as np
from sklearn import linear_model

# x = np.array([5, 15, 25, 35, 45, 55]).reshape(-1, 1)
# y = np.array([5, 20, 14, 32, 22, 38])
#
# model = linear_model.LinearRegression()
# model.fit(x, y)

# print(model.intercept_)
# print(model.coef_)
# z = np.array(([65])).reshape(-1, 1)
# y_pred = model.predict(z)
# print(y_pred)

# Multiple
# x = [
#     [3, 2, 3, 2, 2],
#     [2, 1, 2, 1, 1],
#     [2, 1, 3, 1, 2],
#     [2, 1, 2, 1, 2],
#     [2, 1, 2, 0, 2],
#     [4, 1, 2, 0, 1],
#     [2, 1, 2, 0, 2]
# ]
# y = [1, 1, 1, 1, 0, 0, 1]
#
# x = np.array(x)
# y = np.array(y)
#
# print(x)
#
# multi_model = linear_model.LinearRegression()
# multi_model.fit(x, y)
#
# z_new = [[3, 1, 1, 0, 0]]
# z_new = np.array(z_new)
#
# print(z_new)
#
# y_new = multi_model.predict(z_new)
# print('%f' % y_new)

dict1 = {"id": 1, "name": "tung"}

print(json.dump(dict1))
