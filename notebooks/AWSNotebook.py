# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC LIST 's3://aws-databricks-skamalj';

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE main.default.flights (date string, delay int, distance int, origin string, destination string) 
# MAGIC USING CSV
# MAGIC OPTIONS (header "true", inferSchema "true")
# MAGIC LOCATION "s3://aws-databricks-skamalj"

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(*) from main.default.flights;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC refresh table main.default.flights;

# COMMAND ----------

# MAGIC %sql
# MAGIC drop  table main.default.flights;
