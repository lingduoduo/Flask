Architecture
====
* python3
* Flask
* MySQL
* Bootstrap
* jQuery

Running Code
====
### Flask
```
cd /Users/linghuang/Git/Flask/code_399/ppt4/4.3
export FLASK_APP=index_1.py 
flask run
# flask run --host 0.0.0.0
curl "http://127.0.0.1:5000"

cd /Users/linghuang/Git/Flask/code_399/ppt4/4.4
python index_1.py
# http://127.0.0.1:4999/?a=testing%20argument

cd /Users/linghuang/Git/Flask/code_399/ppt4/4.5
export ops_config=./config/base_setting.py
python index_config_3.py
```

### HTTP requests
```
ps -ef | grep python
kill -9 9556
cd /Users/linghuang/Git/Flask/code_399/ppt5/5.1
python index_1.py
python index_2.py
python index_3.py
python index_4.py

cd /Users/linghuang/Git/Flask/code_399/ppt5/5.1
python index_1.py
python index_2.py
python index_3.py
python index_4.py

cd /Users/linghuang/Git/Flask/code_399/ppt5/5.1/index_5
python application.py

cd /Users/linghuang/Git/Flask/code_399/ppt5/5.1/index_6
python test_1.py
python test_2.py

cd /Users/linghuang/Git/Flask/code_399/ppt5/5.3
python application.py
## http://192.168.1.153:4999/python/get
## request:GET,params:ImmutableMultiDict([]),var_a:i love Python
## (http://192.168.1.153:4999/python/get?a=b)
## request:GET,params:ImmutableMultiDict([('a', 'b')]),var_a:b
## request:GET,params:ImmutableMultiDict([('a', 'b'), ('c', 'd')]),var_a:b

## http://192.168.1.153:4999/python/get
## request:GET,params:ImmutableMultiDict([]),var_a:default value for get
## http://192.168.1.153:4999/python/get?a=b
## request:GET,params:ImmutableMultiDict([('a', 'b')]),var_a:b

## http://192.168.1.153:4999/python/post
## request:GET,params:ImmutableMultiDict([('a', 'b')]),var_a:b
## http://192.168.1.153:4999/python/post
## request:POST,params:ImmutableMultiDict([('a', 'b'), ('c', 'd')]),var_a:b

## http://192.168.1.153:4999/python/upload
##request:POST,params:ImmutableMultiDict([('file', <FileStorage: 'Screenshot 2023-02-09 at 10.56.53 AM.png'
	('image/png')>)]),file: <FileStorage: 'Screenshot 2023-02-09 at 10.56.53 AM.png' ('image/png')>
	
curl "http://127.0.0.1:4999/python/get"
curl "http://127.0.0.1:4999/python/get?a=b"
curl "http://127.0.0.1:4999/python/post" -X POST -d "a=b"

curl "http://127.0.0.1:4999/python/post" -X POST --form 'a="b"'
curl --location --request POST 'http://192.168.1.153:4999/python/upload' --form 'file=@"/Users/linghuang/Desktop/Screenshot 2023-02-09 at 10.56.53 AM.png"'
```

### Jinjia2
```
cd /Users/linghuang/Git/Flask/code_399/ppt6/6.1
python application.py
## http://127.0.0.1:4999/python/text
## http://127.0.0.1:4999/python/text_same
## http://127.0.0.1:4999/python/json_same
## http://127.0.0.1:4999/python/template

cd /Users/linghuang/Git/Flask/code_399/ppt6/6.2
python application.py
# http://192.168.1.153:4999/python/template
# http://192.168.1.153:4999/python/extend_template
# http://192.168.1.153:4999/python/extend_template_other
```

### SQLAlchemy
```
pip install flask_sqlalchemy
brew install mysql
pip install mysqlclient

mysql -uroot -p
pwd = 123456
show databases;
use mysql;
select * from `user` -G;

cd /Users/linghuang/Git/Flask/code_399/ppt7/7.1
python manager.py

cd /Users/linghuang/Git/Flask/code_399/ppt7/7.2
python manager.py

pip install flask-sqlacodegen
flask-sqlacodegen "mysql://root:123456@127.0.0.1/mysql" --tables user --outfile "common/models2/user.py" --flask
flask-sqlacodegen "mysql://root:123456@127.0.0.1:3306/mysql" --tables user --outfile "common/models2/user.py" --flask
mysql+pymysql://<username>:<password>@<database-ip>:<port>/<database-name> [--tables <tablenames>] [--notables]


cd /Users/linghuang/Git/Flask/code_399/ppt7/7.3
python manager.py
```

