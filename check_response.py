from request_module import *


def check_response_code():
    if response_bcc.status_code == 200:
        print("Success, Enter!")

    elif response_bcc.status_code == 400:
        print("Page not Found")

    elif response_bcc.status_code == 404:
        print("Oops Sorry something went wrong")



check_response_code()
