# Data Agent 

## Summary
Data agent is a general purpose python backend that is used to to faciliate primarily text based interactions with a designated front end. Its primary application is toward data analysis and visualization.

**Data Agent supports several types of inputs:**
- *New Utterances*: As input, it takes utterances from this front-end that it passes to an API for an LLM model for generating analytic code.
- *Data*: To support analysis, Data Agent can take data in the form of CSV
- *One or more existing conversation* : DataAgent can load prior conversations conducted via Data Agent. 

**Data Agent returns the following outputs:**

For each utterance, Data Agent returns : 1) the code 2) the result of executing the code (text, visualization)

## Getting Started

Ensure that you have Python 3.12 installed. This project uses pipenv to manage dependencies. You can install pip env as follows: ``` pip install pipenv```

### Dependencies
Downloading, manging, and otherwise modifying dependencies can be managed using ```pipenv install```, much like you would use pip. It is also possible to directly modify the ```Pipfile```.  Dev dependencies, for example jupyter notebook and other tools that are useful for exploration, but not the core funcitonality of the library, can be installed using the ```pipenv install --dev``` option. Please consult pipenv itself for additional commands and options.

### Running the API
Data Agent is a flask-based REST API, intended to be accessed by other applications.

Set the environment variable so that the flask app points to ./DataAgent/api.py, this way you can easily run the api from the parent directory.
```export FLASK_APP=/DataAgent/api.py```. The config.py file is automatically set into development mode.

