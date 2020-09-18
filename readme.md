Cricket assignment

This is an application based on Django.
It has functionality to add team, player, and Matches and create Matches fixtures for creating tournaments dynamically.
## Setup

#### Clone the project
```
$ git clone https://github.com/mrrakesh/cricket_assignment.git
$ cd cricket_assignment
```

#### Create virtual env
```
$ python3 -m virtualenv env
$ source env/bin/activate
```

#### Install packages from requirements.txt
```
(env) $ pip install -r requirement.txt
```

#### Setup databse
```
(env) $ python manage.py migrate
```

#### Create superuser to access admin panel
```
(env) $ python manage.py createsuperuser
```

### Run application

```
(env) $ python manage.py runserver
```
Below are the page URLs: -

front page: http://127.0.0.1:8000/
teams list: http://127.0.0.1:8000/team/list
players list: http://127.0.0.1:8000/player/list
create a tournament: http://127.0.0.1:8000/matches/fixtures
Create a fixture: http://127.0.0.1:8000/all_fixtures