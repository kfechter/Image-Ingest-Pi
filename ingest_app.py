import os
import multiprocessing
import time
import argparse


from modules.utils import on_pi, get_logger_params
from settings.settings import load_config

ON_PI = on_pi()
UUID_VAL, USER = get_logger_params(ON_PI)

current_path = os.getcwd()
config_path = os.path.join(current_path, 'settings', 'settings.json')
app_settings = load_config(config_path)

feature_flags = app_settings.get('features')
logging_setting = app_settings.get('logging').get('level')
load_display_module = feature_flags.get('displayEnabled')
load_web_module = feature_flags.get('webEnabled')