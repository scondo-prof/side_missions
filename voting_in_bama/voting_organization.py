
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

def populate_a6_value_in_other_df(a6_pairs: dict[str: list[int]], df: DataFrame, df_columns: list[str]) -> DataFrame:
    if "Street Address" in df_columns and "a6" in df_columns:
        for index, row in df.iterrows():
            street_address = row["Street Address"]
            for key in a6_pairs:
                if key in street_address:
                    if len(a6_pairs[key]) == 1:
                        row["a6"] = a6_pairs[key][0]
                    else:
                        print("length of a6_pair is longer than 1")
            if row["a6"] == "fill":
                print(f"Street Address: {street_address} did not have a6 value, setting to 9999")
                row["a6"] = 9999
        
        return df
            
    






if __name__ == "__main__":
    df = create_data_frame_from_xlsx(xlsx_path="test_Copy of RQ10719.xlsx")
    df_columns = get_dataframe_columns(df=df)

    a6_pairs = get_a6_pairs(df_columns=df_columns, df=df)

    target_df = create_data_frame_from_xlsx(xlsx_path="test_Daphne District 5 Voter List 9.4.25.xlsx", sheet_name="Municipal Voters 8.26.25")

    add_fill_column_to_df(df=target_df, column_name="a6")
    target_df_columns = get_dataframe_columns(df=target_df)


    populate_a6_value_in_other_df(a6_pairs=a6_pairs, df=target_df, df_columns=target_df_columns)