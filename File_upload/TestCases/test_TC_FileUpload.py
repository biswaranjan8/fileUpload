from Base.initiate_driver import startBrowser
from Page import set_fileUpload
import time

def test_app_uploadFile():
    driver = startBrowser()
    set_fle = set_fileUpload.setFile(driver)
    driver.get("http://testautomationpractice.blogspot.com/")

    driver.switch_to_frame(0)
    set_fle.fileUpload("C://Users/Admin/Desktop/data_driven_test/test.py")
    driver.switch_to_default_content()
    time.sleep(2)


