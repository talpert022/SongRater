# comp333-react_native

React Native mobile app for Homework 4 completed by Cole Stevenson, Matthew Querdasi, and Tommy Alpert. The link to the website version of the app is comp333-react.web.app

## Divison Of Work

We divided the work according to the bottom tabs of the app. Matt worked on the 'Create Songs' tab which added new songs to the database. Cole did the songs list tab which displayed all the songs in the data, and allows users to edit and delete songs. Tommy worked on the tab structure of the app and the search songs tab, which allows users to search our songlist by title and artist. Cole really mastered the deployment of the backend on heroku, and we all collabed on the deployment of the frontend.

## Backend

The backend is stored in the backend directory. First, create your own virtual environment with python -m venv /path/to/new/virtual/environment, and activate it with source venv/bin/activate. Inside this venv, you may need to run npm install, or use yarn/brew to add required packages. cd into the backend directory, and run python manage.py runserver. This should run the server locally. If you get any errors due to package installation, just follow the instructions to add what is missing. There are also some lurking files from the heroku deployment, you can ignore those. In the browser, use http://localhost:8000/admin (or whatever address you have configured) to add some preliminary data, like users and songs (this is the only way to add a new user). After, go to http://localhost:8000/api to see how those are stored in our models. Leave this running, and in a new console tab, move on to the frontend:

## Frontend
The frontend is stored in the frontend directory. You may need to use npm install again, but barring any missing packages, this can be run with npm start