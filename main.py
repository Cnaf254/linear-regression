#import important libraries
import io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import keras
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import seaborn as sns

#load the csv file

chicago_taxi_dataset = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/chicago_taxi_train.csv")

#update the data frame

update_taxi_df = chicago_taxi_dataset[['TRIP_MILES', 'TRIP_SECONDS', 'FARE', 'COMPANY', 'PAYMENT_TYPE', 'TIP_RATE']]

print("Read data set completed successfully.")
print("Total number of rows: {0}\n\n".format(len(update_taxi_df.index)))

print(update_taxi_df.head(10))


#view dataset statistics
print(update_taxi_df.describe(include='all'))