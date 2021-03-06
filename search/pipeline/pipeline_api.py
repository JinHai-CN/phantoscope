from flask import Blueprint
from flask_restful import reqparse
from common.common import from_view_dict, json_response
from pipeline.pipeline import all_pipelines
from pipeline.pipeline import pipeline_detail
from pipeline.pipeline import new_pipeline
from pipeline.pipeline import delete_pipeline


pipeline = Blueprint("pipeline", __name__)


@pipeline.route("/")
@json_response
def pipeline_list_api():
    return all_pipelines()


@pipeline.route("/<name>")
@json_response
def pipeline_detail_api(name):
    return pipeline_detail(name)


@pipeline.route("/<name>", methods=['POST'])
@json_response
def new_pipeline_api(name):
    args = reqparse.RequestParser(). \
        add_argument("input", type=str, required=True). \
        add_argument("description", type=str, required=True). \
        add_argument("processors", type=str, required=True). \
        add_argument("encoder", type=str, required=True). \
        add_argument("indexFileSize", type=int, required=True). \
        parse_args()
    args = from_view_dict(args)
    args['name'] = name
    return new_pipeline(**args)


@pipeline.route("/<name>", methods=['DELETE'])
@json_response
def delete_pipeline_api(name):
    return delete_pipeline(name)
