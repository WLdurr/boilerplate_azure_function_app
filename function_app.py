# this file is used for the execution of your function app
import azure.functions as func
import logging
from function_file import function_I_want_to_execute # obviously change to your settings

app = func.FunctionApp()

# This is a boilerplate for a function app that is triggered by a certain time interval, example: daily
@app.timer_trigger(schedule="0 0 0 * * *", arg_name="myTimer", run_on_startup=True, use_monitor=True)
def some_function_name(myTimer: func.TimerRequest) -> None: # change function name
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Timer triggered. Running function...')
    function_I_want_to_execute()
    logging.info('function completed.')
