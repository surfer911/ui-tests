# Snapdeal E-commerce Network calls Testing Project

This project aims to perform basic tests on the popular e-commerce website [Snapdeal](https://www.snapdeal.com/).

## Overview

The project involves the following tests:

1. **Product Search Test**: Searches for a specified product and verifies if relevant search results appear.
2. **Network Inspection Test**: Checks the network traffic for HTTP calls made during the test.
   - Specifically looks for events that are analytics-related.
   - Examines specific key-value pairs inside the POST calls.


## How To Run


1. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

2. Navigate to the tests directory:

    ```bash
    cd tests
    ```

3. Run the tests using pytest:

    ```bash
    python3 -m pytest test_search_analytics.py
    ```


## Analytics Call Sample

A sample analytics call structure is provided below
Captures    "eventName": values and stores for further evaluation


- **URL**: `https://log.snapdeal.com/eventData`
- **Payload**:

```json
{
  "orgId": "1001_1",
  "email": "",
  "cookieId": "171202619708658538",
  "appType": "WEB",
  "platformType": "MacIntel",
  "assetVersion": "1639746993560",
  "browserDetails": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
  "eventTypes": [
    {
      "eventType": "clickStream",
      "eventName": "eventLoggingLogging",
      "timestamp": "2024-04-02 12:40:47.414",
      "eventValuesV2": [
        {
          "type": "notificationSWErrorWeb",
          "name": "notifPermission",
          "values": "default"
        }
      ],
      "abTest": "akm",
      "locale": "en",
      "evtId": "1712029247413_6900_171202619708658538",
      "currUrl": "https://www.snapdeal.com/search?keyword=shirt&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=",
      "refPg": "searchResult",
      "refPgId": "1712029247096_3044_171202619708658538"
    }
  ],
  "imsId": ""
}
