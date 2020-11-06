# -*- coding: utf-8 -*-
import requests
from sqlalchemy import Integer
from sqlalchemy import Column, String, create_engine, TEXT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json
from concurrent.futures import ThreadPoolExecutor
import time
import pandas as pd

Base = declarative_base()
metadata = Base.metadata
engine = create_engine(
    'mysql+pymysql://root:416798@127.0.0.1/test')
DBSession = sessionmaker(bind=engine)
session = DBSession()

for item in range(10000):
    print(id(session))