### MVC
```
cd /Users/linghuang/Git/Flask/code_399/ppt8/8.2
pip install flask-script
python manager.py
python manager.py runserver

export ops_config=local
python manager.py runserver

pip install flask_debugtoolbar
python manager.py runserver
```

### Registration and Login
```
create database `movie_cat` default character set = `utf8mb4`;
create table `user` (
    id INT(11) UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT
);
alter table user
    add login_pwd varchar(32) null,
    add login_salt varchar(32) null,
    add status tinyint(3) null,
    add updated_time datetime null,
    add created_time datetime null
;
alter table `user` add unique index `uk_login_name` (`login_name`); 

cd /Users/linghuang/Git/Flask/code_399/ppt9/9.1
export ops_config=local
python manager.py runserver
# http://192.168.1.153:4999/python/template

cd /Users/linghuang/Git/Flask/code_399/ppt9/9.1
export ops_config=local
python manager.py runserver
# http://192.168.1.153:4999/

cd /Users/linghuang/Git/Flask/code_399/ppt9/9.2
export ops_config=local
python manager.py runserver
# http://192.168.1.153:4999/

cd /Users/linghuang/Git/Flask/code_399/ppt9/9.3
export ops_config=local
python manager.py runserver
# http://192.168.1.153:4999/

cd /Users/linghuang/Git/Flask/code_399/ppt9/9.4
export ops_config=local
python manager.py runserver
# http://192.168.1.153:4999/
```

### Launch Jobs
```
cd /Users/linghuang/Git/Flask/code_399/ppt10/10.2
python manager.py
python manager.py runjob

python manager.py runjob -m Test ( jobs/tasks/Test.py )
python manager.py runjob -m test/index ( jobs/tasks/test/index.py )
python manager.py runjob -m test -a list -p 1 2 3 4

cd /Users/linghuang/Git/Flask/code_399/ppt10/10.3
python manager.py runjob -m movie -a list
select * from movie;
crontab -l
30 3 * * *  { export ops_config=local && /Users/linghuang/Git/Flask/code_399/ppt10/10.3/manager.py runjob -m movie -a list ; }
```

-- ppt11 Layout and Pagination
```
cd /Users/linghuang/Git/Flask/code_399/ppt11/11.1
python manager.py runserver
```

### uwsgi + nginx
```
python -m site

for virtual env
python3 -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])'
l /Users/linghuang/.pyenv/versions/3.10.5/bin/uwsgi
sudo ln -s /Users/linghuang/.pyenv/versions/3.10.5/bin/uwsgi /usr/local/bin/uwsgi

https://www.runoob.com/python3/python-uwsgi.html
uwsgi --socket 127.0.0.1:3031 --wsgi-file myflaskapp.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:9191
uwsgi --http-socket :4999 --wsgi-file manager.py --callable app 
uwsgi --http-socket :4999 --wsgi-file manager.py --callable app --processes 4
uwsgi uwsgi.ini
ps -ef | grep uwsgi

brew install nginx
sudo nginx
cd /usr/local/etc/nginx/
ln -s /usr/local/etc/nginx/conf.d/default.conf default.conf
sudo nginx -s reload
http://127.0.0.1:8000
uwsgi --reload /Users/linghuang/Git/Flask/code_399/tmp/logs/movie.pid
```

### Disclaimer

This repository and its contents are collected and shared solely for academic and research purposes.
All code, data, and related materials are intended to support independent study, experimentation, and learning.

If you believe any part of this repository inadvertently includes content that should not be shared publicly or may cause concern, please contact me immediately. I will review and, if necessary, remove the material without delay.

I do not claim ownership of any third-party data or content and have made every effort to respect intellectual property and privacy rights.