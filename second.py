import logging
# print(dir(logging))
logging.basicConfig(filename='message.log',filemode='a',format='%(asctime)s %(name)s - %(levelname)s - %(message)s')
logging.warning('This third warning message will be logged to the file.')
