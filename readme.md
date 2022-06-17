# Start the API server


## Create python env
```
python -m venv env // or any other name
```
## Activate the env

### In Bash
```
source env/bin/activate
```


### In windows

```
env/scripts/activate
```


## Install the dependencies

```
pip  install -r requirements.txt
```

## Start the server 

```
uvicorn main:app --reload
```