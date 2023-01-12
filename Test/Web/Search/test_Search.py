from Test.BaseTest.base import *


class Test_SearchBox(BaseTest):
    def test_Existing_Product(self):
        SEARCH = super()
        SEARCH.initial()                                                # Initial Web address
        SEARCH.click(Search_Path)                                       # Click on the search button
        SEARCH.send_key(INPUT_onSearch_Box, 'Bright Red Bag')             # enter Firstname
        SEARCH.click(Search_Path)                                       # Click on the search button
        search_result = SEARCH.text_xpath(Search_Display)                # Find existing product ul
        assert 'Bright Red Bag' == search_result                         # Display search result
        SEARCH.tear_down()

    def test_NonExisting_Product(self):
        SEARCH = super()
        SEARCH.initial()                                                # Initial Web address
        SEARCH.click(Search_Path)                                       # Click on the search button
        SEARCH.send_key(INPUT_onSearch_Box, 'Adidas')                   # Enter product name
        SEARCH.click(Search_Path)                                        # Click on the search button
        product = SEARCH.title(Non_ExistingProduct_Ul)                    # Find non-existing product ul
        assert product == "Sorry, but nothing matched your search terms. Please try again with some different keywords."  # display error message
        SEARCH.tear_down()

    def test_null(self):
        SEARCH = super()
        SEARCH.initial()                                        # Initial Web address
        SEARCH.click(Search_Path)                                 # Click on the search button
        SEARCH.send_key(INPUT_onSearch_Box, '')                  # Enter blank
        SEARCH.click(Search_Path)                                 # Click on the search button
        product = SEARCH.driver.title                              # Find AtidStore page
        assert product == "ATID Demo Store – ATID College Demo Store for Practicing QA Automation"  # display AtidStore
        SEARCH.tear_down()
