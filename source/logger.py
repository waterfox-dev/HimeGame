import os
import time

from datetime import datetime


def get_time(millisecond=True) -> str:
    if millisecond:
        return f"{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}.{datetime.now().microsecond}"
    else:
        return f"{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}"


class _Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m' 
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Logger:

    def __init__(self, write=False) -> None:

        self.write = write

        if self.write:
            self.w_file = open(f'log/log.txt', 'w')
            self.w_file.write(f"--HIME-- || DATE : {get_time()} \n")

        self.start_time = get_time()

    def __del__(self) -> None:

        if self.write:
            try:
                self.w_file.close()
            except AttributeError:
                pass

    def log(self, context: str, message: str):

        message = f"[{get_time()}][{context}] -> {message}"
        print(message)

        if self.write:            
            self.w_file.write(message + '\n')

    def warn(self, context: str, message: str):

        message = f"[{get_time()}][{context}] -> {message}"
        print(_Colors.WARNING + message + _Colors.ENDC) 

        if self.write:
            self.w_file.write(message + " (warn)" + '\n')
    
    def fail(self, context: str, message: str):

        message = f"[{get_time()}][{context}] -> {message}"
        print(_Colors.FAIL + message + _Colors.ENDC) 

        if self.write:
            self.w_file.write(message + " (fail)" + '\n')
    
    def succeed(self, context: str, message: str):

        message = f"[{get_time()}][{context}] -> {message}"
        print(_Colors.OKGREEN + message + _Colors.ENDC) 

        if self.write:
            self.w_file.write(message + " (succeed)" + '\n')