import logging

logger = logging.getLogger(__name__)

def divide(a, b):
    logger.info("Attempting to divide %s by %s", a, b)
    
    try:
        if b == 0:
            raise ZeroDivisionError("Number cannot divided by zero")
        
        return a /b
    except ZeroDivisionError:
        logger.exception("A division error occurred while processing the request.")
        raise
    
    

print(divide(2,0))