# Flask network manager

## Use

* Flask (Obvious!)
* Flask-SQLAlchemy (ORM for database)
* Flask-WTF (Generation of forms and validations)
* Faker (Generates fake data)

## Install

```bash
pip install -r requirements.txt
python3 migrations.py
```
## Run

```bash
python3 app.py
```

## Run with docker
```
docker run -it --rm --name my-running-script -p 5000:5000 -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 bash -c ./run-up.sh
```
