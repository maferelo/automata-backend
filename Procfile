web: alembic upgrade head && gunicorn main:app \
        --access-logfile - \
        -k uvicorn.workers.UvicornWorker \
        -w 4
