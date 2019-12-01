import logging
import random
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
        logging.info('Python HTTP trigger function processed a driedel spin.')
        choices = ["נ","ג" ,"ה" ,"ש"]
        return func.HttpResponse(body="You spun " + random.choice(["נ","ג" ,"ה" ,"ש"]))
