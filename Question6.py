# Best Practise while Handling Exception
import logging

logging.basicConfig(filename='test.log',level=logging.INFO)

try:
    a = 5+6
    logging.info("The addition of 5 and 6 is {}".format(a))
except Exception as e:
    logging.debug(e)
finally:
    logging.info("Program Executed")