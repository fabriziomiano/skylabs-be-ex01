"""
API Blueprint
"""
from flask import Blueprint

STATS_SCHEMA = {
    "type": "object",
    "required": ["aggregationType", "aggregationValue"],
    "properties": {
        "aggregationType": {"type": "string"},
        "aggregationValue": {"type": "integer"},
    },
}
ACCEPTED_AGGREGATION_TYPES = ("age", "education_level_id", "occupation_id")

api = Blueprint("api", __name__, url_prefix='/api')

from . import endpoints
