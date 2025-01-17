"""
XSSCon - 2019/2020
This project was created by menkrep1337 with 407Aex team. 
Copyright under the MIT license
"""
from XSSCon.lib.helper.helper import G, N, R, Y
from datetime import datetime


class Log:
    @classmethod
    def info(self, text):
        print(
            "["
            + Y
            + datetime.now().strftime("%H:%M:%S")
            + N
            + "] ["
            + G
            + "INFO"
            + N
            + "] "
            + text
        )

    @classmethod
    def warning(self, text):
        print(
            "["
            + Y
            + datetime.now().strftime("%H:%M:%S")
            + N
            + "] ["
            + Y
            + "WARNING"
            + N
            + "] "
            + text
        )

    @classmethod
    def high(self, text):
        print(
            "["
            + Y
            + datetime.now().strftime("%H:%M:%S")
            + N
            + "] ["
            + R
            + "CRITICAL"
            + N
            + "] "
            + text
        )
