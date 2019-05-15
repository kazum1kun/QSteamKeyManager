![QSKM Logo Long, courtesy of Font Meme](https://fontmeme.com/permalink/181231/ae70c4a9e1fc905ed3b78b09ddb0b801.png)

A simple PyQt-based tool that allows you to manage your unused Steam keys and redemption URLs with ease. Functionality-wise similar to my previous project, [Steam Key Manager](https://github.com/l19980623/SteamKeyManager) but rewritten in Python and Qt framework (powered by [PyQt5](https://www.riverbankcomputing.com/software/pyqt/intro)).  

No preview release is available as of yet. Feel free to contribute to the project by submitting Pull Requests or leaving comments. Thank you!

## Intro 
Do you have a lot of leftover keys from all that bundles but wonder what you can do with them? No worries, QSteamKeyManager (QSKM) is here to help you! With QSKM you can record, modify, and delete keys and URLs in an intuitive UI. You can also tag and categorize keys and see the corresponding game in the store. All data are stored in a database, making them less vulnerable to tampering.

## Getting Started
Since there is no official build as of yet, you need to install and compile the files yourself.
(Assume you have installed Qt 5.12+ on your local machine already)

1. Clone the project: `git clone https://github.com/l19980623/QSteamKeyManager.git`
2. Install necessary dependencies: `cd QSteamKeyManager` then `pip install -r requirements.txt`
3. The entry point of QSKM is `main.py` under the project directory

I have also included the `.ui` files (under `\ui` folder) that can be modified in Qt Designer.
You can then compile them into `.py` files by executing 
`pyuic5 -x [INPUT_FILE].ui -o [OUTPUT_FILE].py`

## Functionality
The following additions and improvements are being worked on:
- Add/Remove entries to the table (done)
- Add notes to entries (done)
- Edit an entry (done)
- Sort the list (done)
- Search for anything in the table (done)
- Search for a game on multiple platforms (done)
- Copy game, key, and notes to the system clipboard (done)
- Import keys from an existing text file (being worked on)
- Save the table to sql file (done)
- Activate keys on various platforms (being worked on)
    - Autodetect the key format??
- Multi-language support
- Tag and categorize entries
- Encrypt local storage

## Issues? 
Should you encounter bugs or have suggestions, feel free to post them in the [Issues](https://github.com/l19980623/QSteamKeyManager/issues) tab. 

## Changelog
See [changelog](https://github.com/l19980623/QSteamKeyManager/blob/master/CHANGELOG.md) in a separate page.
