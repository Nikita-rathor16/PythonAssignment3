"""import time and datetime"""
import time
import datetime
def log_execution_time(func):
    """.log the time"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        current_date = datetime.datetime.now()
        module_name = func.__module__
        log_file_name = f"{module_name}_{current_date.strftime('%Y%m%d')}.log"
        with open(log_file_name, 'a', encoding="utf-8") as file:
            file.write(f"Function {func.__name__} executed in {execution_time} seconds\n")
        return result
    return wrapper
@log_execution_time
def my_function():
    """Decorated this function """
    print("Function called !")
my_function()
