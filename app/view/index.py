"""
主页
"""
from flask import Blueprint

index = Blueprint('index', __name__)


@index.route('/')
def index():
    return "这是上传页面"
