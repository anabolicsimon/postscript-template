import threading

# run tasks in parallelo !non toccare

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()