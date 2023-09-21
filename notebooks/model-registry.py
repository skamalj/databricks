# Databricks notebook source
# MAGIC %pip install --upgrade "mlflow-skinny[databricks]>=2.5.0" tensorflow
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

import mlflow
mlflow.autolog(exclusive=False)
mlflow.set_registry_uri('databricks-uc')

# COMMAND ----------

import pandas as pd
wind_farm_data = pd.read_csv("https://github.com/dbczumar/model-registry-demo-notebook/raw/master/dataset/windfarm_data.csv", index_col=0)

def get_training_data():
  training_data = pd.DataFrame(wind_farm_data["2014-01-01":"2018-01-01"])
  X = training_data.drop(columns="power")
  y = training_data["power"]
  return X, y

def get_validation_data():
  validation_data = pd.DataFrame(wind_farm_data["2018-01-01":"2019-01-01"])
  X = validation_data.drop(columns="power")
  y = validation_data["power"]
  return X, y

def get_weather_and_forecast():
  format_date = lambda pd_date : pd_date.date().strftime("%Y-%m-%d")
  today = pd.Timestamp('today').normalize()
  week_ago = today - pd.Timedelta(days=5)
  week_later = today + pd.Timedelta(days=5)

  past_power_output = pd.DataFrame(wind_farm_data)[format_date(week_ago):format_date(today)]
  weather_and_forecast = pd.DataFrame(wind_farm_data)[format_date(week_ago):format_date(week_later)]
  if len(weather_and_forecast) < 10:
    past_power_output = pd.DataFrame(wind_farm_data).iloc[-10:-5]
    weather_and_forecast = pd.DataFrame(wind_farm_data).iloc[-10:]

  return weather_and_forecast.drop(columns="power"), past_power_output["power"]

# COMMAND ----------

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

MODEL_NAME = "models.dev-models.test"

def train_and_register_keras_model(X, y):
  with mlflow.start_run():
    model = Sequential()
    model.add(Dense(100, input_shape=(X.shape[-1],), activation="relu", name="hidden_layer"))
    model.add(Dense(1))
    model.compile(loss="mse", optimizer="adam")

    model.fit(X, y, epochs=100, batch_size=64, validation_split=.2)
    example_input = X[:10].to_numpy()
    mlflow.tensorflow.log_model(
        model,
        artifact_path="model",
        input_example=example_input,
        registered_model_name=MODEL_NAME
    )
  return model

X_train, y_train = get_training_data()
model = train_and_register_keras_model(X_train, y_train)
