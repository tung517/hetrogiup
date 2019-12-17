class Author1:
    point = 0

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
                     "author1": self.author1,
                     "author2": self.author2,
                     "id2": self.id2,
                     "hoc_vi": self.hoc_vi,
                     "co_quan": self.co_quan,
                     "linh_vuc": self.linh_vuc,
                     "num_co_operate": self.num_co_operate,
                     "num_newspaper": self.num_newspaper,
                     "point": self.point
                     }
        return dict_data


class Author2:
    def __init__(self, id, ten, hoc_vi, linh_vuc, co_quan):
        self.id = id
        self.ten = ten
        self.hoc_vi = hoc_vi
        self.linh_vuc = linh_vuc
        self.co_quan = co_quan

    def get_dict(self):
        dict_data = {"id": self.id,
                     "ten": self.ten,
                     "hoc_vi": self.hoc_vi,
                     "co_quan": self.co_quan,
                     "linh_vuc": self.linh_vuc
                     }
        return dict_data
