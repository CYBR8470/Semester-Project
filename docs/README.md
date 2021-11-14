# ***User Stories*** 
---
## 1. As a player, I want to be able to log in so I can host or join a game.
### Acceptance Criteria  
- Login feature is separate from admin login
- Players are able to login in and log out
- Login is semi-permanent (can return to game from new tab, say)

---
## 2. As a player, I want to host a game so that I can play Yahtzee with others.
### Acceptance Criteria
- Logged-in player can click host, backend generates a new game model and redirects player to the new game page

--- 
## 3. As a malicious user, I want to spam host requests so that I can degrade the performance of the service.
### Acceptance Criteria 
- Completion of 4

---
## 4. As a game developer, I want to control the creation of new games to prevent spamming.
### Acceptance Criteria 
- When a player creates a new game, the gameid links to the hosting player in a one-to-one relationship
- A check mechanism is in place during game creation to ensure a player does not already have a hosted game i.e. gameid=null

---
## 5. As a player, I want to be able to join a hosted game so that I can play Yahtzee with others.
### Acceptance Criteria
- Player can click on the join button for a public game and enter directly
- For a private game, player can enter the proper join code and join a game 
- Entering an incorrect join code will turn the join code field red and not redirect the player

---
## 6. As a malicious user, I want to subvert the join code so that I can join a private game.
### Acceptance Criteria 
- Completion of 7

---
## 7. As a game developer, I want a mechanism to manage joincode keys to prevent malicious users from joining private games
### Acceptance Criteria
- Join code mechanism should use accepted open source cryptographic random function
- Join code should be of sufficient length to deter brute force attacks
- Join codes should be lowercase and numbers only, and be easy to copy/paste
- Join code field does not accept special characters
- Join codes are not visible for private games
- Join codes are visible / provided for public games

---
## 8. As a system administrator, I want to protect login credentials so that credential harvesting is less likely.
### Acceptance Criteria
- Select and integrate a vetted open-source authentication / authorization mechanism
- Ensure password criteria includes a minimum standard (length, complexity)

## 9. As a malicious user, I want to steal login data so that I can try login credentials on other sites.
### Mitigation Criteria
- Completion of 10

## 10. As a system administrator, I want to protect login credentials so that credential harvesting is less likely. 
### Acceptance Criteria
- Select and integrate a vetted open-source authentication / authorization mechanism
- Ensure password criteria includes a minimum standard (length, complexity)

---
# ***Future User Stories***
---
## 11. As a game developer, I want to recreate the Yahtzee game steps within the browser so that players can complete a game. 
### Acceptance Criteria
- Player has 5 dice
- First roll randomizes all 5 dice
- Player may roll up to 3 times before scoring
- Each die can be saved to prevent rerolling
- Saved die can also be unsaved to reroll
- After third roll, all dice are set for scoring
- Each game consists of 13 rounds, with scores chosen at the end of each round
- Winner has highest score at the end of all rounds

---
## 12. As a game developer, I want to thoroughly test scoring to ensure players receive the correct score for their dice set.
### Acceptance Criteria
- Array of all possible combinations of 5 dice is tested against ruleset
- Die values are aggregated (1's, 2's, 3's) and scored 
- Special cases are determined (3/4 of a kind, small/large straight, yahtzee) and annotated
- Generated values match predicted values

---
## 13. As a game developer, I want to recreate the Yahtzee scoring chart so that online play matches in-person play.
- Scores automatically generated for each valid scoresheet column based on dice values
- Player clicks the column they want to save each round's score against
- Each unique yahtzee rule is developed (bonuses, chance, joker, etc) to complete scoring
- This story will be broken down into smaller stories during Milestone 2

---
## 14. As a player, I want the interface to be intuitive and easy to navigate so that I am likely to play again.
### Acceptance Criteria
- HTML, CSS, Javascript recreate mockup layout design and functionality
- If able, graphics will be integrated for the dice and player avatars

---
## 15. As a malicious user, I want to be able to cheat so that I can win every game.
### Acceptance Criteria
- Completion of 16 

---
## 16. As a game developer, I want to prevent cheating so that all players enjoy their game.
### Acceptance Criteria
- All values are stored server-side
- Control logic prevents data manipulation outside the ruleset in stories 9-11
- Further criteria may be found as development continues

---
## 17. As a player, I want a chat function so that I can communicate with the other players in the game while in the app.
### Acceptance Criteria
- This is a push item and will be further evaluated during milestone 2

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
