# Module add_two
Function to add two things of same kind

# Quick start
## Setting up the environment 
Go to root folder (where the 'Pipfile' is located) 

Run following command to sync the python environment:
```command
pipenv sync
```

Then, test the environmonet by running the main module using:

```python
python -m add_two.main --file add_two\items.json
```
## Checking the code
In ```tasks.py``` different utility function are defined for code style, formatting, syntax and tests.

### Pycodestyle
In terminal window run pycodestyle using:
```python
invoke style
```
Correct the code according to the output.

### Pylint 
In terminal window run pylint using:
```python
invoke lint
```
Correct the code according to the output.

### Unit tests
In terminal window run unit tests using:
```python
invoke unit-tests
```
(NB! The underscore becomes a dash when calling the function.)

Important to isolate each test to its input and output reference frame using mocking functionality. 

Coverage should aim for 100%.

### Integration tests
In terminal window run integration tests using:

```python
invoke unit-tests
```
Coverage should aim for 100%.