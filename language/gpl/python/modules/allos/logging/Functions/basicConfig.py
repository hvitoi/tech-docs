# %%
import logging

# Basic configuration for the logging system
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
    datefmt="%m-%d %H:%M",
    filename="installer.log",
    filemode="w",
)
