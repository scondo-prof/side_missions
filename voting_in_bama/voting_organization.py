
import pandas as pd
from pandas import DataFrame

def create_data_frame_from_xlsx(xlsx_path: str) -> DataFrame:
    df: DataFrame = pd.read_excel(xlsx_path, engine="openpyxl")

    return df

if __name__ == "__main__":
    create_data_frame_from_xlsx("test_Copy of RQ10719.xlsx")