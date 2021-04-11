import os
import pandas as pd
from download import download
from wwstatviz.io import url_db, db


class Load_db:
    def __init__(self, list_url=url_db, list_name=db):
        for i in range(len(list_url)):
            url = list_url[i]
            db_name = list_name[i]
            path_target = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", db_name + ".csv")
            download(url, path_target, replace=False)

    @staticmethod
    def save_as_df(list_name=db):
        df_list = []
        for dtb in list_name:
            path_target = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", dtb + ".csv")
            df = pd.read_csv(path_target)
            df_list.append(df)
        return df_list
