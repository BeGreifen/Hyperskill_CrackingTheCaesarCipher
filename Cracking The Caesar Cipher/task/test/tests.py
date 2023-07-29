import logging
from hstest import CheckResult, TestedProgram, StageTest, dynamic_test, WrongAnswer
import string


def encoder_1(message):
    # making the encoded message
    # string 'cheesecake' becomes list [2, 7, 4, 4, 18, 4, 2, 0, 10, 4]
    # then becomes string '2 7 4 4 18 4 2 0 10 4' with space delimiter
    # does not encode ' ' spaces
    # please use 'x' instead of ' ' if spaces are desired
    message = message.lower()
    message_encoded = [string.ascii_lowercase.index(letter) for letter in message]
    message_encoded_for_stdin = ' '.join([str(i) for i in message_encoded])
    return message_encoded_for_stdin


class DecipherTest(StageTest):
    test_data = [
        'Cheesecake',
        'Hello',
        'World',
        'Dog',
        'Mousse'
    ]

    @dynamic_test(data=test_data)
    def test(self, x):
        encoded_message = encoder_1(x)  # a string full of ints separated by spaces
        pr = TestedProgram()
        pr.start()
        output = pr.execute(stdin=encoded_message)
        if not output:
            raise WrongAnswer('Your program did not print anything.')
        if not output.isascii():
            raise WrongAnswer('This string contains non-ascii values.')
        output_cleaned = output.lower().strip().replace(' ', '')
        check = x.lower().replace(' ', '') in output_cleaned
        return CheckResult(check, f'Wrong message returned.\n'
                                  f'You printed: {output}Original message: {x}\n'
                                  f'(Capitalization does not matter)')


if __name__ == '__main__':
    DecipherTest().run_tests()
