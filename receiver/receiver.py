from flask import Flask
from influxdb import InfluxDBClient
import logging
import settings
import signal
import sys
import random
from datetime import datetime

logging.basicConfig(format=settings.LOG_FORMAT,
                    level=settings.LOG_LEVEL, stream=sys.stderr)


app = Flask(__name__)

"""Instantiate a connection to the InfluxDB."""
client = InfluxDBClient(settings.DB_HOST, settings.DB_PORT, settings.DB_USER,
                        settings.DB_PASSWORD, settings.DBNAME)


def signal_handler(signum, frame):
    logging.info("Receiver is stopped")
    signal.signal(signum, signal.SIG_IGN)  # ignore additional signals
    client.close()  # close HTTP connection
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


@app.route('/data')
def put_data():
    json_body = [
        {
            "measurement": "maple_farm",
            "tags": {
                "region": "yanaul"
            },
            "time": datetime.now(),
            "fields": {
                "temperature": 25.4,
                "pressure": 3.3,
                "engine_speed": 300,
                "fuel_level": 89
            }
        }
    ]

    logging.info("Write points: {0}".format(json_body))
    client.write_points(json_body)

    return 'The fields were recorded'


if __name__ == '__main__':
    logging.info('Receiver is starting')
    app.run(host='0.0.0.0')
