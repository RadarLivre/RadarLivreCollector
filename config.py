SERVER_HOST = "localhost:8000"

LOGIN = "joao"
PASSWORD = "marianna123"
COLLECTOR_ID = "29384c61-c588-488f-9390-52251d6491ed"

# Define a location to local database
DATABASE_DIR = "data"

# Define a location to log files
LOG_DIR = "log"

# Override with the collector adress, normaly located in /dev/ttyACM...
COLLECTOR_ADDRESS = '/dev/ttyACM0'

# 60 seconds. After this time, the not sent messages will be deleteds. Meassured in milliseconds
MAX_MESSAGE_AGE = 60 * 1000

DATA_OUTPUT_ENABLED = False
DATA_OUTPUT_HOST = "127.0.0.1"
DATA_OUTPUT_PORT = 30003

LOCAL_DATA_ENABLED = False
