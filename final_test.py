from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time


class Search(unittest.TestCase):
    # Использую много time.sleep на случай плохого интернета
    def setUp(self):
        self.drv = webdriver.Chrome()
        self.drv.get('http://google.com/ncr')
        time.sleep(2)

    def test_search(self):
        assert 'Google' in self.drv.title
        elm = self.drv.find_element(By.NAME, 'q')
        elm.send_keys('selenide')
        elm.send_keys(Keys.RETURN)
        time.sleep(2)
        # Несмотря на то, что элементов с таким классом много, можно провести поиск по нему, ибо по заданию необходим первый результат
        elm = self.drv.find_element(By.CLASS_NAME, 'byrV5b')
        assert elm.text == 'https://selenide.org'
        print(f'{time.ctime()}: Элемент найден')
        final_check = elm.text
        elm = self.drv.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
        elm.click()
        time.sleep(2)
        elm = self.drv.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[2]/div[1]/div')
        assert 'selenide.org' in elm.text
        print(f'{time.ctime()}: Изображение подходит')

        elm = self.drv.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]')
        elm.click()
        # В моем случае следующий assert выдает ошибку поскольку первая ссылка отличается от второй (selenide.org против ru.selenide.org)
        assert self.drv.find_element(By.CLASS_NAME, 'byrV5b').text == final_check, "Different links"
        print(f'{time.ctime()}: Первая ссылка такая же как при первом поиске')

    def tearDown(self):
        self.drv.close()


if __name__ == '__main__':
    unittest.main()
