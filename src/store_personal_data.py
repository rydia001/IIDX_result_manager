#!/usr/bin/env python3
# coding: utf-8

import os, sqlite3
from contextlib import closing

data_dir = "./personal_data/"
latest_dbname = data_dir+"latest.db"
log_dbname = data_dir+"log.db"


def get_music(music_data, cursor):
    rec = cursor.execute(u"""select * from latest where 
                    Name = ? and SPDP = ? and Difficulty = ?""",
                    (d["Music"], d["SPDP"], ["Difficulty"]))
    return rec.fetchone()


def store_latest(data, dbname):
    conn = sqlite3.connect(latest_dbname)
    c = conn.cursor()
    init_sql = """create table if not exists 'latest' (
           'ID' integer primary key,
           'Name' varchar(64) not null,
           'SPDP' integer not null,
           'Difficulty' integer not null,
           'LEVEL' integer not null,
           'Clear' integer not null,
           'DJLEVEL' integer not null,
           'Score' integer not null);"""

    c.execute(init_sql)
    for music_data in data:
        d = music_data.get_data()
        
        

def store_log(data):


def store_personal_data(data):
    if not os.path.isdir(data_dir):
        os.mkdir(data_dir)
    
