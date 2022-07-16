from ...utils.console import Console
import httpx, toml, time

__config__ = toml.loads(open('../../config/config.toml', 'r+').read())

class PhoneApi:
    @staticmethod
    def get_phone_number():
        err = 0
        bl = []
        while True:
            base_url = f'https://api.sms-activate.org/stubs/handler_api.php?api_key={__config__["phone"]["api_key"]}'
            with httpx.Client() as client:
                prices = client.get(f'{base_url}&action=getPrices&service=ds').json()

                country_code = 3
                cheap_cost = 100
                for price in prices:
                    if 'ds' not in str(prices[price]):
                        continue

                    item = prices[price]['ds']

                    if item['count'] == 0:
                        continue

                    if cheap_cost > item['cost'] and price not in bl:
                        cheap_cost = item['cost']
                        country_code = price

                Console.debug(f'Best country for phone found -> country: {country_code} --> price:  {cheap_cost}')

                response = client.get(f'{base_url}&action=getNumber&service=ds&country={country_code}').text.split(':')

                if response == [''] or response == ['NO_NUMBERS']:
                    if err == 3:
                        Console.debug(f'Blacklist country {country_code} due to many errors.')
                        bl.append(country_code)
                    else:
                        err += 1

                    Console.debug('Unable to get phone number, sleep 1s')
                    time.sleep(1)
                    continue

                #      task-id      phone-numb
                return response[1], response[2]

    @staticmethod
    def get_verification_code(task_id: str):
        base_url = f'https://api.sms-activate.org/stubs/handler_api.php?api_key={__config__["phone"]["api_key"]}'
        with httpx.Client() as client:
            Console.debug(client.get(f'{base_url}&action=setStatus&status=1&id={task_id}').text)

            errors = 0
            while errors < 60:
                response = client.get(f'{base_url}&action=getStatus&id={task_id}').text
                Console.debug(response)
                if 'STATUS_OK' in response:
                    return response.split(':')[1]
                else:
                    Console.debug(f'wait phone: {errors}')
                    time.sleep(1)
                    errors += 1

            Console.debug('banned phone / sms never sent')
            Console.debug(client.get(f'{base_url}&action=setStatus&status=8&id={task_id}').text)
            return None