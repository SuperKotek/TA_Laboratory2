from os import path
import pandas as pd

df = pd.DataFrame(columns=["id", "Figure", "Material", "X (A/R)", "Y", "Z", "Volume", "Square of Surface", "Mass"])

class __report__:

    def add_record(figure, material, x, y, z, v, s, mass):

        df.loc[len(df)] = [len(df), figure, material, x, y, z, v, s, mass]

    def export_report():
        if len(df) == 0:
            raise Exception
        else:
            index = 0
            while True:
                name = "report/Report" + str(index) + ".xlsx"
                if not(path.exists(name)):
                    df.to_excel(name, index=False)
                    break
                else: 
                    index += 1