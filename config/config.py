import os

DRIVER_PATH = "d:\\selenium\\chromedriver.exe"
TEST_CASE = os.path.join( os.path.dirname(__file__),"../test_case")

GY_UI_URL = 'http://qa.yansl.com/#/home'

GY_DB_MALL = {
    'host': 'qa.guoyasoft.com',             
    'port': 3306,                           
    'db': 'guoya_virtual_mall_1811',        
    'user': 'root',                         
    'passwd': 'Guoya006',                   
    'charset': 'utf8'                       
}											
