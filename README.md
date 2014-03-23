gamebook
========

django app to serve/run/create gamebooks in the style of Choose Your Own Adventure.

current data layout
-------------------

gamebook
* author (MtM)
* synopsis
* page count
* pages
* date published
* number of playthroughs
* popularity


author
* name
* email address
* gamebooks (MtM)
* bio

page
* gamebook (MtO)
* content
* choices

choice
* page from
* text-content
* page to

User
* neccesaries for authentication
* email address
* currentpages[] (one per gamebook)
* prevgamebooks[] (completed, with last page)
	
