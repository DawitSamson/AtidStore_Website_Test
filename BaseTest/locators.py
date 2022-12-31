# This Locator is the Xpath Url for AtidStore website which help us on testing functionality code display Clearly
"""
+-+-+-+-++-+-+-+-+-+
|A|t|i|d|S|t|o|r|e|
+-+-+-+-++-+-+-+-+-+
"""
# Atid_store address
atidStore_WebAddress = "https://atid.store/"
AddToCart = "//button[contains(text(),'Add to cart')]"
ViewCart = "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/a[1]"

'''
+-+-+-+-+-+ +-+-+-+-+-+-+-+-+
|S|t|o|r|e| |C|a|t|a|g|o|r|y|
+-+-+-+-+-+ +-+-+-+-+-+-+-+-+
'''
# For store
store_categoryHeader = "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]"
store_SelectProductBody = "//body/div[@id='page']/div[@id='content']/div[1]/div[2]/main[1]/div[1]/ul[1]/li[2]/div[1]/a[1]/img[1]"
store_ContainProductName = "//a[contains(text(),'ATID Black Shoes')]"

'''
+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+
|A|c|c|e|s|s|o|r|i|e|s| |C|a|t|a|g|o|r|y|
+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+
'''
# For Accessories
Accessories_categoryHeader = "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[5]/a[1]"
Accessories_SelectProductBody = "//body/div[@id='page']/div[@id='content']/div[1]/div[2]/main[1]/div[1]/ul[1]/li[6]/div[1]/a[1]"
Accessories_ContainProductName = "//a[contains(text(),'Buddha Bracelet')]"

'''
+-+-+-+ +-+-+-+-+-+-+-+-+
|M|e|n| |C|a|t|a|g|o|r|y|
+-+-+-+ +-+-+-+-+-+-+-+-+
'''
# For Men
Men_categoryHeader = "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]"
Men_SelectProductBody = "//body/div[@id='page']/div[@id='content']/div[1]/div[2]/main[1]/div[1]/ul[1]/li[9]/div[1]/a[1]"
Men_ContainProductName = "//a[contains(text(),'Dark Blue Denim Jeans')]"

'''
+-+-+-+-+-+ +-+-+-+-+-+-+-+-+
|W|o|m|e|n| |C|a|t|a|g|o|r|y|
+-+-+-+-+-+ +-+-+-+-+-+-+-+-+
'''
# For Women
Women_categoryHeader = "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[4]/a[1]"
Women_SelectProductBody = "//body/div[@id='page']/div[@id='content']/div[1]/div[2]/main[1]/div[1]/ul[1]/li[6]/div[1]/a[1]"
Women_ContainProductName = "//a[contains(text(),'Blue Denim Shorts')]"

'''
+-+-+-+-+-+-+-+
|C|o|u|p|o|n|s|
+-+-+-+-+-+-+-+
'''
# For Coupons
Coupons_categoryHeader = "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]"
Coupons_SelectProductBody = "//body/div[@id='page']/div[@id='content']/div[1]/div[2]/main[1]/div[1]/ul[1]/li[1]/div[1]/a[1]/img[1]"
Coupons_ContainProductName = "//a[contains(text(),'Anchor Bracelet')]"
Coupons_InsertCode = "//input[@id='coupon_code']"
Apply_CouponCode = "//button[contains(text(),'Apply coupon')]"
Coupon_Error_Message_Xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]"
