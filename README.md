# GPTAPIinterface
Build in progress using the open AI GPT API. Launch in terminal
Place loafco3.py & migrate.py in the same folder.
Launch loafco3.py in terminal
You will be prompted to enter your api key in terminal
once entered, a config file is created that stores the apikey
upon closing the program, loafco3.py will call the migrate script
The migrate scripts handles the storing of chat history. 
When migrate is called, two log files will be created.
One log files stores the last conversation history
The other log file is appended to add the last conversation.

This way you can automatically load the last conversation, and have storage for all of your conversations. All datestamped. 
