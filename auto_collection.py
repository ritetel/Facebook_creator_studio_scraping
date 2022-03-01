# cd C:\Program Files\Google\Chrome\Application - Triet PC
# cd C:\Program Files (x86)\Google\Chrome\Application - Company PC
# chrome.exe --remote-debugging-port=8989 --user-data-dir="C:\Triet\Chromeprofile\triet_mcv"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
import datetime as dt
import math

print("Starting date of Date range - dd/mm/yyyy: ")
start_date = dt.datetime.strptime(input(), '%d/%m/%Y')
print("Ending date of Date range - dd/mm/yyyy: ")
end_date = dt.datetime.strptime(input(), '%d/%m/%Y')

if ((start_date >= end_date) | ((end_date + dt.timedelta(days=2)) > dt.datetime.today()) | (end_date - dt.timedelta(days=95) >= start_date)):
    print("Re-type the date, the date is invalid")
else:
    opt = Options()
    opt.add_experimental_option("debuggerAddress", "localhost:8989")
    driver = webdriver.Chrome(executable_path = "C:\Triet\Chromeprofile\chromedriver.exe", chrome_options = opt)
    
    cs_per_url = "https://business.facebook.com/creatorstudio/insights_performance"
    driver.get(cs_per_url)
    sleep(2)
    
    # Xpath - page group/collections button
    xpath_insight_tab = '//*[@id="insights_left_nav_parent_tab"]'
    xpath_page_group = '//*[@id="mediaManagerPagesSelector"]'
    xpath_page_group_see_more = '/html/body/div[1]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div/div/div[1]/div[5]/a/div'
    
    # Xpath - Page group
    xpath_ex01 = '/html/body/div[1]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div/div/div[1]/div[18]'
    xpath_ex02 = '/html/body/div[1]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div/div/div[1]/div[19]'
    xpath_ex03 = '/html/body/div[1]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div/div/div[1]/div[20]'
    xpath_ex04 = '/html/body/div[1]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div/div/div[1]/div[21]'
    xpath_ex05 = '/html/body/div[1]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div/div/div[1]/div[22]'
    xpath_ex06 = '/html/body/div[1]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div/div/div[1]/div[23]'
    xpath_ex07 = '/html/body/div[1]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div/div/div[1]/div[24]'
    xpath_ex08 = '/html/body/div[1]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div/div/div[1]/div[25]'
    xpath_ex09 = '/html/body/div[1]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div/div/div[1]/div[26]'
    xpath_ex10 = '/html/body/div[1]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div/div/div[1]/div[27]'
    xpath_ex11 = '/html/body/div[1]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div/div/div[1]/div[28]'
    xpath_ex12 = '/html/body/div[1]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div/div/div[1]/div[29]'
    xpath_ex13 = '/html/body/div[1]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[3]/div[1]/div/div/div[1]/div[30]'
    
    page_groups = [xpath_ex01, xpath_ex02, xpath_ex03, xpath_ex04, xpath_ex05, xpath_ex06, xpath_ex07, xpath_ex08, xpath_ex09, xpath_ex10, xpath_ex11, xpath_ex12, xpath_ex13]
    
    # Xpath timeline
    xpath_timeline_button = '/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div[1]'
    xpath_backward_button = '/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[1]'
    xpath_forward_button = '/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[2]'
    xpath_update_button = '/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div[2]/div/div[3]/span[2]/div'
    
    creator_studio_today = dt.datetime.today() - dt.timedelta(days=1)
    start_date_day = float(start_date.strftime("%d"))
    start_date_month = float(start_date.strftime("%m"))
    start_date_year = float(start_date.strftime("%Y"))
    end_date_day = float(end_date.strftime("%d"))
    end_date_month = float(end_date.strftime("%m"))
    end_date_year = float(end_date.strftime("%Y"))
    now_month = float(creator_studio_today.month)
    now_year = float(creator_studio_today.year)
    
    start_month_change = now_month - start_date_month + 12 * (now_year - start_date_year)
    end_month_change = end_date_month - start_date_month + 12 * (end_date_year - start_date_year)
    
    print(start_month_change)
    print(end_month_change)
    
    num_first_row_start_date =  7 - (dt.date(int(start_date_year), int(start_date_month), 1).isoweekday() % 7)
    num_first_row_end_date = 7 - (dt.date(int(end_date_year), int(end_date_month), 1).isoweekday() % 7)
    start_date_row = math.ceil((start_date_day - num_first_row_start_date)/7) + 1
    end_date_row = math.ceil((end_date_day - num_first_row_end_date)/7) + 1
    
    if (start_date_day > num_first_row_start_date):
        start_date_col = start_date.isoweekday() % 7 + 1
    else:
        start_date_col = start_date_day
    
    if (end_date_day > num_first_row_end_date):
        end_date_col = end_date.isoweekday() % 7 + 1
    else:
        end_date_col = end_date_day
    
    # Xpath - Data export board
    xpath_export_data = '//*[@id="mediaManagerExportInsightsButton"]/div[1]/div[1]'
    
        # data option
    
    xpath_opt_start = '/html/body/div['
    xpath_opt_mid1 = ']/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div/div[3]/div/div/div[2]/div['
    xpath_opt_mid2 = ']/div/div[2]/div/div/div/label['
    xpath_opt_end = ']/div/div/div[1]/div/div/div[1]/input'
    
    opt_lifetime = '1'
    opt_daily = '2'
    opt_video = '1'
    opt_post = '2'
    opt_page = '3'
    opt_creationdate = '1'
    opt_activity = '2'
    
        # data preset
    xpath_preset_button_end = ']/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]'
    xpath_preset_audience_end = ']/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div[6]/div/div/div[1]/div/div[1]'
    xpath_preset_earning_end = ']/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div[8]/div/div/div[1]/div/div[1]'
    
        # generate - finish selection process
    generate_but_end = ']/div[1]/div[1]/div/div/div/div/div[3]/div/div[2]/div'
    
    # Waiting until the page finish loading process
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath_insight_tab)))
    sleep(2)
    
    # choose timeline
    driver.find_element_by_xpath(xpath_timeline_button).click()
    sleep(1)
    
    xpath_start_date = '/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div/div/div[' + str(start_date_row) + ']/div[' + str(start_date_col) + ']'
    
    xpath_end_date = '/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div/div/div[' + str(end_date_row) + ']/div[' + str(end_date_col) + ']'
    
        # choose start date
    for i in range(int(start_month_change)):
        driver.find_element_by_xpath(xpath_backward_button).click()
        sleep(1)
    sleep(1)
    driver.find_element_by_xpath(xpath_start_date).click()
    sleep(1)
        
        # choose end date
    if (start_date != end_date):
        for i in range(int(end_month_change)):
            driver.find_element_by_xpath(xpath_forward_button).click()
            sleep(1)
        sleep(0.5)
        driver.find_element_by_xpath(xpath_end_date).click()
        sleep(0.5)
    
    driver.find_element_by_xpath(xpath_update_button).click()
    sleep(0.5)
        
    # download reports
    for page_group in page_groups:
        if (page_groups.index(page_group) == 0):
            i = str(page_groups.index(page_group) + 4)
        else:
            i = '5'
        
        xpath_opt_dataview = xpath_opt_start + i + xpath_opt_mid1 + "1" + xpath_opt_mid2 + opt_daily + xpath_opt_end
        xpath_opt_contentlevel = xpath_opt_start + i + xpath_opt_mid1 + "2" + xpath_opt_mid2 + opt_video + xpath_opt_end
        xpath_opt_filter = xpath_opt_start + i + xpath_opt_mid1 + "3" + xpath_opt_mid2 + opt_activity + xpath_opt_end
        xpath_generate_button = xpath_opt_start + i + generate_but_end
        xpath_preset_button = xpath_opt_start + i + xpath_preset_button_end
        xpath_preset_ex_daily = xpath_opt_start + i + xpath_preset_earning_end
        
        driver.find_element_by_xpath(xpath_page_group).click()
        
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath_page_group_see_more)))
        sleep(0.5)
        
        driver.find_element_by_xpath(xpath_page_group_see_more).click()
        sleep(0.5)
        
        driver.find_element_by_xpath(page_group).click()
        sleep(0.5)
        
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath_insight_tab)))
        sleep(3)
        
        driver.find_element_by_xpath(xpath_export_data).click()
        sleep(2)
        
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath_opt_dataview)))
        sleep(1.5)
        
        driver.find_element_by_xpath(xpath_opt_dataview).click()
        sleep(0.7)
        
        driver.find_element_by_xpath(xpath_opt_contentlevel).click()
        sleep(0.5)
        
        driver.find_element_by_xpath(xpath_opt_filter).click()
        sleep(1)
        
        driver.find_element_by_xpath(xpath_preset_button).click()
        sleep(0.5)
        
        driver.find_element_by_xpath(xpath_preset_ex_daily).click()
        sleep(1)
        
        driver.find_element_by_xpath(xpath_preset_button).click()
        sleep(0.5)
        
        driver.find_element_by_xpath(xpath_generate_button).click()
        sleep(4)
    
    driver.get(cs_per_url)
    sleep(2)
    
    # Waiting until the page finish loading process
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath_insight_tab)))
    sleep(2)
    
    #New start time
    start_date = start_date - dt.timedelta(days=30)
    start_date_day = float(start_date.strftime("%d"))
    start_date_month = float(start_date.strftime("%m"))
    start_date_year = float(start_date.strftime("%Y"))
    
    start_month_change = now_month - start_date_month + 12 * (now_year - start_date_year)
    end_month_change = end_date_month - start_date_month + 12 * (end_date_year - start_date_year)
    
    num_first_row_start_date =  7 - (dt.date(int(start_date_year), int(start_date_month), 1).isoweekday() % 7)
    num_first_row_end_date = 7 - (dt.date(int(end_date_year), int(end_date_month), 1).isoweekday() % 7)
    start_date_row = math.ceil((start_date_day - num_first_row_start_date)/7) + 1
    
    if (start_date_day > num_first_row_start_date):
        start_date_col = start_date.isoweekday() % 7 + 1
    else:
        start_date_col = start_date_day
    
    # choose timeline
    driver.find_element_by_xpath(xpath_timeline_button).click()
    sleep(1)
    xpath_start_date = '/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div/div/div[' + str(start_date_row) + ']/div[' + str(start_date_col) + ']'
    
        # choose start date
    for i in range(int(start_month_change)):
        driver.find_element_by_xpath(xpath_backward_button).click()
        sleep(0.5)           
    sleep(1)
    driver.find_element_by_xpath(xpath_start_date).click()
    sleep(1)
        
        # choose end date
    if (start_date != end_date):        
        for i in range(int(end_month_change)):
            driver.find_element_by_xpath(xpath_forward_button).click()
            sleep(0.5)
        sleep(1)
        driver.find_element_by_xpath(xpath_end_date).click()
        sleep(1)
    
    driver.find_element_by_xpath(xpath_update_button).click()
    sleep(1)
    
    for page_group in page_groups:
        
        if (page_groups.index(page_group) == 0):
            i = str(page_groups.index(page_group) + 4)
        else:
            i = '5'
        
        xpath_opt_dataview = xpath_opt_start + i + xpath_opt_mid1 + "1" + xpath_opt_mid2 + opt_lifetime + xpath_opt_end
        xpath_opt_contentlevel = xpath_opt_start + i + xpath_opt_mid1 + "2" + xpath_opt_mid2 + opt_post + xpath_opt_end
        xpath_opt_filter = xpath_opt_start + i + xpath_opt_mid1 + "3" + xpath_opt_mid2 + opt_creationdate + xpath_opt_end
        xpath_generate_button = xpath_opt_start + i + generate_but_end
        
        driver.find_element_by_xpath(xpath_page_group).click()
        
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath_page_group_see_more)))
        sleep(0.5)
        
        driver.find_element_by_xpath(xpath_page_group_see_more).click()
        sleep(0.5)
        
        driver.find_element_by_xpath(page_group).click()
        sleep(0.5)
        
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath_insight_tab)))
        sleep(2)
        
        driver.find_element_by_xpath(xpath_export_data).click()
        sleep(2)
        
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath_opt_dataview)))
        sleep(1)
        
        driver.find_element_by_xpath(xpath_opt_dataview).click()
        sleep(0.7)    
        
        driver.find_element_by_xpath(xpath_opt_contentlevel).click()
        sleep(0.5)
        
        driver.find_element_by_xpath(xpath_opt_filter).click()
        sleep(0.5)
        
        driver.find_element_by_xpath(xpath_generate_button).click()
        sleep(4)
    
    
    
    
    
    
    
    
    
    
    
    
