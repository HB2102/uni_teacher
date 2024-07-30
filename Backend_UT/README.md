# University Teacher Back-End
## Back-end of a website to see university teachers, rate them and comment about what you know about them with FastAPI (Python).
<hr>
Here is back-end of a website for rating and commenting about teachers. With this porject
you can rate about different aspects of teacher (behaviour, teaching, ...) comment about them,
like or dislike comments, see the teachers profile and their average ratings 
and see their universities and subjects. This project is written in microservice architecture
and uses and external service named Liara for both database and cloud file savings.
This back-end was written with FastAPI web framework and uses postgresql for 
database and different data structures was used in it.
to use it and test the backend you can follow instructions below:

### 1. Download project
Download the project into your device or simply clone the project into a 
directory with your virtual environment or any directory you want by 
running the command :

```commandline
git clone https://github.com/HB2102/uni_teacher
```

and then cd into the back-end directory:
```commandline
cd Backend_UT
```

### 2. Install requirements

First you should install the requirements of the project, for that, make sure 
you have pip installed and then go to the project directory 
and run the command :

```commandline
pip install -r requirements/requirements.txt
```

and wait for pip to install packages.


### 3. Run the project
First note that for using the project you have to have your own database url 
for external an external database or simply change the database url in 
database file to in the create_engine part to :
```python
engine = create_engine('sqlite:///<your_database_name>.db', connect_args={'check_same_thread': False})
```
and you also need to change the cloud service for project to work properly,
but just to run the project, go to its backend directory and 
run the command :

```commandline
uvicorn main:app --reload
```

if you get the error that the port is in use you can change the port by running the command like :

```commandline
uvicorn main:app --reload --port 5000
```

and it'll change the port to 5000 but running it on port 8000 should be fine at the beginning.  
When the project is running you can go to the URL that it shows tou on your browser and see the first page.


### 4. See the APIs list

To see the list of APIs just add /docs at the end of the URL. It should look something like this :

```Url
http://127.0.0.1:8000/docs
```

you can see the list of all the APIs and you can test them if you want. project has different functionalities, you can
add use them as admin or a simple user.

database already has one default admin with default values of :

- Username : admin
- Password : admin


<br><br><br>
Thanks for your time.
