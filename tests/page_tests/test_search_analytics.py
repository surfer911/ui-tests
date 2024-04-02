from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from tests.page_tests.conftest import print_event_info, clear_request_history


"""
   Test the title for snapdeal website
"""
def test_title_anonymous_user(driver):
    driver.get("https://m.snapdeal.com/")
    assert "Shop Online" in driver.title, "Expected Shop Online in title"

"""
    Test the search functionality of the Snapdeal website
    Test if analytics events are being pushed properly with correct 
    keys and values
"""
def test_search_and_read_network_tab_anonymous_user(driver):
    clear_request_history(driver)
    event_data_request_on_page = 0 #used to count analytic calls

    # perform search for a product
    try:
        url = "https://www.snapdeal.com/"
        search_term = "t-shirt"
        driver.get(url)

        search_input_box= driver.find_element(By.XPATH, value="//span[@id='preFillInput']")
        search_input_box.send_keys("t-shirt")

        search_button = "//span[@class='searchTextSpan']"
        driver.find_element(By.XPATH, search_button).click()

        search_result_text = driver.find_element(By.XPATH, "//div[@id='searchMessageContainer']/descendant::span[2]")
        search_result_message = search_result_text.text

        ''' reads the network tab to get http network calls such as eventData (analytics calls) saves the key value pairs from POST calls in a JSON '''
        for request in driver.requests:
            if request.response:
                # The analytics call has URL https://log.snapdeal.com/eventData
                # request.path means the URL.
                if 'eventData' in request.path:
                    event_data_request_on_page += 1
                    print('*******************')
                    print(request.path)
                    print(request.body)
                    print('\n\n')
                    print_event_info("Landing page ", request.body, event_data_request_on_page)

        # assert to check if the search term appears like 'showing results for search_term'
    except NoSuchElementException as e:
        print("error ", e)

    assert search_term in search_result_message
