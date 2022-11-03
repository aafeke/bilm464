# Assignment 3: An API with Multiple Endpoints

## Usage
Setting a python environment up is recommended.
Clone the repo, change directory into `assignment_3`
```
pip install -r requirements.txt
uvicorn main:app --reload
```
You can perform API calls from now on.
There are 4 functional endpoints; a couple with POST/GET methods for item dictionary, one GET method that emulates a CPU intensive task and returns in 2 seconds, Another GET method that acts as a middleware for a dictionary API where you can query for English words. 
Detailed documentation is at `/docs` directory of the server.

Could have been much easier with Flask but since I wanted this to be durable against the [C10K Problem](https://en.wikipedia.org/wiki/C10k_problem) I went for FastAPI and it's asynchronous approach.