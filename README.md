## URL Shortener (aka Link Shortener)

#### Technologies Used:
Python, Django, PostgreSQL, Docker, HTML, and Materialize.

#### How It Works:
As shown in the screenshot below, the app comes with two inputs and an index table. The first input is for submitting a link/url, where after hitting submit, the application will shorten the link and return both the full link and the shortened link below in the index table. Both of these links are clickable and will take the user to the URL of the full link.

The second input is a search feature that is used to check the database for the short link and to return its coinciding full link, both of which are clickable. If the link is not in the databse, it will return "There are no records for that short link."

<p float="middle">
    <img src="/screenshot/LinkShortenerSS.PNG?raw=true" width="30%" height="30%">
</p>

#### Approach:
My approach for this app was to start by setting up a Docker Compose, then build out the Django application as usual, including a PostgreSQL database. This first involved some extra research of Docker online, in order to make sure I knew how exactly the application would need to function. The commands for setting up this app were fairly boilerplate, with the Docker docs offering a couple examples that I used here: https://docs.docker.com/samples/django/. 

#### Assumptions:
Since the requirements do not include having the app hosted online, I developed it locally on my device, running the app on localhost:8000. As the app is hosted locally it made sense to run the database locally as well, which is named "postres".

After clarifying, it was determined the short links did not need to be clickable from outside of the app. This is important, as it allowed me to simply tag each short link as an <a> tag pointing its href to the coinciding full link that was also stored in the database.

It was also assumed that functionality was the important part of this app, so styling was kept to a minimum.

#### Decision Making Process:
While most decisions went back to the requirements of the project, others were based on assumptions I had made, as mentioned above. This meant keeping the app to a minimum while prioritizing functionality over stlying. I decided to build this app using Python, as I felt it would be more relevent to the job that way.

The sources I used included the Docker docs and Django docs, as well as previous applications I had built, including a Python/Django/PostgreSQL app here: https://github.com/curtismceachen/Digipets. Stack overflow was used for some of the smaller or more random problems I had, such as the full link not taking the user to the URL if a scheme (i.e. https://) was not included in the full link when it was first submitted. In order to fix this I simply placed two forward slashes in front of the link.full_link href in the index.html.

#### How to Run This App:
Once Python, Django, PostgreSQL, psycopg2-binary, and Docker are installed on your device, the app should be able to run using the "docker-compose run" and "docker-compose up" commands. It will then be runnning on localhost:8000.



