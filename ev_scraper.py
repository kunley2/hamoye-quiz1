from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
from selenium.webdriver.chrome.options import Options

car_name = []
car_model = []
car_battery = []
car_seats = []
car_acceleration = []
car_speed = []
car_distance = []
car_eff = []
car_charge = []
price_g = []
price_n = []
price_p = []


option = Options()
option.headless = True
browser = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://ev-database.org/'
browser.get(url)
time.sleep(10)
browser.find_element_by_xpath('//div[@id="paging"]').click()
browser.find_element_by_xpath('//*[@id="paging"]/ul/li[4]').click()
time.sleep(20)
car_list = browser.find_elements_by_xpath('//div[@class="data-wrapper"]')
for names in car_list:
    name = names.find_element_by_xpath('.//a[@class="title"]/span').text
    car_name.append(name)
    model = names.find_element_by_xpath('.//a[@class="title"]/span[2]').text
    car_model.append(model)
    battery = names.find_element_by_xpath('.//div[@class="subtitle"]/span').text.split(' ')[0]
    car_battery.append(battery)
    seats = names.find_element_by_xpath('.//div[@class="icons"]/span[6]').text
    car_seats.append(seats)
    acceleration = names.find_element_by_xpath('.//div[@class="specs"]/p/span[2]').text.split(' ')[0]
    car_acceleration.append(acceleration)
    speed = names.find_element_by_xpath('.//div[@class="specs"]/p[2]/span[2]').text.split(' ')[0]
    car_speed.append(speed)
    distance = names.find_element_by_xpath('.//div[@class="specs"]/p[3]/span[2]').text.split(' ')[0]
    car_distance.append(distance)
    efficiency = names.find_element_by_xpath('.//div[@class="specs"]/p[4]/span[2]').text.split(' ')[0]
    car_eff.append(efficiency)
    fast_charge = names.find_element_by_xpath('.//div[@class="specs"]/p[5]/span[2]').text.split(' ')[0]
    car_charge.append(fast_charge)
    price_gbp = names.find_element_by_xpath('.//div[@class="pricing align-right"]/span[3]').text[1:]
    price_p.append(price_gbp)
    price_germany = names.find_element_by_xpath('.//div[@class="pricing align-right"]/span[1]').text[1:]
    price_g.append(price_germany)
    price_netherland = names.find_element_by_xpath('.//div[@class="pricing align-right"]/span[2]').text[1:]
    price_n.append(price_netherland)

# saving the data into a dictionary and then turning it into a csv file
car_data = {'vehicle_name':car_name,'model':car_model,'battery':car_battery,'seats':car_seats,
            'acceleration':car_acceleration,'top_speed':car_speed,'distance':car_distance,'efficiency':car_eff,
            'fast_charge':car_charge,'price_pounds':price_p,'price_germany':price_g,'price_netherland':price_n}
# print(car_data)
car_df = pd.DataFrame().from_dict(car_data)
print(car_df)
car_df.to_csv('electric_vehicle.csv')