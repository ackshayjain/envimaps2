echo "Creating Virtual Environment envi"
virtualenv envi
cd envi
source bin/activate envi
echo "Virtual Environment activated"

echo "Installing required packages"
pip install django==1.8.18 python2 Pillow requests
mkdir src
cd ..
pwd
echo "Moving Files to envi/src"
mv envimaps2 envi/src

cd envi/src/envimaps2/

echo "Running project"
python manage.py makemigrations
python manage.py migrate
python manage.py runserver