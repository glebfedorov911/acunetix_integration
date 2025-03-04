import pandas as pd


class UrlFileReader:


    def __init__(self, filename):
        self.filename = filename

    def get_url(self):
        df = self._read_file()
        return df["url"].tolist()

    def _read_file(self):
        return pd.read_excel(self.filename)