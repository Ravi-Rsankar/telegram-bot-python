# telegram-bot-python

## Getting Started with DogBot

This python telegram bot which retrieves a dog image from `https://random.dog/woof.json`

It displays the image in the telegram chat on passing the `/bop` command

### Setup

#### :dog Create a new bot in BotFather

Register you bot in the telegram BotFather

Once registered now add the bot to a group so as to make the bot to interact with the members in the group.

To get the updates of the bot go to the URL `https://api.telegram.org/bot<botToken>/getUpdates`

This URL returns a JSON response including the chat Ids of the telegram groups to which your bot is added and the conversations in that group

#### :dog Install the library

```
pip3 install python-telegram-bot
```



### How to test

After running the dogbot python file using `python dogbot.py`

- Go to the group where the bot is added and whose chat Id have been added in the code.

- Now in the chat type and send `/bop` 

- You should be getting a dog image



### Source 

[freecodecamp]: https://www.freecodecamp.org/news/learn-to-build-your-first-bot-in-telegram-with-python-4c99526765e4/

