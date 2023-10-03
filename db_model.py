from db_clean_up import db_cleaned

# Setting the target and the feature
y = db_cleaned["N sources \nthat mention this chemical"]
x = db_cleaned[["N global \nFCM inventories where included"]]
