# Ideone-API
This Python package allows getting information about projects on Ideone

# Installing
```shell
pip install git+https://github.com/TheRealZFinch/Ideone-API.git#egg=httpie
```

# Importing
```python
import ideoneapi
```

# Using the api
###### Seting up project
```python
#Replace 'project id' with your project's id
project = ideoneapi.ideone(' project id ')
```

###### Getting language the project was written in
```python
project_language = project.language()
print(project_language)
```

###### Getting the project's code
```python
project_code = project.code()
print(project_code)
```

####### Example code
```python
import ideoneapi

project = ideoneapi.ideone('5oNhRW')

print(project.language())
print(project.code())
```
