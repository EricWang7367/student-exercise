# Exercise 1: Walking skeleton

A [walking skeleton](https://wiki.c2.com/?WalkingSkeleton) is just enough implementation to perform a small end-to-end
function.  It links together the key architectural components of a system and provides a base upon which the system and 
it's architecture can evolve.
For this project, the walking skeleton is a partially implemented web application for creating and managing registers
of things.  This first exercise is about ensuring that your development environment is set up and working as expected, 
and to prove the end-to-end development process we will be following throughout subsequent exercises.


## Prerequisites

The laptop you have been provided should already have the software you will be using installed and set up, namely:
- Git
- Python 3.14
- Docker (Engine & Compose)
- VSCode and/or PyCharm

In addition to the above you'll need a GitHub account.


## Forking/cloning the repository

The first thing you'll need to do is fork this repository so that you have your own copy you can work with and push
changes back to.

1. Open a browser and log in to GitHub using your own credentials
2. Go to https://github.com/LandRegistry/student-exercise and fork it
3. Once forked, you need clone the repository locally in order to work on it.  You can do this by:
   1. Get the web URL (on the repository page "<> Code" -> "Local" -> "HTTPS" -> "Copy URL to clipboard")
   2. Open the command line and change to the directory where you want to clone the project and run:
      ```shell
        git clone <web-url>
      ```


## Running the project

Now that the project has been cloned locally, let's configure and run it.

1. Create a `.env` file in the root of the cloned repo and enter your specific config based on this example:
    ```dotenv
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    POSTGRES_DB=db
    POSTGRES_USER=db_user
    POSTGRES_PASSWORD=db_password
    REDIS_HOST=cache
    REDIS_PORT=6379
    SECRET_KEY=[see below]
    ```
    You **must** set a new `SECRET_KEY`, which is used to securely sign the session cookie and CSRF tokens. It should be a long random `bytes` or `str`. You can use the output of this Python command to generate a new key:
    ```shell
    python -c 'import secrets; print(secrets.token_hex())'
    ```
2. From the root of the cloned repo, run the following command:
   ```shell
   docker compose up --build
   ```
   The first time you run this it may take a while to download all the dependencies, but these will be cached
   for future executions.
3. Open a browser, visit https://localhost and accept the browser’s security warning.
4. Confirm that the application has loaded and you presented with the welcome page.


## Stopping the containers

1. To stop the running containers, press `Ctrl+C` from the terminal/shell where you ran the docker compose command.

