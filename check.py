class Checker:

    @staticmethod
    def check_str_loks_like_int_num(str_value):
        try:
            int(str_value)
            return True
        except ValueError:
            print('Incorect answer! Value must be an integer number')
            return False
