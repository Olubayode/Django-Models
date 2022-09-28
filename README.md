# Django-Models

Author: Olubayode Ebenezer.

Created a new GitHub repository with a README.md, and Python .gitignore file.

I Clones it to my machine/computer, which will create a new folder on my computer with my repository’s content.

I Created a new virtual environment in that folder named .env and install Django in it.

I Created a new Django project.  I Used  an ID number  as the name of the project.

I Created a new application using the Django startapp command. The app should be called blog.

I Added  the blog app to the main_projects INSTALLED_APPS.


 I Created a new model in the blog app called Post. It should have the following fields:


# Post
# --------

Title : A string of maxlength 200, use Django’s models.CharField

 Text : Any amount of text, use Django’s TextField

 Author : A Foreign Key to the current user model. Make use of Django’s get_user_model function.

 Created_date : A date-time column, use Django’s models.DateTimeField. 

 Published_date : A date-time column, use Django’s models.DateTimeField. 

 

I Created migrations for my new model using the makemigrations Django command. 

I Run all migrations using the migrate Django command.

I Staged and Commit your Django project and push my changes to my GitHub repository.

# Resources:

Python: Environment Variables in Django (https://www.youtube.com/watch?v=ceSm2yE97VE&list=PLxuUHF3OiqfWAITD4gPUHZ1GcYRqmyF7P&index=36)

https://www.youtube.com/watch?v=EexZAwPI2FM&list=PLxuUHF3OiqfWAITD4gPUHZ1GcYRqmyF7P&index=33 

Introduction To Django by Eniola and Mildness (https://www.youtube.com/watch?v=fun0b0C2hAM&list=PLxuUHF3OiqfUre0fws5Y33YMfGJnzTBMZ&index=11)
