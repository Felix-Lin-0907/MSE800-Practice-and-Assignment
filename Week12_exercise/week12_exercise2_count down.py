import time

# Slow down decorator
def slow_down(interval=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(interval)  # Pause the function for 'interval' seconds
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Applying slow_down decorator to the countdown function
@slow_down(1)  # Slows down by 1 second between calls
def count_down(n=10):
    if n > 0:
        print(n)
        count_down(n-1)
    else:
        print("Countdown ends!")

# Calling the countdown function
count_down(10)