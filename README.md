# ComePlayGo project plan

Goal
====

We are aiming to create a website where players can buy and developers can sell
their games. The games are not hosted by the site, they would be available
through the links that the developers provide. One developer can have many games
but for now we allow only one developer to manage a game: they can see the
statistics, see their revenues, etc.

Players can purchase the uploaded games. After purchasing the game they can have
access to it, they can save their high score and they can even save the status
of the game, so they can continue where they have left off.

Functionality
=============

Main models
-----------

![models](https://git.niksula.hut.fi/makipaa1/gamestore/raw/master/docs/images/models.png)          

FK = foreign key <br>
[_text_] = blank is allowed

URLs, APIs
----------

Here is a short list with the URLs that are planned for the minimum viable product.


| **Who can access it** | **URL** | **Action** |
|---|---|---|
| D | /sign_up/developers | sign up link for developers |
| P | /sign_up/player | sign up link for players |
| * | /players | listing all the players |
| * | /developers | listing all the developers |
| * | /developers/{id}/games | listing all the games of a developer |
| * | /games | listing games (search with parameters) |
| * | /games/{id} | showing a game with id |
| D | /games/new | adding a new game |
| D | /games/{id}/edit | editing a game with id |
| D | /games/{id}/remove | remove a game with id |
| * | /login | login page |
| * | /logout | logging out, deleting session |
| * | /profile | showing the profile of the user |
| * | /profile/edit | editing the user profile |
| P | /games/{id}/buy | buying a game |
| P | /successful_payment | after successful payment |
| P | /failed_payment | after failed payment |

A = admin <br>
P = player <br>
D = developer

Priorities
----------

First we are planning to focus on the minimal viable product: users (developers,
players) should be able to sign up, to create an account. Then players should be
able to play with the uploaded games, while developers should be able to upload
new games into the system: they should be able to modify them, and if they want
to, they should be able to remove the game.

In the second phase we would take into use the payment feature. Then we will
implement all the messaging functionalities between the game and its parent
page. Later on we would make the registration more secure by signing up with
email.

In the third round we would enhance the existing feature: handsome statistics
for game developers and players about purchases, high scores. We would add some
categorization for the games, thus making the browsing easier and more
intuitive. The security features would be also enhanced, paying special
attention that pages can be visited only by those to whom it is intended.

Finally, in case we have more time we could add try to implement some of the
extra features (in the order of priority):

1. Mobile Friendly
2. Save/load resolution
3. RESTful API
4. 3rd party login
5. Own game
6. Social media sharing

In every phase we will add tests to make sure that the existing features work
and they are compatible with the newly added ones.

Subtasks
========

### The subtasks below are in a chronological order.

Initial layout and the design document:
---------------------------------------

| **Task** | **Description** | **Priority** | **Estimated time** |
|---|---|---|---|
| Layout design | Template pages | 1 | 10 hours |
| Model design | Database | 1 | 10 hours |
| Url planning | Page URLs | 1 | 5 hours |

Main design phase
-----------------

| **Task** | **Description** | **Priority** | **Estimated time** |
|---|---|---|---|
| Page layout implementation | Development of the templates for the pages that are rendered | 1 | 35 hours |
| Back end development | Implementation of all the server side functionality | 1 | 30 hours |
| JavaScript | Game embedding and other JS functionality | 1 | 25 hours |
| CSS Design | Style sheets of the pages | 2 | 15 hours |
| Front-end testing | Test the user interface | 3 | 10 hours |
| Back-end testing | Test the back-end functionality | 3 | 20 hours |
| Website final testing | Testing the website overall, different use-cases etc. | 2 | 10 hours |
| Deployment | Deploy the application to Heroku | 1 | 10 hours |
| | | | 180 hours |

180 hours makes 60 hours per developer which equals to the amount in the course
description.

NOTE: The "chronological order" of this table is merely didrectional, for example 
testing is done in more places than just in the end.

![mockup](https://git.niksula.hut.fi/makipaa1/gamestore/raw/master/docs/images/mockup.png)

Development
===========

Development practices
---------------------

We use Slack to facilitate the communication between team members. We meet once a
week to work together and to talk about tasks for the next week. We use the 
issue-tracking system of GitLab to stay on track of bugs and problems that need
attention.

Developers ought to do development in feature-specific branches to always have a
working version in the master branch.

To ensure the quality and readability of the code, JSLint is used for JavaScript
files.

![mockup](https://git.niksula.hut.fi/makipaa1/gamestore/raw/master/docs/images/diagram.png)

Testing
-------

The purpose of testing is to ensure the best possible quality of software. The
importance of it is emphasized the more the larger the project is, becoming crucial 
in software in continuous development and in production. Because for our online game
store and platform, there is a lot to do in very limited time, testing is not 
performed in a very inclusive manner as that would slow down the development proces 
too significantly.

However, for the very core features whose behaviour we do not expect to change,
testswill be written to ensure their working. Following criteria will be used to
evaluate for which features tests should be written for:

* Is the feature ready, that is to say, the behaviour not supposed to change later?
* Is it something that other parts of the software rely on or probably will rely on in the future?
* Is it something with many possible inputs and outcomes making it difficult to test manually?
* Is it a core feature, meaning that it behaving unexpectedly would be a “show-stopper”

If at least one of these criteria is met, tests should be written for that part of
the application. Other parts can be tested manually, as that tends to be faster,
though less reliable, in small number of tests (when the development process is
short).

It is up for the developer to decide whether they want to follow test-driven
development strategy or write the tests only afterwards to ensure that later work
will not break the feature.

For automated testing, we will use Django’s unit tests available in the django.test
directory: <https://docs.djangoproject.com/en/1.9/topics/testing/overview/>

The application should be ensured to work on at least Chrome and Firefox browsers.

Security
--------

The messaging system between the embedded games and our application is very 
vulnerable, but that is left without attention in this project. Also, the whole 
application uses HTTP instead of HTTPS due to the lack of an SSL certificate.

Other parts that do require attention when it comes to security include user 
authentication and authorization. The users should only have access to pages they are 
allowed. For example, game sales statistics are only visible for the developer.

The payments must be treated properly and any kind of injection should be disallowed
by never using the user input as is.

As part of the development process, security should be thought about by the
developer of the feature. For a production-ready software, peer reviews would 
be conducted but to make the process as agile as possible, security remains the 
responsibility of the developer of the feature mainly in this project.
