import time

CNF = {
    'hour': 3600,
    'half_hour': 1800,
    'last_time_called': 0
}

def set_time():
    CNF['last_time_called'] = time.time()
