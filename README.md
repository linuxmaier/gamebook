gamebook
========

django app to serve/run/create gamebooks in the style of Choose Your Own Adventure.

current data layout
-------------------

gamebook
	author (MtM)
	page count
	pages
	date published
	number of playthroughs
	popularity


author
	name
	email address
	gamebooks (MtM)
	bio

page
	gamebook (MtO)
	content
	choices

choice
	page_from
	text-content
	page_to

User
	neccesaries for authentication
	email address
	current_pages[] (one per gamebook)
	prev_gamebooks[] (completed, with last page)
	
