import os

TITLE = "User Image System"
DESCRIPTION = "This system shall store users images along the time," \
              " and as a banking application, it may be audited."
VERSION = "1.0.0"

# DATABASE
DB_PORT = os.environ.get("DB_PORT", 5432)
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_NAME = os.environ.get("DB_NAME", "user_image_db")
DB_USER = os.environ.get("DB_USER", "user_image")
DB_PASS = os.environ.get("DB_PASS", "user-pass*2021")
DB_SCHEMA = "user_system_image"
