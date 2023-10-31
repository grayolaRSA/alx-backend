This is a readme file for the i18n task for the ALX SE backend specialisation

Tasks
0. Basic Flask app
mandatory
First you will setup a basic Flask app in 0-app.py. Create a single / route and an index.html template that simply outputs “Welcome to Holberton” as page title (<title>) and “Hello world” as header (<h1>).

1. Basic Babel setup
mandatory
Install the Babel Flask extension:

$ pip3 install flask_babel==2.0.0
Then instantiate the Babel object in your app. Store it in a module-level variable named babel.

In order to configure available languages in our app, you will create a Config class that has a LANGUAGES class attribute equal to ["en", "fr"].

Use Config to set Babel’s default locale ("en") and timezone ("UTC").

Use that class as config for your Flask app.

2. Get locale from request
mandatory
Create a get_locale function with the babel.localeselector decorator. Use request.accept_languages to determine the best match with our supported languages.

3. Parametrize templates
mandatory
Use the _ or gettext function to parametrize your templates. Use the message IDs home_title and home_header.

Create a babel.cfg file containing

[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
Then initialize your translations with

$ pybabel extract -F babel.cfg -o messages.pot .
and your two dictionaries with

$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr
Then edit files translations/[en|fr]/LC_MESSAGES/messages.po to provide the correct value for each message ID for each language. Use the following translations:

msgid	English	French
home_title	"Welcome to Holberton"	"Bienvenue chez Holberton"
home_header	"Hello world!"	"Bonjour monde!"
Then compile your dictionaries with

$ pybabel compile -d translations
Reload the home page of your app and make sure that the correct messages show up.

4. Force locale with URL parameter
mandatory
In this task, you will implement a way to force a particular locale by passing the locale=fr parameter to your app’s URLs.

In your get_locale function, detect if the incoming request contains locale argument and ifs value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.

Now you should be able to test different translations by visiting http://127.0.0.1:5000?locale=[fr|en].

Visiting http://127.0.0.1:5000/?locale=fr should display this level 1 heading:

![Alt text](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/f958f4a1529b535027ce.png?X-Amz-Algorithm%253DAWS4-HMAC-SHA256%2526X-Amz-Credential%253DAKIARDDGGGOUSBVO6H7D%252F20231031%252Fus-east-1%252Fs3%252Faws4_request%2526X-Amz-Date%253D20231031T174736Z%2526X-Amz-Expires%253D86400%2526X-Amz-SignedHeaders%253Dhost%2526X-Amz-Signature%253D0b09c1e1f8df235924b346d5a190b7a6b39006756bc11fdfe6702c8796e250a6)

5. Mock logging in
mandatory
Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in 5-app.py.

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
This will mock a database user table. Logging in will be mocked by passing login_as URL parameter containing the user ID to log in as.

Define a get_user function that returns a user dictionary or None if the ID cannot be found or if login_as was not passed.

Define a before_request function and use the app.before_request decorator to make it be executed before all other functions. before_request should use get_user to find a user if any, and set it as a global on flask.g.user.

In your HTML template, if a user is logged in, in a paragraph tag, display a welcome message otherwise display a default message as shown in the table below.

msgid	English	French
logged_in_as	"You are logged in as %(username)s."	"Vous êtes connecté en tant que %(username)s."
not_logged_in	"You are not logged in."	"Vous n'êtes pas connecté."

Visiting http://127.0.0.1:5000/ in your browser should display this:

![Alt text](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/2c5b2c8190f88c6b4668.png?X-Amz-Algorithm%253DAWS4-HMAC-SHA256%2526X-Amz-Credential%253DAKIARDDGGGOUSBVO6H7D%252F20231031%252Fus-east-1%252Fs3%252Faws4_request%2526X-Amz-Date%253D20231031T174736Z%2526X-Amz-Expires%253D86400%2526X-Amz-SignedHeaders%253Dhost%2526X-Amz-Signature%253D0f848fb971c510d5c26a4ff62d08f93d6591a95d0f0c8957613648cf476a15f4)

Visiting http://127.0.0.1:5000/?login_as=2 in your browser should display this: 
![Alt text](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/277f24308c856a09908c.png?X-Amz-Algorithm%253DAWS4-HMAC-SHA256%2526X-Amz-Credential%253DAKIARDDGGGOUSBVO6H7D%252F20231031%252Fus-east-1%252Fs3%252Faws4_request%2526X-Amz-Date%253D20231031T174736Z%2526X-Amz-Expires%253D86400%2526X-Amz-SignedHeaders%253Dhost%2526X-Amz-Signature%253D09772268bdd6e6d1ebca97d2a25812d063d6bd3d99f46d356c000a7b0d581afc)

6. Use user locale
mandatory
Change your get_locale function to use a user’s preferred local if it is supported.

The order of priority should be

Locale from URL parameters
Locale from user settings
Locale from request header
Default locale
Test by logging in as different users

![Alt text](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/9941b480b0b9d87dc5de.png?X-Amz-Algorithm%253DAWS4-HMAC-SHA256%2526X-Amz-Credential%253DAKIARDDGGGOUSBVO6H7D%252F20231031%252Fus-east-1%252Fs3%252Faws4_request%2526X-Amz-Date%253D20231031T174736Z%2526X-Amz-Expires%253D86400%2526X-Amz-SignedHeaders%253Dhost%2526X-Amz-Signature%253D4c3e69c74c64cc4b0a1a59e3114dd7c02237f7700438ae5e178d22561c77e3a0)

7. Infer appropriate time zone
mandatory
Define a get_timezone function and use the babel.timezoneselector decorator.

The logic should be the same as get_locale:

Find timezone parameter in URL parameters
Find time zone from user settings
Default to UTC
Before returning a URL-provided or user time zone, you must validate that it is a valid time zone. To that, use pytz.timezone and catch the pytz.exceptions.UnknownTimeZoneError exception.

8. Display the current time
#advanced
Based on the inferred time zone, display the current time on the home page in the default format. For example:

Jan 21, 2020, 5:55:39 AM or 21 janv. 2020 à 05:56:28

Use the following translations

msgid	English	French
current_time_is	"The current time is %(current_time)s."	"Nous sommes le %(current_time)s."
Displaying the time in French looks like this:

![Alt text](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/bba4805d6dca0a46a0f6.png?X-Amz-Algorithm%253DAWS4-HMAC-SHA256%2526X-Amz-Credential%253DAKIARDDGGGOUSBVO6H7D%252F20231031%252Fus-east-1%252Fs3%252Faws4_request%2526X-Amz-Date%253D20231031T185932Z%2526X-Amz-Expires%253D86400%2526X-Amz-SignedHeaders%253Dhost%2526X-Amz-Signature%253Ddca87bb0413d311642e0ef61467988f2de356e059399cd7e4776b9eb7ea1c057)

Displaying the time in English looks like this:

![Alt text](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/54f3be802024dbcf06f4.png?X-Amz-Algorithm%253DAWS4-HMAC-SHA256%2526X-Amz-Credential%253DAKIARDDGGGOUSBVO6H7D%252F20231031%252Fus-east-1%252Fs3%252Faws4_request%2526X-Amz-Date%253D20231031T185932Z%2526X-Amz-Expires%253D86400%2526X-Amz-SignedHeaders%253Dhost%2526X-Amz-Signature%253D227da572218dd4e7ee3c4b41bb6d720e67addcefdfd21684ea1f10f7ebaaad48)