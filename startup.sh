# update and install required packages
sudo apt-get update
sudo apt-get install -y postgresql postgresql-contrib libpq-dev python-dev python-pip

# creating users and granting permissions
sudo -u postgres psql -c "create user contacts_dev with password '123456' SUPERUSER"
sudo cp /vagrant/pg_hba.conf /etc/postgresql/9.3/main/
sudo service postgresql restart
PGPASSWORD=123456 createdb -U contacts_dev contactsapp
sudo -u postgres psql -c "grant all privileges on database contactsapp to contacts_dev"

# setting up the app

cd /home/vagrant/mycontacts; pip install -r requirements.txt
cd /home/vagrant/mycontacts; python manage.py migrate
cd /home/vagrant/mycontacts; python manage.py runserver 0.0.0.0:8000
