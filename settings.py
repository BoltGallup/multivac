import configparser
import os

from dotenv import load_dotenv
from pathlib import Path

from multivac.src import utilities


cfg = configparser.ConfigParser()
cfgDIR = Path(__file__).resolve().parent

try:
    cfg.read(cfgDIR / config_file_name)
except NameError:
    cfg.read(cfgDIR / 'multivac.cfg')

root_dir = cfg['PATHS'].get('root_dir', cfgDIR / 'multivac')
data_dir = cfg['PATHS'].get('data_dir', root_dir / 'data')
raw_dir = cfg['PATHS'].get('raw_dir', data_dir/'raw')
interim_dir = cfg['PATHS'].get('interim_dir', data_dir/'interim')
processed_dir = cfg['PATHS'].get('processed_dir', data_dir/'processed')
metadata_dir = cfg['PATHS'].get('metadata_dir', processed_dir/'metadata')
models_dir = cfg['PATHS'].get('models_dir', root_dir/'models')

# Get search and filter settings; default to empty lists
terms = eval(cfg['SEARCH'].get('terms', '[]'))
sources = eval(cfg['SEARCH'].get('sources', '[]'))
arxiv_drops = eval(cfg['FILTER'].get('drops', '[]'))

# make data directories if they don't already exist
dirs = [data_dir, raw_dir, interim_dir, processed_dir, metadata_dir, models_dir]
dirs += [raw_dir / x for x in sources]
for _dir in dirs:
    utilities.mkdir(_dir)



