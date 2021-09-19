import logging
  
def create_logger():
	logging.basicConfig(filename="city_finder_dashboard.log",
	                    format='%(asctime)s %(message)s',
	                    filemode='w')
	logger=logging.getLogger()
	logger.setLevel(logging.INFO)
	return logger