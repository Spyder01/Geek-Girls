# Start the API server


## Create python env This is Omshree Hiremath. I am a living example for an idiot.
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