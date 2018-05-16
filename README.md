# HackerNewsClone

This is a small programming challenge proposed by Faber Ventures.

## Getting Started

I picked Python and Django to do this project. To get the project started, you need to go to the directory of the django project, and run the command:

```
python manage.py runserver
```

### Prerequisites

In order to get started you need to have Python and Django installed(Django is the Python Web framework that I used). I used Anaconda to install Python, although you don't need to. It would also help if you had GitBash installed. I was going to explain how to install Python and Django but there are tutorials online that explain that better than I do. This is some of them:

	https://wiki.python.org/moin/BeginnersGuide/Download
	https://docs.djangoproject.com/en/2.0/topics/install/


### Installing

If you have all the prerequisites, you can clone my repository to your computer and run the server.
Here is a tutorial in how to clone repositories in GitHub:

	https://help.github.com/articles/cloning-a-repository/

After cloning the project, use the comamnd prompt, go to the project dir in your computer and run the command:

```
python manage.py runserver
```

After that, you can use any web browser and go to the link (http://127.0.0.1:8000/) and it will open my site.


## Running the tests

There are three types of accounts, the admin account, the staff account and the normal account, the admin can controll everything, the staff account is like a normal account but it can see the number of comments per article and can hide articles.

There is one Admin Account and a Staff Account already created.

The credentials for the Admin user are:

Username: faberadmin<br />
Password: faberisawesome

The credentials for the Staff user are:

Username: faberstaff<br />
Password: faberisawesome

To create a normal user you can just register and it will create a new account.


## Built With

* [Python](https://www.python.org/) - The language used
* [Django](https://www.djangoproject.com/) - The Web framework used


## Authors

**Pedro Ribeiro**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
