import sys

class Log:
    FILE = None

    def fname():
        return sys._getframe(2).f_code.co_name
    
    def pin(content, marker):
        print(f'[{marker}] {content} : ', end = '')

    def alert(message):
        Log.pin(Log.fname(), '!')
        print(message)

    def ok(message):
        Log.pin(Log.fname(), '-')
        print(message)

