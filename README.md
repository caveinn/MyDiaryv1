This is an online diary where users can pen down their thoughts

**Travis CI badge**

[![Build Status](https://travis-ci.org/caveinn/MyDiaryv1.svg?branch=develop)](https://travis-ci.org/caveinn/MyDiaryv1)

**Coverall badge**

[![Coverage Status](https://coveralls.io/repos/github/caveinn/MyDiaryv1/badge.svg?branch=develop)](https://coveralls.io/github/caveinn/MyDiaryv1?branch=develop)

**codeclimate badge**

[![Maintainability](https://api.codeclimate.com/v1/badges/8e3e3c7fa16442fba697/maintainability)](https://codeclimate.com/github/caveinn/MyDiaryv1/maintainability)

To run this project you should follow the following steps:  

1. Cretate  a virual enviroment with the command  
`$ virtualenv -p python3 venv  

1. Activate the venv with the command     
`$ source venv/bin/activate`

1. Install git  
1. clone this repo  
`$ git clone "https://github.com/caveinn/MyDiaryv1.git"`

1. install requirements      
`$ pip install -r requirements.txt`

1. now we are ready to run. 
	1. for tests run  
	`$ python test_Api.py`   
	1. for the application run  
	`$ export APP_SETTINGS="development"`    
	`$ python run.py`  

If you ran the aplication you can test the various api end points sing postman. The appi endpoints are  

|Endpont|functionality|contraints(requirements)|
|-------|-------------|----------|
|get  /api/v1/login | login |requires authentication |
|get /api/v1/entries| get all the entries| none |
|get /api/v1/entries/<entryid>|return a single entry| entry id |
|delete /api/v1/entries/<entryid>| delete a singel entry| entry id|
|post /api/v1/entries | create a new entry| entry data|
|put  /api/v1/entries/<entryid> |update an entry| entry id & new entry data| 



