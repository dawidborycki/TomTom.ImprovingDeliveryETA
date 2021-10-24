import pandas as pd

# Read train data
dataFrame = pd.read_csv('train_data.csv',sep=';')

# Use DepartureHour column as X
X = dataFrame.DepartureHour

# Use TravelTimeInHours column as Y
Y = dataFrame.TravelTimeInHours

# Train the model
from sklearn.linear_model import LinearRegression
import numpy as np

model = LinearRegression().fit(np.array(X).reshape(-1,1), Y)

# Predict travel time for different departure hours
departureHours = [1.5, 3.12, 5.17, 16.05, 10.15, 20.29]

for departureHour in departureHours:
    predictedTravelTime = model.predict(np.array(departureHour).reshape(-1,1))

    print(f"Departure hour: {departureHour},\t Predicted travel time: {predictedTravelTime[0]:.2f} h")