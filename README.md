# SW Engineering Project
## Order Processing Application

## How to Run Our App
* A few things:
  * Our app is currently locally hosted
  * We have only hosted our database on Google Cloud

 ##### You can clone our master branch to your machine:
 ```linux
 git clone https://github.com/mkhalid578/sw_eng_project.git
 ```
 
 #### A Few Important Dependencies 
 
 ##### You will need Python installed on your machine (Python 2.7 recommended)
 
 ```linux
 sudo apt-get install python
 ```
 ##### The Flask extension 
 
 ```linux
 sudo pip install flask
 ``` 
 
 ##### The pymsql library 
 
 ```linux
 sudo pip install pymysql
 ```
 
 ##### Go to the FlaskApp directory 
 
 ```linux
 cd sw_eng_project/flask/flaskApp
 ```
 ##### Run the web app as such:
 
 ```python
 python app.py
 ```
 ##### You will be prompted with a message letting you know the server is running locally
 
 ```linux
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```
 ##### Open a web browser and type or paste the following into your address bar:
 
 ```linux
 http://127.0.0.1:5000/compLogin
 ```

## Scrum/Agile Environment
* In this project we will be using Agile/Scrum Methodology
* We will be using ZenHub as a tool to help us implement an Agile environment
* In order for you to see the "Scrum Board", you must add ZenHub as an extension on your Chrome Browser:
 * https://www.zenhub.com/
* Once ZenHub is installed, GitHub will now have two additional columns, _Boards_ and _Reports_. This is where our product backlog, and sprint backlogs are kept. In addition that, we also have our burndown charts to show our sprint velocity. 

## Sprints 
* We have included all the information pertaining to backlogs and sprint backlogs under /Sprints/README.md 
* We will conduct daily sprint meetings and ask the 3 important questions: 
  * What did you do since the last sprint meeting
  * What will you do today
  * What are you stuck one? Do you need help with anything? 

* The designated ScrumMaster is Muhammed Khalid (@mkhalid578)
* The Product Owner is Vibhuti Patel (@vibhuti_patel1)
* The Principal Software Engineer is Michael Bertucci (@michael_bertucci1)

## Branches 

* Master Branch
  * This will be the final branch used for release and prototype submission. It will included merged content from seperate branches
  * Everything, in a perfect world, should be validated and tested before it is commited to this master branch. Documentation and unit tests are an exception 
 
* Django Branch 
  * A python web framework. Possible tool in web development. 
  * All files and tasks related to Django will be commited here
  * Validated and tested and then merged with the master branch
  
* Flask Branch
  * A python web framework. Another possible tool in web development that Muhammed will be experimenting with
  * Similar to the Django branch, all tasks related to Flask will be done and committed here. 
  * Validated and tested and then merged with the master branch
  
* MySQL Branch
  * All development related to the mysql database will be performed in this branch 
  * So far only a .sql file has been created
  * We have a single database with three tables. More information is provided in the sql file. 
  
* User Interface Branch
  * This will contain all the GUI elements of the project. 
  * HTML/CSS/JS files
