class Checker:

    @staticmethod
    def check_str_loks_like_int_num(str_value):
        try:
            int(str_value)
            return True
        except ValueError:
            print('\nIncorect answer! Value must be an integer number.')
            print('Try again!\n')
            return False

    @staticmethod
    def check_number_in_range(number, start=1, end=None):
        if end is not None and end > start:
            if start <= number <= end:
                return True
            msg = 'Value must be a number in range [{},{}].'.format(start, end)
        else:
            if number >= start:
                return True
            msg = 'Value must be a number greater then {}.'.format(start)
        print('\nIncorect answer! {}\nTry again!\n'.format(msg))
        return False

    @staticmethod
    def check_length(str_value, length):
        if len(str_value) >= length:
            return True
        print('\nIncorect value! Name length must be greater then {}.'.format(length))
        return False
