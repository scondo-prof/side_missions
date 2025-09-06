
import pandas as pd
from pandas import DataFrame

def create_data_frame_from_xlsx(xlsx_path: str, sheet_name: str = None) -> DataFrame:
    if sheet_name:
        df: DataFrame = pd.read_excel(xlsx_path,sheet_name=sheet_name, engine="openpyxl")
    else:
        df: DataFrame = pd.read_excel(xlsx_path, engine="openpyxl")

    return df

def get_dataframe_columns(df: DataFrame) -> list[str]:
    return df.columns.to_list()


def get_a6_pairs(df_columns: list[str], df: DataFrame) -> dict[str: list[int]]:
    if "a4" in df_columns and "a5" in df_columns and "a6" in df_columns:
        print("Starting to pair a6 value with a4_a5 key")

        a6_pairs: dict[str: list[int]] = {}

        for index, row in df.iterrows():
            
            value_a4: str = str(row["a4"])
            value_a5: str = str(row["a5"])
            try:
                value_a6: int = int(row["a6"])
            except:
                print(f"Value cant be made int: {row["a6"]}, making value 9999")
                value_a6: int = 9999

            key: str = f"{value_a4} {value_a5}"

            if key in a6_pairs.keys():
                if not value_a6 in a6_pairs[key]:
                    a6_pairs[key].append(value_a6)
            else:
                a6_pairs[key] = [value_a6]
        
        return a6_pairs
    
    else:
        print("Required Columns are not Present")

def add_fill_column_to_df(df: DataFrame, column_name: str) -> DataFrame:

    df[column_name] = "fill"
    return df





if __name__ == "__main__":
    df = create_data_frame_from_xlsx(xlsx_path="test_Copy of RQ10719.xlsx")
    df_columns = get_dataframe_columns(df=df)

    a6_pairs = get_a6_pairs(df_columns=df_columns, df=df)

    target_df = create_data_frame_from_xlsx(xlsx_path="test_Daphne District 5 Voter List 9.4.25.xlsx", sheet_name="Municipal Voters 8.26.25")
    df_columns = get_dataframe_columns(df=target_df)

    print(f"Pre Add: {df_columns}")

    add_fill_column_to_df(df=target_df, column_name="a6")
    df_columns = get_dataframe_columns(df=target_df)

    print(f"Post Add: {df_columns}")