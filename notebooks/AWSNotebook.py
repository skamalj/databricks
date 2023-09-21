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

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into main.default.test  select * from main.default.flights

# COMMAND ----------

# MAGIC %sql
# MAGIC GENERATE symlink_format_manifest FOR TABLE main.default.test

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE main.default.test SET TBLPROPERTIES(delta.compatibility.symlinkFormatManifest.enabled=true)

# COMMAND ----------

create external schema myspectrum_schema 
from data catalog 
database 'myspectrum_db' 
iam_role 'arn:aws:iam::<account>:role/service-role/AmazonRedshift-CommandsAccessRole-20220901T162738'
create external database if not exists;

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(*) from main.default.test;
