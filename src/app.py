import copy
import os

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from loguru import logger

from .manager import FileManager

logger.info("Initialized app . . .")
app = Flask(__name__)


@app.route("/api/extract/", methods=["POST"])
def extract():
    logger.info("Inside extract")

    ...


def main():
    app.run()


if __name__ == "__main__":
    main()
