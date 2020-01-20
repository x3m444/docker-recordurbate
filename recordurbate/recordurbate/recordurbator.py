import logging
from pathlib import Path

from .ssdl.bot import Bot

log_folder_path = Path("/data", "logs")
if not log_folder_path.is_dir():
    log_folder_path.mkdir()

file_name_increment = 0
while Path(log_folder_path, "ssdl{0}.log".format(file_name_increment)).is_file():
    file_name_increment += 1

log_file_path = Path(log_folder_path, "ssdl{0}.log".format(file_name_increment))
if not log_file_path.is_file():
    log_file_path.touch()

logger = logging.getLogger('smdl')
logger.setLevel(logging.INFO)
fh = logging.FileHandler(str(log_file_path))
fh.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)

b = Bot(logger)
b.run()
