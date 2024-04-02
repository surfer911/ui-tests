import os

import pytest
from selenium import webdriver
from seleniumwire import webdriver
import json

@pytest.fixture()
def driver():
    current_dir = os.getcwd()
    project_root = os.path.dirname(os.path.dirname(current_dir))
    chrome_driver_path = os.path.join(project_root, 'browser_drivers', 'chromedriver')

    chrome_options = webdriver.ChromeOptions()

    #use a mobile browser
    chrome_options.add_argument(
        '--user-agent=Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Mobile Safari/537.36')
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)


    # Wait for upto 30 seconds  per element
    driver.implicitly_wait(30)
    yield driver

    # teardown tests by killing the browser instance
    driver.quit()

sub_json_list = []

''' Make a list of the keys from a network call POST data, number of times a network call has appeared'''
def print_event_info(page_title, json_bytes, number_of_requests):
    decoded_data = json_bytes.decode('utf-8')
    parsed_data = json.loads(decoded_data)

    for event_info in parsed_data.get("eventTypes", []):
        event_type = event_info.get("eventType")
        event_name = event_info.get("eventName")
        ref_pg = event_info.get("refPg")

        sub_json = {
            "Page Title": page_title,
            "eventName": event_name,
            "eventType": event_type,
            "refPg": ref_pg,
            "numberOfRequests": number_of_requests,
        }

        sub_json_list.append(sub_json)
        print(f"eventType: {event_type}, eventName: {event_name}, refPg: {ref_pg}")


def clear_request_history(driver):
    driver.requests.clear()
    driver.backend.storage.clear_requests()