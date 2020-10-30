import pyautogui as pg
from selenium import webdriver


import time
import pandas as pd
import numpy as np

class WhatsApp():
    def __init__(self, path):
        self.path = path
    
        self.driver = webdriver.Firefox(executable_path="/media/hamza/linux1/Coding/Python/whatsapp_bulk_msg_sender/geckodriver")
        self.driver.get("https://web.whatsapp.com/")

        input('Enter anything after scanning QR code')
        
        self.run()

    # Methods
    def run(self):
        self.loop_everyone()

    def loop_everyone(self):
        data = self.read_csv_file()
        for name, number, message, attachment in data:
            self.whatsapp_web_control(Name=name, Number=number, Message=message, Attachments=attachment)

    def read_csv_file(self):
        data = pd.read_csv(self.path)
        data_dict = data.to_dict('list')
        return zip(data_dict['names'], data_dict['LeadNumber'], data_dict['Message'], list(data_dict['attachment'])) # ((name,number, msg), (name,number, msg))
    
    def whatsapp_web_control(self, Name, Number, Message, Attachments):
        if str(Name) != "nan":    
            print("1")
            self.by_number(Number=Number, Message=Message, Attachments=Attachments)
        
        if str(Name) == "nan":
            print("2")
            self.by_name(Name=Name, Message=Message, Attachments=Attachments)
            

    def by_name(self, Name, Attachments, Message):
        time.sleep(1)
        searchName = self.driver.find_element_by_xpath('//div[@class = "{}"]'.format("_3FRCZ copyable-text selectable-text")) 
        searchName.click()
        searchName.send_keys(Name)
        time.sleep(1)

        user = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(Name))
        user.click()

        if str(Message)  != "nan":
            time.sleep(1)
            msgBox = self.driver.find_element_by_css_selector('#main ._3FRCZ')
            msgBox.click()
            msgBox.send_keys(str(Message))

            submit = self.driver.find_element_by_css_selector("._3uMse+ ._1JNuk")
            submit.click()

        if str(Attachments) != "nan":
            for attachment in Attachments.split(","):
                time.sleep(1)
                print(attachment)
                self.attach_file(file_path=attachment)
            

    def by_number(self, Number, Attachments, Message=""):
        if Message == "nan":  
            self.driver.get('https://web.whatsapp.com/send?phone=' + str(Number) +"&text="+" ")
        else:
            self.driver.get('https://web.whatsapp.com/send?phone=' + str(Number) +"&text="+ Message)
        
        time.sleep(4)
        submit = self.driver.find_element_by_css_selector("._3uMse+ ._1JNuk")
        submit.click()
        
        if str(Attachments) != "nan":
            for attachment in Attachments.split(","):
                time.sleep(1)
                print(attachment)
                self.attach_file(file_path=attachment)


    def attach_file(self, file_path):
        time.sleep(1)
        attachment_box = self.driver.find_element_by_xpath('//div[@title = "Attach"]')
        attachment_box.click()

        image_box = self.driver.find_element_by_xpath(
            '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        print(file_path)        
        image_box.send_keys(file_path)
        time.sleep(1)
        

        send_button = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
        send_button.click()


if __name__ == "__main__":
    WhatsApp("leads_final.csv")







