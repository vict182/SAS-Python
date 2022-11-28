from behave import given, when, then
from ConfiguracionBD.ConexionBD import ConexionBD
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from IPython.display import display
from hamcrest import assert_that, equal_to, is_not
from selenium.webdriver.chrome.options import Options

@given(u'La linea "{linea}" se encuentre existente en la tabla sas_dm.ar_abt_campaign')
def step_impl(context, linea):
    conex = ConexionBD(user='EXB35249', password='Matias12', port='1521',
                       dsn='sascmt04.claro.amx/TSASCM')

    registro = conex.ejecutarSelect("""SELECT cellular_number,anio_mes,service_status
                                     FROM sas_dm.ar_abt_campaign
                                     where cellular_number in ('""" + linea + """')""")

    display(registro[0])

    assert_that(len(registro), equal_to(1),
                reason="No se encontraron registros en la tabla sas_dm.ar_abt_campaign")



@given(u'se encuentre existente en la tabla AR_aux.OFFERS_MATRIX')
def step_impl(context):
        conex = ConexionBD(user='EXB35249', password='Matias12', port='1521',
                           dsn='sascmt04.claro.amx/TSASCM')

        registro = conex.ejecutarSelect("""select campaign, country, offer_code, treatment, start_date, end_date
                                             from AR_aux.OFFERS_MATRIX 
                                             where offer_code in ('cluster_cr_li_sp')""")

        display(registro[0])

        assert_that(len(registro), equal_to(1),
                    reason="No se encontraron registros en la tabla AR_aux.OFFERS_MATRIX")


@when(u'Se ejecute la campaña SATPUSH_Prueba_Lote_spv05_Automation')
def step_impl(context):
    chrome_profile = Options()
    chrome_profile.add_argument("--headless")
    browser = webdriver.Chrome('C:\\Users\\usuario\\Desktop\\TESTING AUTOMATI JAVA/chromedriver.exe', chrome_options=chrome_profile)
    browser.maximize_window()
    browser.get("http://sascmt03.claro.amx:7980/SASLogon/login?service=http%3A%2F%2Fsascmt03.claro.amx%3A7980%2FSASCIStudio%2Fj_spring_cas_security_check")
    time.sleep(1)

    clicksasusuario = browser.find_element(By.ID, 'username')
    clicksasusuario.send_keys("EXA30481@saspw")
    time.sleep(1)
    clicksascontraseña = browser.find_element(By.ID, 'password')
    clicksascontraseña.send_keys("EXA30481")
    time.sleep(1)

    clickingresar = browser.find_element(
        By.XPATH, '//*[@id=\"credentials\"]/button')
    clickingresar.click()
    time.sleep(15)

    frame = browser.find_element(By.XPATH, '//*[@id=\"sasci_iframe\"]')
    browser.switch_to.frame(frame)
    time.sleep(6)

    buscardorcampaña = browser.find_element(By.ID, '__page0-searchField-I')
    buscardorcampaña.click()
    buscardorcampaña.send_keys("SATPUSH_Prueba_Lote_spv05_Automation")
    clickfidelizacion = browser.find_element(By.XPATH, '//*[@id=\"__table1-rows-row0-col0\"]/div/span')
    clickfidelizacion.click()

    clickdiseñador = browser.find_element(By.XPATH, '//*[@id=\"__icon75\"]')
    clickdiseñador.click()
    clickcvpp = browser.find_element(By.XPATH, '//*[@id=\"__icon76\"]')
    clickcvpp.click()

    clickcvppincentivov07 = browser.find_element(By.XPATH, '//*[@id=\"__link2-col0-row3\"]')
    clickcvppincentivov07.click()
    time.sleep(15)
    ejecutarcampaña = browser.find_element(By.ID, '__button217')
    ejecutarcampaña.click()
    time.sleep(2)
    ejecutarcampañaSI = browser.find_element(By.XPATH, '//*[@id="__dialog0-customButton0"]')
    ejecutarcampañaSI.click()
    time.sleep(15)
    cerrarmensajecampaña = browser.find_element(By.ID, '__dialog1-closeButton')
    cerrarmensajecampaña.click()
    time.sleep(5)
    cerrarcampaña = browser.find_element(By.ID, '__page5-closeButton')
    cerrarcampaña.click()
    time.sleep(2)


@then(u'Se envía un mensaje del tipo Sat push y se inserta un registro en la tabla AR_AUX.EXECUTED_HISTORICO_DYNAMO')
def step_impl(context):
    conex = ConexionBD(user='EXB35249', password='Matias12', port='1521',
                       dsn='sascmt04.claro.amx/TSASCM')

    registro = conex.ejecutarSelect("""select * 
                                    from (select * from AR_AUX.EXECUTED_HISTORICO_DYNAMO   
                                    where campania ='SATPUSH_Prueba_Lote_spv05_Automation' 
                                    order by fecha_ejecucion desc) 
                                    where rownum=1""")

    display(registro[0])

    assert_that(len(registro), equal_to(1),
                reason="No se encontraron registros en la tabla AR_AUX.EXECUTED_HISTORICO_DYNAMO")
