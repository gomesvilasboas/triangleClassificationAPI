from multiprocessing import cpu_count

bind = '0.0.0.0:8080'
timeout = 2
max_requests = 1000
worker_class = 'sync'
workers = 2  # cpu_count()
loglevel = 'info'
reload = True
reload_engine = 'auto'
disable_redirect_access_to_syslog = True
