import pandas as pd
from io import StringIO
from xlsx2csv import Xlsx2csv

ac_ext = ["csv", "xlsx"]
def read_file(file_object: object) -> pd.DataFrame:
    return pd.read_csv(file_object, encoding="utf-8")
    # try:
    #     if file_object.name == ac_ext[1]:
    #         # buffer = StringIO()
    #         # Xlsx2csv(file_object, output_encoding="utf-8").content_types(buffer)
    #         # buffer.seek(0)
    #         # return pd.read_csv(buffer)
    #         return pd.read_excel(file_object)
    #     elif file_object.name == ac_ext[0]:
    #         # print(pd.read_csv(file_object, encoding="utf-8").head())
    #         return pd.read_csv(file_object, encoding="utf-8")
    # except OSError as e:
    #     raise f"Given file {file_object.name} is not supported. Supported file type: {ac_ext}" from e