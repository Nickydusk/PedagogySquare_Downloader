import json
import logging
import os
import re
import time
from contextlib import closing

import requests
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pandas as pd
home_dir = r"D:\OneDrive - smail.nju.edu.cn\desktop\home"
os.chdir(home_dir)
files = pd.read_csv("./list.csv",header=None,encoding="gbk").values[:,0].tolist()
files = pd.DataFrame(files)
files.to_csv("./list.csv",header=False,index=False,encoding="gbk")
print("Done!")