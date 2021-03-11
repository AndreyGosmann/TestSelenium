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

    time.sleep(7)

    if selenium.current_url == 'https://petfriends1.herokuapp.com/all_pets':
        selenium.save_screenshot('result_TestSPF.png')
    else:
        raise Exception('Login Error')


