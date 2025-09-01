## Python Developer

This repo is basically my first repo made it with git hub. Here is where I basically I'm going to put anything related to python and anything relatetd to my personal growth with the language.

If you're a software engineer, or a python developer, this repo it could be for you, or even if you starting with all this awesome career in technology, I promise you that you would not regreet of beign here in this repo, with the time I would put all my based knowlede of software and all my current knowledge with language here, so you might be follow me with the projects and with the knowledge, I hope that you have fun as well I wil.

## First Initial

This repo is a technical repo in where all the information it would placed in a restfull api in the web, of course you would be able to have the information no just here, in my personal portfolio you will be able to see it there.

Since a continue creating the project I will continue to put more details about eveything that I going to build here.

I need to say that all this it would be with the respective links.

## Python Essentials

- Respective blog link.

## Python for the Development (API's, GRAPHQL, Docker, Cloud, CI/CD)

- Respective blog link.

## Things regarding to create a project using django

Starting with the project:

- python3 -m venv [name of you virtual enviroment]

- To activate the venv you can click f1 if you're using vscode this would guide to a couple of options that of differents python enviroments, he usually would recommend you to use one, so choose that one. If maybe vscode is not recommend you nothing about it, you can start the project by doing this:

- source [name of you venv]/bin/activate
- to deactivate it would be -> deactivate

Then you go with installing the necessary librarys and frameworks.

- pip install django
- pip install djangorestframework
- pip install mysql-connector-python
- pip install mysqlclient
- pip PyMySQL

- django-admin startproject [name of you project] . (the dot is to create the file inside of the folder that you currently have, if you don't use the dot, django will create the project insidie of antoher folder that he would create)

## Python django ORM

At the moment that you need or want to use or to the orm from django this are the keys that you need to considered.

1. import first the models from the application in where you wanna working on.

- from library.models import \*

2. than, to get all the values from the models it would be like this:

- Book.objects.all().values()

3. to storage an element in a model that doesn't have any relationship with any other data base it would be like this:

- author = Author(name = "test", last_name = "test", age = 21)
- author.save()

4. than if is for a table or model that actually has a relantionship beetwen an existing model you can use:

- book = Book(title = "test", author_name_id = 2) [in author_name_id = id] you need to looking for the id of the author to be able to link the record of the book to that author.

so if is for test, check first the id from test, and than make the query above.

5. than if you wanna filter some register to check the autor from a specific book you just do this:

- Book.objects.filter(author_name_id=[the id from of the author]).values('title', 'author_name\_\_name')

## Python for Data Analyst

- Respective blog link.

## Python for Data Engineer

- Respective blog link.

## Python for Data Science

- Respective blog link.
