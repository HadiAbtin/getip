# Getip returns container IP 
# Copyright 2024, Hadi Abtinfar <hadi.abtinfar@gmail.com>

from flask import Flask, url_for
import psutil, socket

app = Flask(__name__)

app.config["JSONIFY_PRETTYPRINT_REGULAR"] = 1

@app.route("/")
def index():
    return f"""<!DOCTYPE html>
<html>
    <body>
        <div id="main">
            <h1>Available endpoints:</h1>
            <ul>
                <li><a href="{url_for('getip')}">/getip</a></li>
            </ul>
            <a href="https://github.com/HadiAbtin/getip">GetIP</a>
        </div>
    </body>
</html>"""

@app.route("/getip")
def getip():

    """
    This API returns all IPs of the container(or host)
    """
    ip_addresses = {}
    result_text = ""
    interfaces = psutil.net_if_addrs()
    for interface_name, interface_addresses in interfaces.items():
        for address in interface_addresses:
            if address.family == socket.AF_INET or address.family == socket.AF_INET6:
                ip_addresses.setdefault(interface_name, []).append(address.address)
    for interface, addresses in ip_addresses.items():
        result_text += f"{interface}: {', '.join(addresses)}\n"
    return result_text
