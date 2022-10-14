import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", "10261086"))
    API_HASH = os.environ.get("API_HASH", "9195dc0591fbdb22b5711bcd1f437dab")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5775270763:AAGhMhC3zM2Dpr6iDr2rIwNcT-JU_MnPswU") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "BQAFx9HucRkBO50mMypC93NXw9a6Xr9BOO3roJ2Qn9HNm3qJ9x0wEflAmGXeLwNOH8NI6yuF8BAsJovgnbAkaw_LXI-RERvK970Lg5IxnWgqrMBc9m6MW_JKDULt5ZeN8mML7ogKA6MK3rChAYPNmtBhaXBnb0GbeK_aYD9lzvgtNvLssw1hIDl2iXYYMx5_k7fzMmOoKkYVa-appiw1h4brc6hM68wXUXGP9lR2eQOj9tVkpITpmzwRS8OtI0cHYm10s0rWXvsZpxODQIOQh34UQJQNFxHJpuvNo8el1M7NlFCLsKR5XBLTCa6086dNXWThHhQPjJORnqhrzJjsovf6VQgE6gA") 
    OWNER_ID = os.environ.get("OWNER_ID", "1426588906")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://hbbot:hbbot@cluster0.byhu9r2.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","hbbot")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    SESSION = os.environ.get("SESSION", "BQAFx9HucRkBO50mMypC93NXw9a6Xr9BOO3roJ2Qn9HNm3qJ9x0wEflAmGXeLwNOH8NI6yuF8BAsJovgnbAkaw_LXI-RERvK970Lg5IxnWgqrMBc9m6MW_JKDULt5ZeN8mML7ogKA6MK3rChAYPNmtBhaXBnb0GbeK_aYD9lzvgtNvLssw1hIDl2iXYYMx5_k7fzMmOoKkYVa-appiw1h4brc6hM68wXUXGP9lR2eQOj9tVkpITpmzwRS8OtI0cHYm10s0rWXvsZpxODQIOQh34UQJQNFxHJpuvNo8el1M7NlFCLsKR5XBLTCa6086dNXWThHhQPjJORnqhrzJjsovf6VQgE6gA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001652623781"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", None)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
