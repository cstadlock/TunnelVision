# This file sets up the virtual environment. 
# Run "source setup.sh" each time you want to run the app. 

mkdir -p data

if [ ! -d venv ]
then
  virtualenv venv
fi

. venv/bin/activate

pip install Flask
pip install peewee
pip install pyyaml
pip install PyMySQL
pip install flask_login
pip install flask_wtf
pip install wtf-peewee