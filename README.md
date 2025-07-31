# boilerplate_azure_function_app
This is a repository that can be used for local testing and debugging of azure function apps in Pycharm. Everything can be tested via the PyCharm terminal. No usage of other tools needed. (to be continued).

## How to use
- clone repo
- switch to folder where the function resides
- run pip install -r requirements.txt
- obviously change Azure connection strings and storage account info
- type "func start"
- quit with "ctrl + c"
- restart function if desired

  ---
### function_app.py
This file handles the trigger and execution in Azure. 

### my_function.py
This file contains the main code what your function app intends to do. Webscraping, data transfer, etc. goes in here.

## Deploying to Azure
type following commands in your terminal:

- az login (use your credentials)
- zip -r appname.zip
- az functionapp deployment source config-zip --name appname --resource-group your-rg --src appname.zip


## FAQ
- local.settings.json is only used for local development. If you publish the fuinction app to Azure, it is no longer needed.
- This is a basic setup for a function, that is triggered by a time interval (cron Expression)
- A CRON expression is a string that represents a schedule for running commands or scripts at specific times. It consists of five fields that define the timing:
Minute (0-59)
Hour (0-23)
Day of the month (1-31)
Month (1-12)
Day of the week (0-7, where both 0 and 7 represent Sunday)
For example, a CRON expression like 0 12 * * 1-5 would run a command at 12:00 PM every weekday. You can also use online tools to generate and visualize CRON expressions easily.
