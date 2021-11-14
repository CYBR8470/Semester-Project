# ***User Roles*** 
---
## 1. As a player, I want to be able to log in so I can host or join a game.
### Acceptance Criteria  
- Login feature is separate from admin login.
- Players are able to login in and log out.
- Login is semi-permanent (can return to game from new tab, say).

---
## 2. As a player, I want to host a game so that I can play Yahtzee with others.
### Acceptance Criteria
- Logged-in player can click host, backend generates a new game model and redirects player to the new game page.

--- 
## 3. As a bad actor, I want to spam host requests so that I can degrade the performance of the service.
### Acceptance Criteria 
- Completion of 4

---
## 4. As a system administrator, I want to control the creation of new games to prevent spamming.
### Acceptance Criteria 
- When a player creates a new game, the gameid links to the hosting player in a one-to-one relationship.
- A check mechanism is in place during game creation to ensure a player does not already have a hosted game i.e. gameid=null

---
## 5. As a player, I want to be able to join a hosted game so that I can play Yahtzee with others.
### Acceptance Criteria
- TBD

---
## 6. As a bad actor, I want to subvert the join code so that I can join a private game.
### Acceptance Criteria 
- Completion of 7

---
## 7. As a system administrator, I want a mechanism to manage joincode keys to prevent bad actors from joining private games
### Acceptance Criteria
- TBD

---
## 8. As a player, I want a chat function so that I can communicate with the other players in the game while in the app.
### Acceptance Criteria
- TBD

---
# ***Mockup Design***

---
![Login Screen](/docs/login.PNG "Login Screen")

---
![Host or Join](/docs/select_game.PNG "Host or Join Screen")

---
![Join](/docs/join.PNG "Join Screen")

---
![Game](/docs/main.PNG "Game Screen")

---
