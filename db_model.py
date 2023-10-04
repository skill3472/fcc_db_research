from db_clean_up import db_cleaned
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Setting the target and the feature
y = db_cleaned["N sources \nthat mention this chemical"]
x = db_cleaned[["N global \nFCM inventories where included"]]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=18)

# Scaling
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# Initialize model
model = LinearRegression()
model.fit(x_train_scaled, y_train)

y_pred = model.predict(x_test_scaled)

# Test
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}; R2: {r2}")