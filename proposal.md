# Proposal

## What will (likely) be the title of your project?

GTFS Timetable

## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")

A website that lets you view train timetables.

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

My software will generate the train timetables that the transit agencies don't
want to anymore by reading the general transit feed specification (GTFS) data
and generating timetables from it. I'll make a website where people can view
the timetables from each train, line, or station for each day. They can either
view the timetable on the website or download a PDF of it for offline use.

Users will be able to upload a GTFS file or provide a URL to one.
For a few major cities, the website will provide the URLs already.
Then the user can select a specific day as well as a certain train line or station
for which they want to view the timetable for.

To run my project, you go to the website and give it a GTFS file. There will already
be a server running that will process the stuff on the back end. Alternatively,
you can run the server yourself locally and use the website connected to your local server.

The reason I want to do this for my project is because transit agencies are shifting
to no longer publishing timetables, instead relying only on people using apps
to see when the next trains arrive, which is powered by the GTFS. There are a
lot of people who would still prefer to look at timetables, though, such as
people planning out trips farther into the future, older people who are not as
familiar with technology, and people who do not own a phone.

## If planning to combine 1051's final project with another course's final project, with which other course? And which aspect(s) of your proposed project would relate to 1051, and which aspect(s) would relate to the other course?

N/A

## If planning to collaborate with 1 or 2 classmates for the final project, list their names, email addresses, and the names of their assigned TAs below.

N/A

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

Have a local python program that can be given a GTFS file and a date and then
run and ask what line/station to view. Then it will generate the timetable.

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

Have the above program running as a server and a website that will interact
with the server allowing the user to choose the GTFS file, date, line/station
via the website and then view the timetable as HTML or as a PDF.

### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

- Make the website look nicer
- Presets for GTFS files for various cities
- The server will be running on the cloud so you don't have to run it locally yourself
- Incorporate GTFS files for planned changes

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

Skills:
- learn how to make a website
- learn basic HTML
- understand how basic http and servers work
- learn how to write a server in Python
- learn how the GTFS format works
- learn [Flask](https://pypi.org/project/Flask/)
- learn how to generate a table in HTML
- learn how to generate a table in PDF

Steps for the CLI:
1. read about what's in a GTFS file and download an example one and explore it
2. find a Python library for parsing the GTFS file
3. list all the stations and lines
4. generate the timetable
5. print the timetable just stdout
6. print the timetable as HTML
7. find a Python library to generate PDFs
8. print the timetable as a PDF

Steps for the website:
1. create a basic HTML page
2. create a form for selecting the date and GTFS file
3. set up a basic Flask server serving the above page
4. create a Flask route that takes in the date and GTFS file, list the station and
   lines, and then lets the user select which one
5. create a Flask route that takes in the date, GTFS file, and line/station
   and calls into the above CLI API and then returns the HTML
