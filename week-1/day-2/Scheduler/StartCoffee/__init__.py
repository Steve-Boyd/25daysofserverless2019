import azure.functions as func
import datetime
import logging

from importlib.machinery import SourceFileLoader
notify = SourceFileLoader("notify", "/home/steve/projects/serverless-challenge/week-1/day-2/Scheduler/notify.py"
                          ).load_module()


def main(startCoffee: func.TimerRequest) -> None:

    # Stockholm time is UTC +1 and all triggers have been adjusted accordingly
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    message = "Start the coffee and take out the cups."

    if startCoffee.past_due:
        logging.info(message)
        notify.main(message)

    else:
        logging.info('Hmm, something happened.')

    logging.info('Python timer trigger function ran at UTC time %s',
                 utc_timestamp)
