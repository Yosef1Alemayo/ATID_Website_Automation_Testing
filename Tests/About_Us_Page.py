from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# This Is The Pre Condition:
def init():
    path = 'C://Users//yossi//Desktop//Python-Project//ATID_Website_Automation_Testing//Driver//chromedriver.exe'
    driver = webdriver.Chrome(path)
    url = 'https://atid.store/'
    driver.get(url)
    driver.maximize_window()
    sleep(5)
    about_page = driver.find_element(By.CSS_SELECTOR, "#menu-item-828")
    about_page.click()
    sleep(3)
    return driver

# All The Functionality Tests:
def test_links_at_the_top():
    driver = init()
    home_page = driver.find_element(By.CSS_SELECTOR, "#menu-item-381")
    home_page.click()
    sleep(3)

    about_page = driver.find_element(By.CSS_SELECTOR, "#menu-item-828")
    about_page.click()
    sleep(3)

    store_page = driver.find_element(By.CSS_SELECTOR, "#menu-item-45")
    store_page.click()
    sleep(3)

    about_page = driver.find_element(By.CSS_SELECTOR, "#menu-item-828")
    about_page.click()
    sleep(3)

    men_page = driver.find_element(By.CSS_SELECTOR, "#menu-item-266")
    men_page.click()
    sleep(3)

    about_page = driver.find_element(By.CSS_SELECTOR, "#menu-item-828")
    about_page.click()
    sleep(3)

    women_page = driver.find_element(By.CSS_SELECTOR, "#menu-item-267")
    women_page.click()
    sleep(3)

    about_page = driver.find_element(By.CSS_SELECTOR, "#menu-item-828")
    about_page.click()
    sleep(3)

    accessories_page = driver.find_element(By.CSS_SELECTOR, "#menu-item-671")
    accessories_page.click()
    sleep(3)

    about_page = driver.find_element(By.CSS_SELECTOR, "#menu-item-828")
    about_page.click()
    sleep(3)

    contact_us_page = driver.find_element(By.CSS_SELECTOR, "#menu-item-829")
    contact_us_page.click()
    sleep(3)

    about_page = driver.find_element(By.CSS_SELECTOR, "#menu-item-828")
    about_page.click()
    sleep(3)

    driver.quit()

def test_photo_link():
    driver = init()
    photo_link = driver.find_element(By.XPATH, "//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]"
                                               "/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/a[1]")
    photo_link.click()
    sleep(3)
    driver.quit()

def test_cart_link():
    driver = init()
    cart_link = driver.find_element(By.XPATH, "//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]"
                                              "/div[1]/div[3]/div[3]/div[1]/div[1]/a[1]")
    cart_link.click()
    sleep(3)
    driver.quit()

def test_search_field():
    driver = init()
    search_button = driver.find_element(By.XPATH, "//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]"
                                                  "/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/a[1]")
    search_button.click()
    sleep(3)

    search_field = driver.find_element(By.TAG_NAME, "input")
    search_field.send_keys('Black Hoodie')
    sleep(3)

    search_button.click()
    sleep(3)
    driver.quit()

def test_accessibility():
    driver = init()
    access_button = driver.find_element(By.XPATH, "//body[1]/nav[1]/div[1]/a[1]")
    access_button.click()
    sleep(5)

    increase_text = driver.find_element(By.XPATH, "//span[contains(text(),'Increase Text')]")
    increase_text.click()
    sleep(3)

    reset_button = driver.find_element(By.XPATH, "//span[contains(text(),'Reset')]")
    reset_button.click()
    sleep(3)

    decrease_text = driver.find_element(By.XPATH, "//span[contains(text(),'Decrease Text')]")
    decrease_text.click()
    sleep(3)

    reset_button.click()
    sleep(3)

    grayscale = driver.find_element(By.XPATH, "//span[contains(text(),'Grayscale')]")
    grayscale.click()
    sleep(3)

    reset_button.click()
    sleep(3)

    high_contrast = driver.find_element(By.XPATH, "//span[contains(text(),'High Contrast')]")
    high_contrast.click()
    sleep(3)

    reset_button.click()
    sleep(3)

    navigate_contrast = driver.find_element(By.XPATH, "//span[contains(text(),'Negative Contrast')]")
    navigate_contrast.click()
    sleep(3)

    reset_button.click()
    sleep(3)

    light_background = driver.find_element(By.XPATH, "//span[contains(text(),'Light Background')]")
    light_background.click()
    sleep(3)

    reset_button.click()
    sleep(3)

    links_underline = driver.find_element(By.XPATH, "//span[contains(text(),'Links Underline')]")
    links_underline.click()
    sleep(3)

    reset_button.click()
    sleep(3)

    readable_font = driver.find_element(By.XPATH, "//span[contains(text(),'Readable Font')]")
    readable_font.click()
    sleep(3)

    reset_button.click()
    sleep(3)

    driver.quit()

