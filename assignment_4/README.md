# Assignment 4: Proof
Running a REST API in a virtual environment with the proof of connectivity of the service.

## Steps Taken:
```
git clone https://github.com/aafeke/bilm464
cd bilm464/assignment_3
python3 -m venv env3 && source env3/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8080
```
## Screenshots
![Server log from the host machine SSH bash](img/1.png)
![/docs directory from an Android device](img/2.jpg)
![GET /dict?word=param endpoint from an Android device](img/3.jpg)