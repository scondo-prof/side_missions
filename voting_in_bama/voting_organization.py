
import pandas as pd
from pandas import DataFrame

def create_data_frame_from_xlsx(xlsx_path: str) -> DataFrame:
    df: DataFrame = pd.read_excel(xlsx_path, engine="openpyxl")

    return df

def get_dataframe_columns(df: DataFrame) -> list[str]:
    return df.columns.to_list()


def get_a6_pairs(df_columns: list[str], df: DataFrame) -> dict[str: list[str]]:
    if "a4" in df_columns and "a5" in df_columns and "a6" in df_columns:
        print("Starting to pair a6 value with a4_a5 key")

        a6_pairs: dict[str: list[str]] = {}

        for index, row in df.iterrows():
            
            value_a4: str = row["a4"]
            value_a5: str = row["a5"]
            value_a6: str = row["a6"]

            key: str = f"{value_a4} {value_a5}"

            if key in a6_pairs.keys():
                if not value_a6 in a6_pairs[key]:
                    a6_pairs[key].append(value_a6)
            else:
                a6_pairs[key] = [value_a6]
        
        return a6_pairs
    
    else:
        print("Required Columns are not Present")





if __name__ == "__main__":
    df: DataFrame = create_data_frame_from_xlsx("test_Copy of RQ10719.xlsx")
    df_columns: list[str] = get_dataframe_columns(df=df)

    print(get_a6_pairs(df_columns=df_columns, df=df))
