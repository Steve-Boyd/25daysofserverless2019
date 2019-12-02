import datetime
import logging

import azure.functions as func


def main(lightCandles: func.TimerRequest) -> None:

    # Stockholm time is UTC +1 and all triggers have been adjusted accordingly
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if lightCandles.past_due:
        logging.info('Light Candles!')

    else:
        logging.info('Hmm, something happened.')

    logging.info('Python timer trigger function ran at UTC time %s',
                 utc_timestamp)
