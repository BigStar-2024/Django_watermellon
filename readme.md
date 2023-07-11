# Watermelon seller-survey

This project is the simple multi-step form with django, native template.


https://user-images.githubusercontent.com/95545435/235451820-af34d0ee-a78d-4ac7-b989-e4fdd701d328.mp4


## Requirements

- Python 3.8
- [Pipenv](https://github.com/pypa/pipenv#installation)



## Basic Installation

1. Clone the repository:

    - Using HTTPS
    ```sh
    https://github.com/Satosh-J/watermelon-seller-survey.git
    ```

2. Install dependencies from Pipfile:

    ```sh
    pipenv install
    ```

## Usage

1. Activate the project virtualenv:

```sh
pipenv shell
```

2. Create tables in the DB by migrating:

```sh
python src/manage.py migrate
```

3. Create an admin user:

```sh
python src/manage.py createsuperuser
```

4. Start the developement server

```sh
python src/manage.py runserver
```

## Page explanation
- http://localhost:8000/
  Multi-step for for seller giftcard survey
- http://localhost:8000/results
  Display all giftcard info
