For plan:
Goal            <- Ivan
(Mockup)        <- Ibrahima
Diagram of client side and backend   <- Antti
Functionality   <- Ivan
Priorities      <- Ivan

Schedule        <- Ibrahima
Subtasks        <- Ibrahima

Testing         <- Antti
Risks           <- Antti

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

Functionalities
===============

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