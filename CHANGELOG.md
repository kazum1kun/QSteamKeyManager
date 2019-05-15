# Changelog
## May 15, 2019
Finally got some time after a incredibly busy semester!
* [NEW] Now you can *remove* selected entries from the table. What an achievement!
* [NEW] You can copy game name, key, or notes right from the table.
* [NEW] You can search for the game on various PC platforms. For now we support
Steam, GOG (only opens the main page because they don't have a search page), itch.io, 
Origin, and Uplay. *EGS will NOT be supported in foreseeable future.*
* [FIX] Now adding a game would no longer cause program crash. No monkeys harmed
in the fixing process!
* [DEV] A `requirements.txt` was added to facilitate dependency D/L process. Kudos to
[@Dontcampy](https://github.com/Dontcampy) for pointing this out!

As of now QSKM should have the same functionality as the old SKM. Hooray!

## February 14, 2019
* [NEW] Search for anything! Hidden indexes as well! (oops)
* [NEW] Clear search keywords by clicking, surprisingly, "Clear" button.

## February 13, 2019
* Happy Lunar New Year!
* Implemented functionality to add a game.
    - Notice that any changes are automatically saved to the database, saving you some hassles.
    - Given how well this model works, it might not be necessary to have "Save" any more.
        - But, "Save" has always been part of the software. It feels incomplete without it! Maybe we should just leave as it is. A good placebo I guess..

## December 30, 2018
* Added two prompts to the program. Right now it does not react to your input, though..
* We now have a (generated) logo! Courtesy of [Font Meme](https://fontmeme.com/fallout-font/). 

## December 28, 2018
* After some serious researching and digging QSKM can now reads from a sqlite-based database! 
* Not only that, it also shows the data in an interesting... table. Yes, a table differing from the prototype. Guess you don't care, anyways.
* The table is editable and sortable. Right now the editing is kinda wonky and need further working on it.
    - Right now edits will be automatically saved to the database when you click away from the row.

## December 8, 2018
The project is online! Right now it contains only a skeleton UI and some mock entries. Stay tuned for further updates!
