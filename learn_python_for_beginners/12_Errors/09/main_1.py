def main():
    try:
        print(IndexError.__mro__)
        print(ZeroDivisionError.__mro__)
        raise Exception("zero division")
    except ZeroDivisionError as e:
        print("zero")
    except Exception as e:
        print("other")

main()
