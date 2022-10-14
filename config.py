import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", "10261086"))
    API_HASH = os.environ.get("API_HASH", "9195dc0591fbdb22b5711bcd1f437dab")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5775270763:AAGhMhC3zM2Dpr6iDr2rIwNcT-JU_MnPswU") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "BQAPRoR-7aiKgCzT9onZpog3s-cY2nDB9R053CswOxVx0TVmDZWVkb3QrE6fwMeioIR1Reeq4Z0HvyFdBUlFjg8pqdS-xR_o5HjaK5n0mBpXt0SauiO1YMdNDXLOFbcUeFTOs-FE2tZBgC-mDVHtoFaIxm13h1BSmC8D3T2KTkePDU-0pNqQAv0nwicDiCa39QL-6BU5tUljn3wrq9XNtS2OSMf7Yq8ulOmzv_DmyzchKPOjxnEsghAPLu00sdt_Y2iCVz_1qIRkGB0kZJ6k_PvlHGh3JNB3aHg_N39vhhohjW4BpbmFWtWJFnUwRftFgEVU4fVC61Cii-E8556SqGNYVQgE6gA" 
    OWNER_ID = os.environ.get("OWNER_ID", "1426588906")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://hbbot:hbbot@cluster0.byhu9r2.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","hbbot")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    SESSION = os.environ.get("SESSION", "BQAPRoR-7aiKgCzT9onZpog3s-cY2nDB9R053CswOxVx0TVmDZWVkb3QrE6fwMeioIR1Reeq4Z0HvyFdBUlFjg8pqdS-xR_o5HjaK5n0mBpXt0SauiO1YMdNDXLOFbcUeFTOs-FE2tZBgC-mDVHtoFaIxm13h1BSmC8D3T2KTkePDU-0pNqQAv0nwicDiCa39QL-6BU5tUljn3wrq9XNtS2OSMf7Yq8ulOmzv_DmyzchKPOjxnEsghAPLu00sdt_Y2iCVz_1qIRkGB0kZJ6k_PvlHGh3JNB3aHg_N39vhhohjW4BpbmFWtWJFnUwRftFgEVU4fVC61Cii-E8556SqGNYVQgE6gA"
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001652623781"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", None)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
