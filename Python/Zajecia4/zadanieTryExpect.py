if __name__ == '__main__':
    
        while True:
            try:
                number = int(input('Podaj liczbe: '))         
            except ValueError as ve:
                print(ve)
                print('To nie to')
            finally:
                print('to zawsze wykonam')
               