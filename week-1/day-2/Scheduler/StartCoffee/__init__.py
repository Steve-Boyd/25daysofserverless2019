import datetime
import logging

import azure.functions as func


def main(startCoffee: func.TimerRequest) -> None:

    # Stockholm time is UTC +1 and all triggers have been adjusted accordingly
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if startCoffee.past_due:
        logging.info('Start the coffee and take out the cups.')

    else:
        logging.info('Hmm, something happened.')

    logging.info('Python timer trigger function ran at UTC time %s',
                 utc_timestamp)
