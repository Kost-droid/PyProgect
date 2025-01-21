
class MyBlocManager:

    def __enter__(self):
        print ('Entering context')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print (exc_type, exc_val)
        print ('Exit')
        return True

    def print_name (self):
        print ('I am!')

def main ():
    #test = ''
    with MyBlocManager () as manager:
       manager.print_name()
       g  = 1/0
       test = 1


    print (test)

main ()