# Databricks notebook source
babynames = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("dbfs:/FileStore/babynames.csv")
babynames.createOrReplaceTempView("babynames_table")


# COMMAND ----------

import requests

response = requests.get('http://health.data.ny.gov/api/views/myeu-hzra/rows.csv')
csvfile = response.content.decode('utf-8')
dbutils.fs.put("dbfs:/mydata/babynames2.csv", csvfile, True)

df = spark.read.csv("dbfs:/mydata/babynames2.csv")
display(df)

# COMMAND ----------

years = spark.sql("select distinct(year) from babynames_table").rdd.map(lambda row : row[0]).collect()
years.sort()
dbutils.widgets.dropdown("year", "2014", [str(x) for x in years])
display(babynames.filter(babynames.Year == dbutils.widgets.get("year")))
