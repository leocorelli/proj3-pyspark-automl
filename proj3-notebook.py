# Databricks notebook source
import pyspark.pandas as ps

# COMMAND ----------

df = ps.read_csv("dbfs:/FileStore/shared_uploads/lmc121@duke.edu/winequality_red-2.csv")
df.head(30)

# COMMAND ----------

df.describe()

# COMMAND ----------

import databricks.automl

# COMMAND ----------

databricks.automl.regress(df, target_col= "quality")

# COMMAND ----------


