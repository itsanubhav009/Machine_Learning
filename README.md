# Machine_Learning
IN this repo to learn machine learning




## Decorators Explore
## Logging Explore
## Generators Explore

##  Process - 

   A process is simply an instance of a program that is being executed
   one Process cannot corrupt another process
   I/O Requirments
   Increased execution time to switch between process

## Threads
  a thread is a unit of execution within the process
  ### Single Threaded Process 
  shared code segment  , datasegment , process
  paint |--->box
        |--->circle
  ### MultiThreaded Process
  parallely shared code segment , datasegment




## Memory managment
  ### Explore tracemalloc


## Flask Framework
   1 - WSAI - web server gateway interface
   2 - Jinja 2 WEB Template Engine it combine we template with data source


   ### Basic Interface
   from flask import Flask

    '''
   it creates an instance of the Flask class.
   which will be your WSGI application.
   '''

    app = Flask(__name__)


    if __name__ == '__main__':
    app.run()


