# Data Agent 
This is a flask-based API to support experimentation with single and multi-agent systems that support data analysis and visualization.  Data Agent advances a framework for modeling AI and Human agents  collaborating through a shared environment.  This library also provides lightweight support for applications relying on conversationg interfaces.

## Getting Started

Ensure that you have Python 3.12 installed. This project uses [pipenv](https://pipenv.pypa.io/en/latest/) to manage dependencies. You can install pipenv as follows: ``` pip install pipenv```

### Dependencies
Downloading, manging, and otherwise modifying dependencies can be managed using ```pipenv install```, much like you would use pip. It is also possible to directly modify the ```Pipfile```.  Dev dependencies, for example jupyter notebook and other tools that are useful for exploration, but not the core funcitonality of the library, can be installed using the ```pipenv install --dev``` option. Please consult pipenv itself for additional commands and options.

### Running the API
Data Agent is a flask-based REST API, intended to be accessed by other applications.

Set the environment variable so that the flask app points to ./DataAgent/api.py, this way you can easily run the api from the parent directory.
```export FLASK_APP=/DataAgent/api.py```. The config.py file is automatically set into development mode.

## Usage
As this is a library intended to support experimentaion it is intended to support varied functionality. As a result, the maturity of different functional capabilities will also vary. As some ideas solidfy they may become their own separate libraries dedicated to a single purpose.  

Refer to following for additional details:
- [Routing](/DataAgent/routes/README.md) : An overview of the different routes this API supports and that can be called by client facing applications.

- [Models](/DataAgent/models/README.md): An overview of the models (Human, AI Agent, Environment) that are currently supported and how to use them. Models that support applications (e.g., Conversational Agents) can also be found here

- [Examples](/Examples/README.md): Some general examples of use -- includes Jupyter notebooks. Ideas and future looking experiments can also be found here.