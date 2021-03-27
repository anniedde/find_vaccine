import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib, ssl

sender_email = "python.notify.35@gmail.com"
receiver_email = "anniedde@gmail.com"

port = 465  # For SSL
password = "Sefvik-zukco0-pedzoc"

driver = webdriver.Chrome('/Users/annie/Downloads/chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://www.walgreens.com/findcare/vaccination/covid-19?ban=covid_scheduler_brandstory_main_March2021');
#time.sleep(5) # Let the user actually see something!
button = driver.find_element_by_class_name('btn')
button.click()
time.sleep(5)
search_box = driver.find_element_by_id('inputLocation')
list = [27519,27523,27560,27513,27713,27623,27511,27709,27502,27518,27517,27617,27695,27607,27539,27676,27707,27612,27703,27606,27515,27599,27613,27702,27710,27711,27715,27717,27722,27701,27706,27562,27605,27510,27608,27708,27611,27514,27602,27619,27620,27621,27622,27624,27625,27626,27627,27628,27629,27634,27635,27636,27640,27650,27656,27658,27668,27675,27690,27697,27698,27699,27601,27609,27540,27228,27603,27615,27704,27705,27559,27516,27614,27604,27661,27312,27526,27712,27616,27610,27278,27529,27592,27587,27509,27545,27522,27503,27588,27243,27571,27501,27528,27340,27237,27520,27253,27330,27552,27591,27596,27505,27256,27581,27331,27543,27506,27258,27349,27521,27572,27359,27527,27231,27302,27525,27252,27597,27207,27344,27213,27546,27541,27583,27593,28368,27332,28323,28339,27504,28355,27544,27216,27508,27201,27314,27215,27577,27557,28335,27298,27355,27576,27217,27565,27524,27208,28326,28356,28390,27573,27568,28334,27574,27549,27555,27316,27259,27291,27283,27244,27202,27542,27377,27880,27536,27882,28311,28327,27807,28342,27325,28308,28394,27342,27233,27248,27249,28307,28350,28344,27379,27582,27537,27230,27569,28395,27343,27301,28366,27816,27851,27313,27212,27341]
list.reverse()
for zip_code in list:
    search_box.clear()
    search_box.send_keys(zip_code)
    time.sleep(2)
    button = driver.find_element_by_class_name('btn')
    button.click()
    time.sleep(2)
    blahblah = driver.find_element_by_id('wag-body-main-container')
    blahblah = blahblah.find_element_by_class_name('common-container')
    blahblah = blahblah.find_element_by_class_name('ApptScreens')
    blahblah = blahblah.find_element_by_class_name('mt40')
    blahblah = blahblah.find_element_by_class_name('alert')
    blahblah = blahblah.find_element_by_class_name('fs16')
    text=blahblah.text
    if "unavailable" not in text:
        context = ssl.create_default_context()
        message = """\
            Subject: {} available

            This message is sent from Python.""".format(zip_code)
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    time.sleep(5)
time.sleep(5) # Let the user actually see something!
driver.quit()
