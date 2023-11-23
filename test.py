# Databricks notebook source
# MAGIC %sql
# MAGIC SHOW STORAGE CREDENTIALS;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE EXTERNAL LOCATION azstore URL 'abfss://dbstage@unityadlsdatabricks.dfs.core.windows.net/catalogs' WITH (CREDENTIAL unityadls);

# COMMAND ----------

# MAGIC %sql
# MAGIC create catalog stagedb managed location 'abfss://dbstage@unityadlsdatabricks.dfs.core.windows.net/catalogs/stagedb';

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE stagedb.raw.loan_risks_upload (
# MAGIC   loan_id BIGINT,
# MAGIC   funded_amnt INT,
# MAGIC   paid_amnt DOUBLE,
# MAGIC   addr_state STRING
# MAGIC );
# MAGIC
# MAGIC COPY INTO stagedb.raw.loan_risks_upload
# MAGIC FROM 'dbfs:/databricks-datasets/learning-spark-v2/loans/loan-risks.snappy.parquet'
# MAGIC FILEFORMAT = PARQUET;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE TABLE stagedb.raw.department
# MAGIC (
# MAGIC   deptcode  INT,
# MAGIC   deptname  STRING,
# MAGIC   location  STRING
# MAGIC );
# MAGIC
# MAGIC INSERT INTO stagedb.raw.department VALUES
# MAGIC   (10, 'FINANCE', 'EDINBURGH'),
# MAGIC   (20, 'SOFTWARE', 'PADDINGTON'),
# MAGIC   (30, 'SALES', 'MAIDSTONE'),
# MAGIC   (40, 'MARKETING', 'DARLINGTON'),
# MAGIC   (50, 'ADMIN', 'BIRMINGHAM');

# COMMAND ----------

# MAGIC %sh
# MAGIC CLUSTER_ID=`databricks clusters list | grep "$CLUSTER_NAME" | cut -d' ' -f 1`
# MAGIC ORG_ID=`echo $DATABRICKS_DBT_HOST | cut -d '.' -f 1 | cut -c 5-`
# MAGIC export DATABRICKS_SQLHTTPPATH=sql/protocolv1/o/$ORG_ID/$CLUSTER_ID
# MAGIC echo $DATABRICKS_SQLHTTPPATH

# COMMAND ----------

# MAGIC %sh
# MAGIC CLUSTER_ID=`databricks clusters list | grep "$CLUSTER_NAME" | cut -d' ' -f 1`
# MAGIC ORG_ID=`echo $DATABRICKS_DBT_HOST | cut -d '.' -f 1 | cut -c 5-`
# MAGIC export DATABRICKS_SQLHTTPPATH=sql/protocolv1/o/$ORG_ID/$CLUSTER_ID
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
