from Test.BaseTest.base import *
from Test.BaseTest.base import is_element_exist


class Test_women(BaseTest):
    def test_search_existingProduct(self):
        WOMEN = super()
        WOMEN.initial()  # Initial Web address
        WOMEN.click(Women_categoryPage)  # Click on "Women" Product Catagory button
        WOMEN.click(Product_searchBox)  # Click on Search box
        WOMEN.send_key(ProductINPUT_searchBox,"Flamingo Tshirt")  # Enter product name
        WOMEN.click(Search_NextArrow)  # Click on next arrow
        product = WOMEN.title(ExistingProduct_Ul)  # Find existing product ul
        assert product == "Flamingo Tshirt"  # display product
        WOMEN.tear_down()

    def test_search_NonExistingProduct(self):
        WOMEN = super()
        WOMEN.initial()  # Initial Web address
        WOMEN.click(Women_categoryPage)  # Click on "Women" Product Catagory button
        WOMEN.click(Product_searchBox)  # Click on Search box
        WOMEN.send_key(ProductINPUT_searchBox,"puma")  # Enter product name
        WOMEN.click(Search_NextArrow)  # Click on next arrow
        product = WOMEN.title(Non_ExistingProduct_Ul)  # Find non-existing product ul
        assert product == "Sorry, but nothing matched your search terms. Please try again with some different keywords."  # display error message
        WOMEN.tear_down()

    def test_adding_product_from_WomenCatagory_into_cart(self):
        WOMEN = super()
        WOMEN.initial()  # Initial Web address
        WOMEN.click(Women_categoryPage)  # Click on "Women" Product Catagory button
        WOMEN.click(Women_SelectProductBody)  # Click on the product "Blue Denim Shorts"
        WOMEN.click(AddToCart)  # Click add to cart button
        WOMEN.click(ViewCart)  # Click cart view
        ProductName = WOMEN.text_xpath(Women_ContainProductName)  # Find product name ul
        assert "Blue Denim Shorts" == ProductName  # Display The product in cart view page
        WOMEN.tear_down()
    # def test_FilterPrice(self):
    # WOMEN = super()
    # WOMEN.initial()  # Initial Web address
    # WOMEN.click(Women_categoryPage)  # Click on "Women" Product Catagory button
    # WOMEN.click("")


class Test_Store(BaseTest):
    def test_Scroll_page3_display(self):
        SCROLL = super()
        SCROLL.initial()                                           # Initial Web address
        SCROLL.click(Store_categoryPage)                           # Click on Store Catagory
        SCROLL.driver.execute_script(SCRIPT)                       # Scroll to bottom
        SCROLL.click(Page3_path)                                   # Click on the 2nd page
        SCROLL.driver.implicitly_wait(2)
        NextPage = SCROLL.text_xpath(NEXTPage_Ul)                  # Find Next page Ul
        assert NextPage == 'Showing 25–31 of 31 results'           # Display 3 page

    def test_Scroll_to_page2_and_AddProduct_To_Cart(self):
        AddProduct = super()
        self.test_Scroll_page3_display()                         # Scroll to page 3
        AddProduct.click(Red_Hoodie)                             # Click Product
        AddProduct.click(AddToCart)                             # Click add to cart button
        AddProduct.click(ViewCart)                              # View Cart page
        cart_Page = AddProduct.driver.title                     # Find Cart page
        assert cart_Page == "Cart – ATID Demo Store"            # Display Cart page
        AddProduct.driver.implicitly_wait(2)


class Test_Add_SaleProduct_To_Cart(BaseTest):
    # Add to the cart just the product with sale & the original price > 72.00 (Bonus - Add all the products to the cart)
    def test_AddToTheCart_JustProduct_withSale_and_OriginalPriceMoreThan72(self):
        SALE_PRICE = super()
        SALE_PRICE.initial()                                             # Initial Web address
        SALE_PRICE.click(Store_categoryPage)                                  # Click on "Store" Product Catagory button.
        storePage = SALE_PRICE.driver.title                                      # Find Store Page
        assert 'Products – ATID Demo Store' == storePage                         # Check if StorePage displayed
        ui_product = SALE_PRICE.ul_(Ul_PRODUCTS)                                 # XPATH for Ul of product
        li_product = ui_product.find_elements(By.TAG_NAME, LI_PRODUCTS)            # Xpath list
        for element in li_product:
            SALE_PRICE.driver.implicitly_wait(10)                               # Screen timr out 10 sec
            price = SALE_PRICE.ul_(PRICE_NAV)                                   # Xpath for ul
            sale = is_element_exist('onsale', element)                          # Check element exist
            a = price.text                                                      # Display the price
            assert a == '80.00 ₪'
            casting = a[:-2]                                                     # Casting the string to number/int
            if float(casting) > 72.00 and sale == 'Sale!':
                element.click()                                                   # Click the product
                SALE_PRICE.click(AddToCart)                                        # Click add to cart button
                SALE_PRICE.click(ViewCart)                                         # View cart button
                cart_Page = SALE_PRICE.driver.title                                # Find Cart page
                assert cart_Page == "Cart – ATID Demo Store"                       # Display Cart page
        SALE_PRICE.tear_down()

    # In "Our Best Sellers" Section add only the products with 5-star rank
    def test_5star(self):
        STARRANK = super()
        STARRANK.initial()                                                   # Initial Web address
        STARRANK.click(Store_categoryPage)                                   # click on "Store" Product Catagory button.
        storePage = STARRANK.driver.title                                    # find Store Page
        assert 'Products – ATID Demo Store' == storePage                     # Check if StorePage displayed
        STARRANK.driver.implicitly_wait(2)
        for i,p in enumerate(PRODUCT_UL):
            LI_5STARTLocation = f"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/ul[1]/li[{i+1}]/a[1]/span[1]"
            rating = STARRANK.driver.find_element(By.XPATH,f"//li[{i+1}]/div[1]")
            if rating.accessible_name == "Rated 5.00 out of 5":
                STARRANK.click(LI_5STARTLocation)                               # Click on the product
                STARRANK.driver.implicitly_wait(2)
                STARRANK.click(AddToCart)                                         # Click Add to Cart button
                STARRANK.click(ViewCart)                                          # Click View to cart
                cartPage = STARRANK.title(Cart_Page)                              # Find Cart page ul
                assert cartPage == "Cart"                                         # Display Cart page
                STARRANK.driver.implicitly_wait(2)
            else:
                pass
        STARRANK.tear_down()


