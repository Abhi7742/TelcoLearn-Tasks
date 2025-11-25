import logging
logging.basicConfig(filename="add_config", level=logging.WARNING)
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
