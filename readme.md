Python Flask快速入门与进阶 ：http://movie.54php.cn/
===========================================

系统演示截图
======
![系统演示](/img/intro.png)

![WebRequestResponse](/img/ppt5.png)

![RestAPIStatusCode](/img/api_status_code.png)

技术选型
====
* python3
* Flask
* MySQL
* Bootstrap
* jQuery

http://www.pythondoc.com/flask-sqlalchemy/quickstart.html

运行代码
====
- ppt4 Flask
```
cd /Users/linghuang/Git/Flask/code_399/ppt4/4.3
# 入口文件
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

- ppt5 HTTP requests
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

- ppt 6 Jinjia2
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

- ppt 7 SQLAlchemy
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

-- ppt 8 MVC
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

-- ppt9
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

```
