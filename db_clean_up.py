import pandas as pd

db = pd.read_excel("FCCdb_201130_v5_Zenodo.xlsx", sheet_name=2)

columns_dropped = ["CAS \nvalidity", "Synonyms, \nas used by other sources",
                   "Priority hazardous substance prioritized based on selected authoritative sources? + why",
                   "Substance of potential concern identified based on selected non-authoritative sources? + why"]

db_cleaned = db.drop(columns=columns_dropped)
