from selenium import webdriver
from time import sleep
from data import user
from data import password



class GramBot:

    def __init__(self, username, password):
        if (username == ''):
            print("Enter your Instagram username: ")
            username = str(input())
        if (password == ''):
            print("Enter your password: ")
            password = str(input())
        self.driver = webdriver.Chrome(
            executable_path="C:\\Users\\14085\\Downloads\\chromedriver_win32\\chromedriver.exe")
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(3)
        self.driver.find_element_by_xpath("//input[(@name=\"username\")]").send_keys(username)
        self.driver.find_element_by_xpath("//input[(@name=\"password\")]").send_keys(password)
        self.driver.find_element_by_xpath("//button[(@type='submit')]").click()
        sleep(4)
        try:
            #"not now" for login info
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        except:
            sleep(2)
        try:
            #"not now" for notifications
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        except:
            sleep(2)
        sleep(2)

    def get_unfollwers(self):
        #click on my profile icon
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span").click()
        sleep(1)
        #click "profile" option in dropdown
        self.driver.find_element_by_xpath("//div[contains(text(), 'Profile')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href, 'following')]").click()
        followingNames = self._get_profiles()
        self.driver.find_element_by_xpath("//a[contains(@href, 'followers')]").click()
        followerNames = self._get_profiles()

        unfollowers = [profile for profile in followingNames if profile not in followerNames]
        print(unfollowers)
#revise
    def _get_profiles(self):
        try:
            suggestions = self.driver.find_element_by_xpath("//h4[contains(text(), 'Suggestions')]").click()
            self.driver.execute_script('arguments[0].scrollIntoView()', suggestions)
        except:
            sleep(1)
        sleep(2)
        height = 0
        prevHeight = 1
        scrollBox = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        while prevHeight != height:
            prevHeight = height
            sleep(0.5)
            height = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scrollBox)
        profileLinks = scrollBox.find_elements_by_tag_name('a')
        profileNames = [profileName.text for profileName in profileLinks if profileName.text != '']
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()
        return profileNames

gram_bot = GramBot(user, password)
gram_bot.get_unfollwers()