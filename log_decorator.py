import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def custom_log_decorator(debug=True):
    def decorator(func):
        def wrapper():
            if debug:
                start_time = time.time()
                logger.info(f"Execution started at {start_time}")
            func()
            if debug:
                end_time = time.time()
                logger.info(f"Execution ended at {end_time}")
                logger.info(f"Execution took {end_time - start_time} seconds")
        return wrapper
    return decorator

@custom_log_decorator(debug=True)
def long_function():
    time.sleep(5)
    print("Inside the function")

@custom_log_decorator(debug=False)
def other_function():
    time.sleep(2)
    print("Another function")

if __name__ == "__main__":
    long_function()

