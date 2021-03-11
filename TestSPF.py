import time

def test_sign_in(selenium):

    selenium.get('https://petfriends1.herokuapp.com/')

    time.sleep(3)

    btn_new_user = selenium.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")
    btn_new_user.click()

    btn_exist = selenium.find_element_by_link_text(u'У меня уже есть аккаунт')
    btn_exist.click()

    field_email = selenium.find_element_by_id('email')
    field_email.clear()
    field_email.send_keys('test_test@mail.ru')

    field_pass = selenium.find_element_by_id('pass')
    field_pass.clear()
    field_pass.send_keys('12345qwerty')

    btn_submit = selenium.find_element_by_xpath("//button[@type='submit']")
    btn_submit.click()

   
    time.sleep(3)

    btn_my_pets = selenium.find_element_by_link_text(u'Мои питомцы')
    btn_my_pets.click()

    time.sleep(3)

    btn_add_pets = selenium.find_element_by_css_selector('body > div.task2.fill > div > div.\\.col-sm-8.right.fill > div > button')
    btn_add_pets.click()

    time.sleep(3)

    field_name = selenium.find_element_by_id('name')
    field_name.clear()
    field_name.send_keys('Тестовый Бобик')

    time.sleep(3)

    field_animal_type = selenium.find_element_by_id('animal_type')
    field_animal_type.clear()
    field_animal_type.send_keys('Супер-дворняга')

    time.sleep(3)

    field_age = selenium.find_element_by_id('age')
    field_age.clear()
    field_age.send_keys('100500')

    btn_add = selenium.find_element_by_css_selector('#addPetsModal > div > div > div.modal-footer > button.btn.btn-success')
    btn_add.click()

    time.sleep(3)

    selenium.save_screenshot('result.png')



