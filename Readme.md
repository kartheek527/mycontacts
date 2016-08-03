#My Contacts
====
```
This is simple app to maintain personal contacts.
````

## Getting Started

### Dev Environment Setup

#### Using vagrant :
* Clone repo
* Download & install vagrant
* Download & install virtualBox
* cd to repo
* `vagrant up`
* `vagrant destroy` (to delete the current instance)

##### Note: 
* To login into the box `vagrant ssh`
* To run dev server cd to repo and `python manage.py runserver 0.0.0.0:8000`
* `vagrant provision` (to apply startup script changes to the box)


#### Using virtual Environment(virtualenv):
* Clone repo
* Download & install Postgres
* Download & install virtual environment
* cd to repo
* If ‘venv’ direcory is not present: `virtualenv venv`
* `source venv/bin/activate`
* `pip install -r requirements.txt`
* `cd mycontacts`
* Set up DB, user role as per project and update in settings.py
* `python manage.py makemigrations`(not required every time)
* `python manage.py migrate`(not required every time)
* `python manage.py runserver`