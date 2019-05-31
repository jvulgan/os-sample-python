import os

from flask import Flask

application = Flask(__name__)


@application.route("/")
def hello():
    return "Hello World!"


@application.route("/host")
def replicas():
    return "Host: {}".format(os.getenv("HOSTNAME", "unknown"))


if __name__ == "__main__":
    application.run()
