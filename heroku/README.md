# heroku

  
  

**Heroku** is a cloud platform as a service (PaaS) supporting several programming languages. One of the first cloud platforms, Heroku has been in development since June 2007, when it supported only the Ruby programming language, but now supports Java, Node.js, Scala, Clojure, **Python**, PHP, and Go.For this reason, Heroku is said to be a polyglot platform as it has features for a developer to build, run and scale applications in a similar manner across most languages. Heroku was acquired by Salesforce.com in 2010 for $212 million.

[wikipedia](https://en.wikipedia.org/wiki/Heroku)

  
  

## History

  
Heroku was initially developed by James Lindenbaum, Adam Wiggins, and Orion Henry for supporting projects that were compatible with the Ruby programming platform known as Rack. The prototype development took around six months. Later on, Heroku faced setbacks because of lack of proper market customers as many app developers used their own tools and environment. In January 2009, a new platform was launched which was built almost from scratch after a three-month effort. In October 2009, Byron Sebastian joined Heroku as CEO.On December 8, 2010, Salesforce.com acquired Heroku as a wholly owned subsidiary of Salesforce.com. On July 12, 2011, Yukihiro "Matz" Matsumoto, the chief designer of the Ruby programming language, joined the company as Chief Architect, Ruby. That same month, Heroku added support for Node.js and Clojure. On September 15, 2011, Heroku and Facebook introduced Heroku for Facebook. At present Heroku supports Redis databases in addition to its standard PostgreSQL.

  

## How to Deploy project

  

1. `pip install psycopg2`
2. `pip install gunicorn`
3. `pip install django-heroku`
4. `pip freeze > requirements.txt`
5. Create [runtime.txt](https://github.com/Arash3f/deploy_django_project/blob/main/heroku/runtime.txt) for set python version 
6. Create [Procfile](https://github.com/Arash3f/deploy_django_project/blob/main/heroku/Procfile)  : `web: gunicorn (APP name).wsgi --log-file -`
7. Change setting.py ([see](https://github.com/Arash3f/deploy_django_project/blob/main/heroku/setting.py))
8. `git init `
9. login heroku :  `heroku login`
10. create app :  `heroku apps:create (app name)`
11. push project :  `git push heroku master`

## Additional
- rename app :

 `heroku apps:rename --app (old-name) (new-name)`
 
- app ps :

 `heroku ps -a (app name)`
 
- open app :

 `heroku open -a (app name)`
 
 - run bash :
 
 `heroku run bash`
