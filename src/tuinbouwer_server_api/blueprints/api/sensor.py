"""Sensor API V1 blueprint"""

from datetime import datetime

from sqlalchemy.exc import IntegrityError
from flask import Blueprint, abort, request

from tuinbouwer_server_api import models, functions


blueprint = Blueprint('api_sensor', __name__, url_prefix='')

@blueprint.route('/api/sensor/v1', methods=(['GET', 'POST']))
@blueprint.route('/sensor_api/v1/', methods=(['GET', 'POST']))
def get_sensor_log():
    """Route to POST sensor data"""
    if request.method == 'GET':
        return "Send 'POST' with json data: temperature, humidity, power, space_id"
    sensor_log = models.MinuteLog()
    sensor_log.date_time = functions.round_time(datetime.now(), 60)
    sensor_log.temperature = request.json.get('temperature')
    sensor_log.humidity = request.json.get('humidity')
    sensor_log.power = request.json.get('power')
    sensor_log.space_id = request.json.get('space_id')
    try:
        models.db.session.add(sensor_log)
        models.db.session.commit()
        return sensor_log.to_dict()
    except IntegrityError:
        return "IntegrityError, make sure you have the json data:\n" + \
            "temperature, humidity, power, space_id\n" + str(sensor_log.to_dict()), 409

@blueprint.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    return abort(404)
