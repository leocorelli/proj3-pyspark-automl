# proj3-pyspark-automl
by Leo Corelli

# What I did
In this project, I used the pyspark.pandas api (apache spark python implementation using pandas API) to load data. Spark is a big deal because it is made for big data, which is almost always the kind of data you work with for real world applications. Pandas is great for local projects with 1000s or 100,000s of data points, but it cannot sustain 10s of millions. Spark is essentially distributed pandas, and I'm using it in this project to prepare myself for working with big data. 

Even though my dataset is only 1,500 examples, it could just as easily be 100s of millions and spark can handle it as long as I have the resources in my cluster. The Databricks platform through Azure is an amazing tool to perform big data analysis at scale in the cloud very easily. You can attach a cluster to your notebook (configured for your specific task), load data tables directly from azure into the notebook using spark, and analyze/modify/organize/data engineer as you see fit. This is what I did.

Then, I used another very powerful databricks tool: AutoML. AutoML automatically trains models and evaluates them in an experiment, returning to you the trained versions of the models that are ready for inference. This abstracts almost all of the early stage machine learning process, and allows you to focus on DevOps: deploying your model at scale in the cloud for real world use.

## AutoML Experiment Tracking:
<p align="center">
  <img src="./pics/AutoML experiment.png" width="1000" /> 
</p>
