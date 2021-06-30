# Flask Project Template

This is a flask web application project template.

## How to use

Clone/fork/download the repository

Install the requirements in your environment (a virtual env is recommended)
`pip install -r requirements.txt`

Run the Flask's built-in server using
`flask run`
Note that it's a development server and should not be used in production.

## Database

The project template has no database. models.py files, the files that interact with the database, are also missing. They should be put under the blueprints that use them.

## Blueprints and structure

The project template uses blueprints to structure the codebase. 

It has two blueprints, errors and main. Add new ones by creating a new directory under app/ and putting a \_\_init\_\_.py file inside it. See main and errors \_\_init\_\_.py files to see what to put there. You also have to import the blueprint and register it in app/\_\_init\_\_.py . You can copy the code used to register the other two blueprints, just change the names.

## Formatting

The project uses black, isort, and flake8. 

To run black:
`black .`

To run isort:
`isort .`

To run flake8:
`flake8`

Black and isort do the changes automatically while flake8 gives you a list of things to fix. 

Flake8 doesn't like some things common with Flask applications, use `# noqa: {ERROR_CODE_HERE}` to ignore them. For example imports not done at the top of the file can be ignored with `# noqa: E402,E401` at the end of the line.

## Testing

The project has simple pytest testing implemented in tests/ . The tests are split into tests/functional/ and tests/unit/ . 

You can run the tests with
`pytest`

## Styling

You can install sass/scss from https://sass-lang.com/install

Sass makes it a lot easier to manage styling. There's a \_base.scss file in app/static/scss which isn't compiled into a css file. Rather, it can be included in scss files that get compiled into css with `@use 'base'`. The \_base.scss should have styling that's used in most or all pages: footer, background and such.

To automatically compile all scss files to css when they change run `sass --watch scss:css` in app/static/

## Deployment

**TODO**