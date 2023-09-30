# End-to-end-Machine-Learning-Project-with-MLflow


## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/abbaouiAchraf/End-to-End-MLOps-with-MLflow
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n MLOpsProject python=3.8 -y
```

```bash
conda activate MLOpsProject
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/abbaouiAchraf/End-to-End-MLOps-with-MLflow.mlflow \
MLFLOW_TRACKING_USERNAME=abbaouiAchraf \
MLFLOW_TRACKING_PASSWORD=2c99247e13655e288ba20cde3e91911aa678d25b \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/abbaouiAchraf/End-to-End-MLOps-with-MLflow.mlflow

export MLFLOW_TRACKING_USERNAME=abbaouiAchraf 

export MLFLOW_TRACKING_PASSWORD=2c99247e13655e288ba20cde3e91911aa678d25b

```
