from playwright.sync_api import sync_playwright
import time
import random
import string




def run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        def log_response(response):
            print(f"Получен ответ: {response.url} со статусом {response.status}")



        page.on("response", log_response)


        page.goto('https://lk.pzzl.ru/')


        page.click('text=Пароль')


        page.fill('input[name="phone"]', '1000443646')


        page.fill('input[name="password"]', 'HAg21N18')


        page.click('#main_wrapper > div > div.MuiContainer-root.MuiContainer-maxWidthLg.css-1wcm3j0 > div.css-gl0gw > div.css-1u0lwz0 > div > div.css-mgmyaz > div')


        page.wait_for_selector('#main_wrapper > div > div.MuiContainer-root.MuiContainer-maxWidthLg.css-cssmpu > div.css-1f61iq5 > div.css-1am664v > div.css-4xcpzv > p')

        page.click('#main_wrapper > div > div.MuiContainer-root.MuiContainer-maxWidthLg.css-cssmpu > div.css-1f61iq5 > div.css-r9uudj > div.css-gfkw9b > div.css-lhqml6 > div.css-53fig7')
        time.sleep(1)

        page.click('#main_wrapper > div > div.MuiContainer-root.MuiContainer-maxWidthLg.css-cssmpu > div.css-rijuka > div > div.css-1121uwa > div.css-3wqkda > div.css-1cw2qsn > div.css-0 > div > div > div.MuiFormControl-root.css-pb5ndi > div > div')
        time.sleep(1)
        page.click('text=Под ключ')


        page.click('text=Далее')


        with page.expect_response(lambda response: 'https://lk.pzzl.ru/api/projects/create-by-builder' in response.url) as response_info:
            pass
        time.sleep(0.5)


        page.click('#main_wrapper > div > div.MuiContainer-root.MuiContainer-maxWidthLg.css-cssmpu > div.css-rijuka > div > div.css-1121uwa > div.css-3wqkda > div.css-80jexa > div > div.css-3nqmk1 > div')
        time.sleep(0.5)

        page.fill('input[name="name"]', 'Екатерина')


        page.fill('input[name="phone"]', '1000000777')


        page.click('#modal_content > div.css-132esj0 > div:nth-child(4) > div')


        # Ответ с частичным совпадением URL
        with page.expect_response(
                lambda response: 'https://lk.pzzl.ru/api/projects/' in response.url and '/invites' in response.url
        ) as response_info:
            invite_response = response_info.value
            assert invite_response.status == 200, f"Ошибка при отправке приглашения: {invite_response.status_text}"
        time.sleep(0.5)


        name_locator = page.locator('text=Екатерина')
        phone_locator = page.locator('text=+7 (100) 000-07-77')

        assert name_locator.is_visible(), "Имя заказчика не отображается на экране"
        assert phone_locator.is_visible(), "Номер телефона заказчика не отображается на экране"

        page.click('text=Далее')
        time.sleep(2)


        final_name_locator = page.locator('text=Екатерина')
        final_phone_locator = page.locator('text=+7 (100) 000-07-77')
        status_locator = page.locator('text=Приглашение отправлено ожидаем ответа')
        step_locator = page.locator('text=1/2')
        resend_button_locator = page.locator('#projects_invite_block > div.css-12vdl56 > div.css-7a5k69 > div:nth-child(1)')
        change_number_button_locator = page.locator('text=Отправить на другой номер')

        # Проверка видимости всех элементов
        assert final_name_locator.is_visible(), "Имя заказчика не отображается на финальном экране"
        assert final_phone_locator.is_visible(), "Номер телефона заказчика не отображается на финальном экране"
        assert status_locator.is_visible(), "Статус приглашения не отображается"
        assert step_locator.is_visible(), "Шаги (1/2) не отображаются"
        assert resend_button_locator.is_visible(), "Кнопка 'Отправить еще раз' не отображается"
        assert change_number_button_locator.is_visible(), "Кнопка 'Отправить на другой номер' не отображается"

        print("Тест успешно выполнен!")


        browser.close()

if __name__ == "__main__":
    run_test()