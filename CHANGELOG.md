# Changelog
## Alpha 0.0.7 - Saved a Trip...
Commit [019e6e0](https://github.com/l19980623/QSteamKeyManager/commit/019e6e00580984ae529d89eb81222175ea329dc2) on Jun 14, 2020. No production build.

This update brings much needed functionality that enables interaction with in-memory database and text files.

* [NEW] After startup, changes are saved to an in-memory database.
   * Upon exit, you will have a chance to save these changes to a local database... or you can discard it. The choice is yours.
   * Alternatively, you can save the changes to a local database and continue to work from there. 
* [NEW] Now you can import entries from a text file. The program will try its best but can still fail under extreme circumstances.
* [NEW] A few more prompts for maximum user-friendliness.
* [FIX] Fixed issues that cause program to crash.

## Alpha 0.0.6 - Legal Stuff and Paperwork
Committed on May 16, 2019. No production build.

This update focuses on the legal stuff: things like "About Me" page, license,
and more.

* [NEW] Added an "About QSKM" page so you can clearly see that this app is clearly
~~not ready for production~~ very awesome. Got it?
    * Also I added a loicense (oi mate!) page to tell you that you can do basically
    whatever you want with the app. 
    * Also also I acknowledged a few open-sauce software, libraries, and cookbooks.
    Without them QSKM will never taste the same!
    * You can also find a link which conveniently take you back to the project page.

## Alpha 0.0.5 - The «Restoration» is Complete!
Committed on May 15, 2019. No production build.

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

## Alpha 0.0.4
Committed on February 14, 2019. No production build.

* [NEW] Search for anything! Hidden indexes as well! (oops)
* [NEW] Clear search keywords by clicking, surprisingly, "Clear" button.

## Alpha 0.0.3
Committed on February 13, 2019. No production build.

* Happy Lunar New Year!
* Implemented functionality to add a game.
    - Notice that any changes are automatically saved to the database, saving you some hassles.
    - Given how well this model works, it might not be necessary to have "Save" any more.
        - But, "Save" has always been part of the software. It feels incomplete without it! Maybe we should just leave as it is. A good placebo I guess..

## Alpha 0.0.2-2
Committed on December 30, 2018. No production build.

* Added two prompts to the program. Right now it does not react to your input, though..
* We now have a (generated) logo! Courtesy of [Font Meme](https://fontmeme.com/fallout-font/). 

## Alpha 0.0.2
Committed on December 28, 2018. No production build.

* After some serious researching and digging QSKM can now reads from a sqlite-based database! 
* Not only that, it also shows the data in an interesting... table. Yes, a table differing from the prototype. Guess you don't care, anyways.
* The table is editable and sortable. Right now the editing is kinda wonky and need further working on it.
    - Right now edits will be automatically saved to the database when you click away from the row.

## Alpha 0.0.1
Committed on December 8, 2018. No production build.

The project is online! Right now it contains only a skeleton UI and some mock entries. Stay tuned for further updates!
