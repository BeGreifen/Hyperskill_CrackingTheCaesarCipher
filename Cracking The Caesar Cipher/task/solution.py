import string
import logging
import inspect


def decorator(func):
    def wrap(*args, **kwargs):
        logging.info(
            f"{func.__name__} - line no: {inspect.getframeinfo(inspect.currentframe().f_back).lineno} with args: {args}, kwargs: {kwargs}")
        # Log the function name and arguments

        # Call the original function
        result = func(*args, **kwargs)

        # Log the return value
        logging.info(f"{func.__name__} returned: {result}")

        # Return the result
        return result

    return wrap


@decorator
def output_result(result_list: list):
    result = "".join(result_list)
    print(result)
    return result


# Example usage
@decorator
def string_list_to_numb(char_list: list) -> list:
    result = []
    if len(char_list) > 1:
        for char in char_list:
            result.append(ord(char) - ord("a"))
    else:
        result = ord(char_list[0]) - ord("a")
    return result


@decorator
def get_cesar(input_numb: list, offset=0) -> list:
    result_list = []
    if isinstance(input_numb, list):
        for numb in input_numb:
            result_list.append((numb + offset) % 26)
    else:
        result_list = (int(input_numb) + offset) % 26
    return result_list


@decorator
def numb_list_to_char_list(input_numb: list) -> list:
    result_list = []
    for numb in input_numb:
        result_list.append(string.ascii_lowercase[numb])
    return result_list


def create_dict(word: str) -> dict:
    dict_find_shift = {}

    for inti, _ in enumerate(string.ascii_lowercase):
        enc_word = "".join(numb_list_to_char_list(
            get_cesar(
                string_list_to_numb(word), inti)))
        dict_find_shift[enc_word] = int(inti)

    return dict_find_shift


@decorator
def create_vigenere_cipher_key(word: str, key_len: int) -> list:
    key_repeated = []
    while len(key_repeated) < key_len:
        key_repeated += word
    logging.info(key_repeated)
    result = string_list_to_numb(key_repeated)
    return result


@decorator
def decode_vigenere_cipher(list_of_encrypted_numbs: str, list_of_key_shifts) -> list:
    result = []
    logging.info(list_of_key_shifts)
    for n, k in zip(list_of_encrypted_numbs, list_of_key_shifts):
        result.append((n-k) % 26)
    output_result(numb_list_to_char_list(result))
    return result


def task3():
    butterscotch_dict = create_dict("butterscotch")
    lower_input = "".join(input().lower().split())
    print(lower_input)
    shift = 0
    for k, v in butterscotch_dict.items():
        if lower_input.find(k) > -1:
            shift = butterscotch_dict[k]
            logging.warning(f"found shift value of: {shift} , {k}")
    result: list = numb_list_to_char_list(
        get_cesar(
            string_list_to_numb(input().lower().split()), -shift))
    output_result(result)


@decorator
def main():
    # result = output_result(numb_list_to_char_list(input().split()))
    # len_key = input()
    raw_key = input("key:")
    numb_encrypted = input("to encrypt:").replace(" ", "x")
    numb_encrypted = string_list_to_numb(numb_encrypted)
    numb_vigenere_cipher_key = create_vigenere_cipher_key(raw_key, len(numb_encrypted))
    decode_vigenere_cipher(numb_encrypted, numb_vigenere_cipher_key)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filename='app.log',  # Specify the file name for logging
                        filemode='w'  # Use 'w' mode to overwrite the log file on each run, or 'a' to append
                        )
    logging.info("**** solution started ****")
    main()
