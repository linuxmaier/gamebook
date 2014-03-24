gamebook
========

django app to serve/run/create gamebooks in the style of Choose Your Own Adventure.

current data layout
-------------------

gamebook
* author (MtM)
* synopsis
* date published
* number of playthroughs
* popularity


author
* name
* email address
* bio

page
* gamebook (MtO)
* page number
* content

choice
* page from
* text-content
* page to

User
* neccesaries for authentication
* email address
* currentpages[] (one per gamebook)
* prevgamebooks[] (completed, with last page)
	
