#!/usr/bin/python3
import requests
from methods.sendTeams import sendTeams
from methods.check_service import check_service
from datetime import datetime
import config #imports variables from config.py file
import time

#disables ssl warnings and set the time for the reports
requests.packages.urllib3.disable_warnings() 
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

def main():
    while True:
        for service in config.services:
            check_service(service, config.services.get(service))

        if config.errors == 0:
            sendTeams(config.reportHook, dt_string, config.upServices)
        time.sleep(config.timer)
        config.upServices = []
        config.errors = 0

if __name__ == "__main__":
    main()