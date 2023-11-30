import datetime

yellow = '\033[01;33m'
white = '\033[01;37m'
green = '\033[01;32m'
blue = '\033[01;34m'
red = '\033[1;31m'
end = '\033[0m'


def custom_encode(input_string):
    encoded_string = ''.join(['%' + char.encode('utf-8').hex() for char in input_string])
    return encoded_string


while True:
    user_input = input(f"[{blue}{datetime.datetime.now().strftime('%H:%M:%S')}{end}] [{green}INFO{end}] Target string :{blue}~{end}$ ")
    encoded_result = custom_encode(user_input)

    mes = f"""
Urlencode resumed the following point(s) from stored session:
-----
Urlencode result
    Type: URL-encoded table combination strings
    Target raw string: {user_input}
    URL-encoded string: {encoded_result}
-----"""
    print(mes)





