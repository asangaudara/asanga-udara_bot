class Development(Config):
    OWNER_ID = 1149011555  # your telegram ID
    OWNER_USERNAME = "Asanga_Udara"  # your telegram username
    API_KEY = "1620387694:AAFuoojnXlAvl2TAgU5b4GCaSjVaw5ohQPM"  # your api key, as provided by the @botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin-038392:Qi9V@v!jkTW2MbKi@127.0.0.1:3306:5432/database'  # sample db credentials
    JOIN_LOGGER = '-1234567890' # some group chat that your bot is a member of
    USE_JOIN_LOGGER = True
    SUDO_USERS = [18673980, 83489514]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
    
    

