# Exercise 2: Running the tests

ensuring that your development environment is set up and working as expected, 
and to prove the end-to-end development process we will be following throughout subsequent exercises

## Running the tests locally

1. Install the project's Python dependencies by running the following commands from the root of the repository:
   ```shell
   python -m pip install --upgrade pip
   ```
   ```shell
   pip install -r requirements_dev.txt
   ```
   ```shell
   pip install -r requirements.txt
   ```
   This step should only need to be done once and can be skipped on subsequent running of the tests.
2. Start the containers:
   ```shell
   docker compose up
   ```
3. Run the following command (you'll have to open a new terminal/shell) to execute the project's functional acceptance tests: 
   ```shell
   python -m pytest tests/acceptance_tests/
   ```
4. Confirm that the tests all pass.
5. Visit the application in a browser (https://localhost) and observe that the data created by the tests is still present.

## Clearing the local database

Whilst being able to view the data created by the tests is useful, the database can fill up very quickly if you're running
the tests multiple times.  A simple script is provided in the root of the project that can be used to truncate the database,
execute it by running the following command from the root of the project (where `<username>` and `<password>` are the database
username and password you set in your .env file:
```shell
python empty_db.py -u <username> -p <password>
```
**IMPORTANT NOTE:** executing this script will delete _all_ the rows in the associated database tables, and you won't be able to get them back!


## Breaking the tests

Now that we've proved the tests are passing, let's try breaking them.  The value of a good test suite is that it can help
defend against regressions in the expected behaviour (functionality).



## Configure the GitHub workflow to run tests

1. This project includes some GitHub workflows, but they will not be enabled by default.
2. Go to GitHub...


## Pushing changes back to the repository

1. Go to "Settings" -> "Developer Settings" -> "Personal Access Tokens" -> "Tokens (Classic)"
   1. Generate a new "classic" token called "HMLR work experience" that expires at the end of the week and select the
      following scopes: `repo`, `workflow`, `write:packages`, `delete:packages`, `user`
   2. Click "Generate token"
   3. Copy the generated token and save it somewhere you'll be able to access it later