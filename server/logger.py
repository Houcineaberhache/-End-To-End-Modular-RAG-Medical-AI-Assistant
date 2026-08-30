import logging
#we will use this logger to get to see whatever happens in our application 
def setup_logger(name="MedicalAssistant"):
    logger=logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    ch=logging.StreamHandler()
    ch.setLevel(logging.DEBUG)


    formatter=logging.Formatter("[%(asctime)s] [%(levelname)s] --- [%(message)s]")
    ch.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(ch)

    return logger



logger=setup_logger()
# Once created, you call different methods depending on severity:
logger.info("RAG prcoess started") # normal event, everything's fine
logger.debug("Debugging") # detailed info, only useful while developing
logger.error("Failed to load") # something broke, but app keeps running
logger.critical("Critical message") # serious failure, app may crash

# This file creates a reusable "logger" — a smarter version of print()
# that adds timestamps and severity levels to every message.

# setup_logger() builds one logger object:
# - It listens for ALL message levels (DEBUG and above)
# - It prints messages to the console (StreamHandler)
# - It formats each line as: [time] [level] --- [message]
# - It checks "if not logger.hasHandlers()" so calling this function
#   multiple times doesn't duplicate log output
