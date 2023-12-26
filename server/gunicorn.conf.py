import multiprocessing

bind = "127.0.0.1:8000"
workers = 2 * multiprocessing.cpu_count() + 1
user = "ildus"
timeout = 120
raw_env = ["DJANGO_SETTINGS_MODULE=core.core.settings"]
