from observer.observer import Observer


def main():
    ans = input('Choice mode:\n1. Start Loader\nRemake cookies')
    if ans == '1':
        soft = Observer()
        soft.scrolling()
    elif ans == '2':
        pass
    else:
        print('Incorrect mode.')


if __name__ == '__main__':
    main()