def test_facebook_link():
    driver = init()
    facebook_link = driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]"
                                                  "/div[1]/div[1]/section[4]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]"
                                                  "/span[1]/a[1]/i[1]")
    facebook_link.click()
    sleep(3)
    driver.quit()

def test_twitter_link():
    driver = init()
    twitter_link = driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]"
                                                 "/div[1]/div""[1]/section[4]/div[2]/div[1]/div[1]/div[3]"
                                                 "/div[1]/div[1]/span[2]/a[1]/i[1]")
    twitter_link.click()
    sleep(3)
    driver.quit()

def test_instagram_link():
    driver = init()
    instagram_link = driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]"
                                                   "/div[1]/div[1]/div[1]/section[4]/div[2]/div[1]/div[1]/div[3]"
                                                   "/div[1]/div[1]/span[3]/a[1]/i[1]")
    instagram_link.click()
    sleep(3)
    driver.quit()

def test_google_link():
    driver = init()
    google_link = driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]"
                                                "/div[1]/div[1]/div[1]/section[4]/div[2]/div[1]/div[1]/div[3]"
                                                "/div[1]/div[1]/span[4]/a[1]/i[1]")
    google_link.click()
    sleep(3)
    driver.quit()

# This Is In Progress:
def test_links_at_the_bottom_page():
    driver = init()
    home_link = driver.find_element(By.CSS_SELECTOR, "#menu-item-423")
    home_link.click()
    sleep(3)

    about_page = driver.find_element(By.CSS_SELECTOR, "#menu-item-387")
    about_page.click()
    sleep(3)


# All The UI Testing:
def test_ui():
    driver = init()
    # ----------------------------------------
    top_ruler = driver.find_element(By.XPATH, "//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]"
                                              "").get_attribute('innerText')
    assert top_ruler == "HOME\nSTORE\nMEN\nWOMEN\nACCESSORIES\nABOUT\nCONTACT US\nSearch\n0.00 ₪ 0"
    # --------------------------------------
    page_title = driver.find_element(By.TAG_NAME, "h1").get_attribute('innerText')
    assert page_title == 'About Us'
    # --------------------------------------
    who_we_are = driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]"
                                               "/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/section[1]"
                                               "/div[1]/div[1]/div[1]").get_attribute('innerText')

    assert who_we_are == "Who We Are\n\nATID Demo Store was created by ATID College dedicated employees. " \
                         "This is a complete demo site for practicing QA & Test Automation methodologies. " \
                         "Don't think for a second you can actually buy here something cause you can't !" \
                         " This Demo Store contains software bugs which were put intentionally and your job " \
                         "is to locate them Good luck falks, Yoni Flenner - ATID College"
    # ---------------------------------------
    our_team = driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]"
                                             "/div[1]/div[1]/div[1]/section[3]/div[1]"
                                             "/div[1]/div[1]").get_attribute('innerText')

    assert our_team == "A Few Words About\nOur Team\n\nWe have the best team ever everybody who is somebody wants" \
                       " to work with us, so we can afford cherry-picking them, one by one...\n\nYoni Flenner" \
                       "\n\nFounder - CEO\n\nAlbert Einstein\n\nCOO\n\nSteve Jobs\n\nMarketing Head\n\nBill Gates" \
                       "\n\nLead Developer\n\nKim Kardashian\n\nIntern Designer\n\nMadonna\n\nHead of Fun"
    # ---------------------------------------
    follow_us_title = driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]"
                                                    "/article[1]/div[1]/div[1]/div[1]/section[4]/div[2]"
                                                    "/div[1]/div[1]/div[2]/div[1]/h2[1]").get_attribute('innerText')
    assert follow_us_title == "Follow Us"
    # ---------------------------------------
    bottom_text = driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]""/article[1]/div[1]"
                                                "/div[1]/div[1]/section[5]").get_attribute('innerText')

    assert bottom_text == "Worldwide Shipping\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar" \
                          " dapibus leo.\n\nBest Quality\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar" \
                          " dapibus leo.\n\nBest Offers\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar " \
                          "dapibus leo.\n\nSecure Payments\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar" \
                          " dapibus leo."
    # ---------------------------------------
    links_text = driver.find_element(By.XPATH, "//body[1]/div[1]/footer[1]/div[1]").get_attribute('innerText')
    assert links_text == "Quick Links\nHome\nAbout\nCart\nContact Us\nFor Her\nWomen Jeans\nTops and Shirts\nWomen " \
                         "Jackets\nHeels and Flats\nWomen Accessories\nFor Him\nMen Jeans\nMen Shirts\nMen" \
                         " Shoes\nMen Accessories\nMen Jackets"
    # --------------------------------------
    copyright_text = driver.find_element(By.XPATH, "//body[1]/div[1]/footer[1]"
                                                   "/div[2]").get_attribute('innerText')
    assert copyright_text == "Copyright © 2022 ATID Demo Store\n\nPowered by ATID College"

    driver.quit()