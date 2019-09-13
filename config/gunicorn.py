# https://docs.gunicorn.org/en/latest/settings.html
import multiprocessing

bind = '0.0.0.0:8000'

# https://docs.gunicorn.org/en/latest/design.html#how-many-workers
workers = multiprocessing.cpu_count()

# https://docs.gunicorn.org/en/latest/settings.html#reload
reload = True

# https://docs.gunicorn.org/en/latest/settings.html#reload-engine
reload_engine = 'poll'