class Test_AddProduct(BaseTest):
    def test_Functionality_of_adding_Product_from_StoreCatagory_into_cart(self):
        Store = super()
        Store.initial()                                                      # Initial Web address
        Store.click(Store_categoryPage)                                      # Click on "Store" Product Catagory button.
        Store.click(Store_SelectProductBody)                                 # Click on the product "ATID Black Shoes"
        Store.click(AddToCart)                                               # Click add to cart button
        Store.click(ViewCart)                                                # Click cart view
        ProductName = Store.text_xpath(Store_ContainProductName)             # Find product name
        assert "ATID Black Shoes" == ProductName                             # Display The product in cart view page
        Store.tear_down()

    def test_Functionality_of_adding_item_from_MenCatagory_into_cart(self):
        MEN = super()
        MEN.initial()                                                     # Initial Web address
        MEN.click(Men_categoryPage)                                       # Click on "Men" Product Catagory button
        MEN.click(Men_SelectProductBody)                                  # Click on the product "Dark Blue Denim Jeans"
        MEN.click(AddToCart)                                              # Click add to cart button
        MEN.click(ViewCart).click()                                       # Click cart view
        ProductName = MEN.text_xpath(Men_ContainProductName)              # Find product name
        assert "Dark Blue Denim Jeans" == ProductName                     # Display The product in cart view page
        MEN.tear_down()

    def test_Functionality_of_adding_item_from_WomenCatagory_into_cart(self):
        WOMEN = super()
        WOMEN.initial()                                                     # Initial Web address
        WOMEN.click(Women_categoryPage)                                     # Click on "Women" Product Catagory button
        WOMEN.click(Women_SelectProductBody)                                # Click on the product "Blue Denim Shorts"
        WOMEN.click(AddToCart)                                              # Click add to cart button
        WOMEN.click(ViewCart)                                               # Click cart view
        ProductName = WOMEN.text_xpath(Women_ContainProductName)                  # Find product name
        assert "Blue Denim Shorts" == ProductName                           # Display The product in cart view page
        WOMEN.tear_down()

    def test_Functionality_of_adding_item_from_AccessoriesCatagory_into_cart(self):
        ACCESSORIES = super()
        ACCESSORIES.initial()                                              # Initial Web address
        ACCESSORIES.click(Accessories_categoryPage)                        # Click on "Assessors" catagory button
        ACCESSORIES.click(Accessories_SelectProductBody)                   # Click on the product "Buddha Bracelet"
        ACCESSORIES.click(AddToCart)                                       # Click add to cart button
        ACCESSORIES.click(ViewCart)                                        # Click cart view
        ProductName = ACCESSORIES.text_xpath(Accessories_ContainProductName).text  # Find product name
        assert "Buddha Bracelet" == ProductName                             # Display The product in cart view page
        ACCESSORIES.tear_down()

    def test_Functionality_of_inserting_CouponCode_Work_Properly(self):
        COUPONCODE = super()
        COUPONCODE.initial()                                           # Initial Web address
        COUPONCODE.click(Coupons_categoryPage)                         # Click on "Store" Product Catagory button
        COUPONCODE.click(Coupons_SelectProductBody)                    # Click on the product "Anchor Bracelet"
        COUPONCODE.click(AddToCart)                                    # Click add to cart button
        COUPONCODE.click(ViewCart)                                     # Click cart view
        ProductName = COUPONCODE.text_xpath(Coupons_ContainProductName)      # Find product name
        assert "Anchor Bracelet" == ProductName                        # Display The product in cart view page
        COUPONCODE.send_key(Coupons_InsertCode,"123")                  # Enter Coupon code
        COUPONCODE.click(Apply_CouponCode)                     # Click on Apply CouponsCode
        errorText = COUPONCODE.text_xpath(Coupon_Error_Message)              # Find Error message
        assert 'Coupon "123" does not exist!' == errorText             # Display Error message
        COUPONCODE.tear_down()
