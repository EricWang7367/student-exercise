# Exercise 2: Running the tests


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


## Configure the GitHub workflow to run tests

1. This project includes some GitHub workflows, but they will not be enabled by default.
2. Go to GitHub...


## Pushing changes back to the repository

1. Go to "Settings" -> "Developer Settings" -> "Personal Access Tokens" -> "Tokens (Classic)"
   1. Generate a new "classic" token called "HMLR work experience" that expires at the end of the week and select the
      following scopes: `repo`, `workflow`, `write:packages`, `delete:packages`, `user`
   2. Click "Generate token"
   3. Copy the generated token and save it somewhere you'll be able to access it later