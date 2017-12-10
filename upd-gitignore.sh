#get new .gitignore from github
wget -q https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore -O .gitignore

#don't forget to ignore our own config file!
echo  >> .gitignore
echo \# conclamantes config file >> .gitignore
echo  config.ini >> .gitignore