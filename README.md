# Use Flask and HTMX to build a simple python app

## Install after git clone

```bash
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python setup/download_js.py
```

## Install psql

```bash
# Update Homebrew
brew update

# Install PostgreSQL
brew install postgresql

# Start the PostgreSQL service
pg_ctl -D /usr/local/var/postgres start
```

## Build & run

```bash
psql -U postgres -tc "SELECT 1 FROM pg_database WHERE datname = 'flask_htmx'" | grep -q 1 || psql -U postgres -c "CREATE DATABASE flask_htmx"
tailwindcss -i ./static/src/main.css -o ./static/dist/main.css --minify
python app.py
```

# Workshop

1. Migrate
    - [ ] Migrate the information that's saved in [Python file](./content/tmp.py) and save it into psql DB called flask_htmx.
> Use Github Copilot to help you as much as possible
>
> Conversational and prompting skills with Copilot chat, and context by using the correct file to prompt from
>
> Validation of the success and content creation relying on Copilot to create tests

2. Model
    - [ ] Generate the models that match the content so they can be queried from the Python code

> Documentation driven development
>
> Code Generation

3. DB Integration
    - [ ] Adapt the search endpoint so that it returns results from the DB query

4. Styling
    - [ ] Add styling and highlight the portion of the text that matches your query

5. OpenAI
    - [ ] Integrate with OpenAI developer (needs to create an account and get an API KEY) to prompt a model and get nutritional information based on a recipe

    An example prompt can be something like
    ```json
    {
    "recipePrompt": "I want you to act as a Nutrition Facts Generator. I will provide you with a recipe and your role is to generate nutrition facts for that recipe. You should use your knowledge of nutrition science, nutrition facts labels and other relevant information to generate nutritional information for the recipe. Add each nutrition fact to a new line. I want you to only reply with the nutrition fact. Do not provide any other information. My first request is: "
    }
    ```

    And the body of the request
    ```json
    1 cup of all purpose flour, sifted 1 1/2 teaspoon baking powder 1/4 teaspoon salt 2 Tablespoon granulated sugar 1/2 Tablespoon unsalted butter, room temperature Approximately 1/3 cup water
    ```

6. Response formatting
    - [ ] Ask to reply in a different format, that can be interpreted and presented better in our app

7. Image Generation
    - [ ] Generate an image of what the result of the recipe might be