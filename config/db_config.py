import os

# redis config
REDIS_DB_HOST = "127.0.0.1"  # your redis host
REDIS_DB_PWD = os.getenv("REDIS_DB_PWD", "")  # your redis password

# mysql config
RELATION_DB_PWD = os.getenv("RELATION_DB_PWD", "A23417!wobulijieya!ug")  # your relation db password
RELATION_DB_URL = f"mysql://root:{RELATION_DB_PWD}@localhost:3306/momo_research_db"

# save data to database option
IS_SAVED_DATABASED = True  # if you want to save data to database, set True
