import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", "10261086"))
    API_HASH = os.environ.get("API_HASH", "9195dc0591fbdb22b5711bcd1f437dab")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5775270763:AAGhMhC3zM2Dpr6iDr2rIwNcT-JU_MnPswU") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "1BVtsOLYBu6Q3dK2NuQo8LOjXAUnYIJznSkyz5lmY0pciVEsilwT1crShxNZLusyAkLcoFpbbggPmMQ0uH0nsOzIdllYVq39rpGeArkTea6rwlqmhiO9eim54u_970UT7Y6j7gel0772sWT1XLaMK8TDeBDCF88vvJHAj9PjZkVC7yiw6Rb66lAL2A836FSGmY43M48qiAdTEyEc3kLGrhuyRTsrvXvgYVLck4AE7OZDVhJVYBa42AHImGZpDfn95yx40Ln-hawNrnAve-WBsYaqqiCN4n_A_P0fXvFcOPBftnjR_npoY5C6PHkVjElg8P5qZKlyhkDj5R6g4hJrvdcqVkGIQJJs=") 
    OWNER_ID = os.environ.get("OWNER_ID", "1426588906")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://hbbot:hbbot@cluster0.byhu9r2.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","hbbot")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    SESSION = os.environ.get("SESSION", "1BVtsOLYBu6Q3dK2NuQo8LOjXAUnYIJznSkyz5lmY0pciVEsilwT1crShxNZLusyAkLcoFpbbggPmMQ0uH0nsOzIdllYVq39rpGeArkTea6rwlqmhiO9eim54u_970UT7Y6j7gel0772sWT1XLaMK8TDeBDCF88vvJHAj9PjZkVC7yiw6Rb66lAL2A836FSGmY43M48qiAdTEyEc3kLGrhuyRTsrvXvgYVLck4AE7OZDVhJVYBa42AHImGZpDfn95yx40Ln-hawNrnAve-WBsYaqqiCN4n_A_P0fXvFcOPBftnjR_npoY5C6PHkVjElg8P5qZKlyhkDj5R6g4hJrvdcqVkGIQJJs=")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001652623781"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", None)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
