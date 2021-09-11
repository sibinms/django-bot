# django-bot
Django based Telegram Joke bot with static jokes
# Intro

This is a simple Django based Telegram bot, which actually replies with some static jokes. 
There is a backend in Postgresql is configured to store the number of clicks that a particular
user clicks on a particular category of joke. Here there is only Fat, Dumb and Stupid jokes category,
If you wanted to add more ! Try it for sure

# Requirements

- Python 3.6
- Make sure you have pip (pip --version)
- pip install virtualenv to install virtual environment
- Telegram messenger (you can also use the web version at web.telegram.org)


## What to do

To get this running, you need the following. First install dependencies

### Step 0 : Clone the Repository

`https://github.com/sibinms/django-bot.git`
`cd django-bot`
`virtualenv -p python3 venv`
`source venv/bin/activate`

### Step 1 : Install dependencies and set up an .env file

`pip install -r requirements.txt`
after installing all the requirements, look for the sample_env file in the directory and rename it to .env
and add the mentioned env variable values. If you are not sure about all f them , keep reading this Readme

### Step 2 : Run migrations

In this Project we used a Postgresql DB , if you are not aware about it try to read it on this link 
(https://www.postgresqltutorial.com/install-postgresql-linux/) and install it on your system.
After the installation create user and database give that details to .env file

`sudo -u postgres createuser -sPE user_name`
`sudo -u postgres createdb db_name`

There is a model named BotUser which basically stores the user details with unique telegram user-ID , name and the number of clicks 

`python manage.py makemigrations`
`python manage.py migrate`

### Step 3 : Start the local server

And start the server with 

`python manage.py runserver`

### Step 4 : Download and use ngrok

You need an HTTPS url for most webhooks for bots to work. For purely development purposes you can use ngrok. It gives a web-accessible HTTPS url that tunnels through to your localhost.
Download ngrok (https://ngrok.com/)  , got to a new tab on your terminal and start it with 

`ngrok http 8000`


### Step 5 : Talk to the BotFather and get and set your bot token

Start telegram, and search for the Botfather. Talk to the Botfather on Telegram and give the command `/newbot` to create a bot and follow the instructions to get a token.

Copy the token and paste in `.env` file

### Step 6 : Set your webhook by sending a GET request to the Telegram API

You can use POSTMAN for creating a webhook with Telegram 
- Request type is "GET"
- copy and paste the below URL in your POSTMAN and replace the variables specified with in < >
- `https://api.telegram.org/bot<BOT-TOKEN>/setWebhook?url=<ngrok https url eg:https://d852-106-76-51-232.ngrok.io>/webhooks/tutorial/`

You should get a response that states that "webhook has been set"

### Step 7 : Talk to the bot

You should now be able to talk to the bot in your mobile and get responses from it

