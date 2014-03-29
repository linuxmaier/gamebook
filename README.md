gamebook
========

django app to serve/run/create gamebooks in the style of Choose Your Own Adventure.

Files
-----

###License.txt

License file

###README.md

This file, right here!

###.gitignore

Provided gitignore, to keep things sane. Lightly modified from git's
standard python ignore.

###Vagrantfile

Included Vagrant config for development. Uses bootstrap.sh to spin up

###bootstrap.sh

Used by Vagrantfile to spin up development env in Vagrant VM

###models.py

Contains data structure info for the application. Used by Django to
create the ORM for the database

###admin.py

Defines the admin interface for the application in Django

###views.py

Defines the HTTP Responses for the application, creating webviews

###tests.py

Defines tests that should confirm the application is working as
intended

management
----------

Contains scripts used by the application

storyfiles
----------

Contains sample stories for use with the application. All are 
licensed under the same license in LICENSE.txt
