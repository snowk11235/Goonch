"""
import json
import psycopg2

DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "goonch"
DB_PASS = "goonch"

def connect():
    conn = psycopg2.connect(dbname=DB_NAME,)


def open_db(filename: str):
    pass

def create_new_table():
"""