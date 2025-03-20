import os
import multiprocessing
import time
import argparse


from modules.utils import on_pi, get_logger_params
from modules.logging_system import Logger
from settings.settings import load_config
from modules.display_app import DisplayApp

ON_PI = on_pi()
UUID_VAL, USER = get_logger_params(ON_PI)

current_path = os.getcwd()
config_path = os.path.join(current_path, 'settings', 'settings.json')
app_settings = load_config(config_path)

feature_flags = app_settings.get('features')
log_level = app_settings.get('logging').get('level')
load_display_module = feature_flags.get('displayEnabled')

global_logger = Logger(log_level)

if load_display_module:
    display_app = DisplayApp()

