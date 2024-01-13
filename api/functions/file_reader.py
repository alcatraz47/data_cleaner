import pandas as pd
import magic
from io import StringIO
from xlsx2csv import Xlsx2csv

ac_ext = ["csv", "xlsx"]

def detect_encoding(file_blob: object) -> str:
    """detects encoding of few characters of file
    as blob. If no encoding is found attempted
    cp1252. retunrs the encoding name.

    Args:
        file_blob (object): few characters of file content

    Returns:
        str: encoding of the file
    """
    m = magic.open(magic.MAGIC_MIME_ENCODING)
    m.load()
    encoding = m.buffer(file_blob)
    if encoding=="unknown-8bit":
        return "cp1252"
    return encoding

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