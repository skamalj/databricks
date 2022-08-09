# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS DBT;
# MAGIC DROP TABLE IF EXISTS dbt.diamonds;
# MAGIC 
# MAGIC CREATE TABLE dbt.diamonds USING CSV OPTIONS (path "/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv", header "true")

# COMMAND ----------

# MAGIC %sh
# MAGIC databricks repos update --path "/Repos/skamalj@outlook.com/databricks.git" --branch master

# COMMAND ----------

# MAGIC %sh
# MAGIC dbt run --profiles-dir /Workspace/Repos/skamalj@outlook.com/databricks.git/my_dbt_demo/ --project-dir /Workspace/Repos/skamalj@outlook.com/databricks.git/my_dbt_demo/

# COMMAND ----------

# MAGIC %sh
# MAGIC cat /tmp/dbt-logs/dbt.log

# COMMAND ----------

# MAGIC %sql 
# MAGIC show tables from dbt

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema testdbt2 location 'dbfs:/mnt/diamonds/warehouse'

# COMMAND ----------

# MAGIC %sql
# MAGIC create table testdbt2.diamonds as select * from dbt.diamonds

# COMMAND ----------

# MAGIC %sql
# MAGIC desc table extended  testdbt2.diamonds;

# COMMAND ----------

# MAGIC %sh
# MAGIC ls /
