import mlflow
import dagshub

mlflow.set_tracking_uri("https://dagshub.com/agarwalprashant/session19-mlops-mini-project.mlflow")

dagshub.init(repo_owner='agarwalprashant', repo_name='session19-mlops-mini-project', mlflow=True)

with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)