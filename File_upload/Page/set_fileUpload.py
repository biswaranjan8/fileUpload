
class setFile:
    file_ele_by_name = "RESULT_FileUpload-10"
    def __init__(self,driver):
        self.driver = driver

    def fileUpload(self,files):

        self.driver.find_element_by_id(self.file_ele_by_name).send_keys(files)
