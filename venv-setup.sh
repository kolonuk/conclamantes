#install python3
sudo apt-get install python3 python3-pip python3-virtualenv -y

virtualenv venv
. venv/bin/activate
pip3 install -r requirements.txt


