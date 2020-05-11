# M&G Blog
An application that allows users to use that one minute wisely. The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.   

## Built By [Martin Gathu](https://github.com/martingathu/)

## Description
M&G Blog is a web application that allow user to post a question of any title, the auther of the blog can delete a post. users can add comments on the blogs.

#### You can view the site at: 

## User Stories
These are the behaviours/features that the application implements for use by a user. As a user I would like to:

* See the blog posts other people have posted
* Signed in for me to leave a comment
* View the blogs I have created in profile page
* Comment on different blog posts
* Submit a question in any category



## Specifications
| Behaviour                                  |            Input             |                                                               Output |
| :----------------------------------------- | :--------------------------: | -------------------------------------------------------------------: |
| Display comments                           |       **On page load**       |           List of various comments sources is displayed per category |
| Display comments from people who signed in |  **Click on Add comments**   |         Redirected to a page with a list of comments from the source |
| Display the blog posts and comments           |       **On page load**       |                 Each blog post displays an title, description and author |
| Read an entire blog                       | **post category sub-title** | Redirected to the picked category source's site to read entire blog |
| Go back to pick category you need          |        **Click Home**        |                                  Redirected to the post a blog area |
## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* virtualenv

### Cloning
* In your terminal:
        
        $ git clone https://github.com/martingathu/Blog
        $ cd Blog

## Running the Application
* Creating the virtual environment

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python 
        
* Installing Flask and other Modules

        $ python3.6 -m pip install Flask
        $ python3.6 -m pip install Flask-Bootstrap
        $ python3.6 -m pip install requests
        
        
* To run the application, in your terminal:
        $ python3.6 manage.py server

## Testing the Application
* To run the tests for the class files:

        $ python3.6 -m unittest discover -s tests
   
## Technologies Used
* Python3.6
* Flask


## License
MIT &copy;2020 [Martin Gathu](https://github.com/martingathu/)