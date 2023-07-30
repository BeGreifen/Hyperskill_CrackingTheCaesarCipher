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
    logging.info(result)
    return result


# Example usage
@decorator
def string_list_to_numb(char_list: list) -> list:
    logging.info(inspect.stack()[0][3])
    logging.info(char_list)
    result = []
    for char in char_list:
        result.append(ord(char) - ord("a"))
    return result


@decorator
def get_cesar(input_numb: list, offset=0) -> list:
    result_list = []
    for numb in input_numb:
        result_list.append((numb + offset) % 26)
    logging.info(result_list)
    return result_list


@decorator
def numb_list_to_char_list(input_numb: list) -> list:
    result_list = []
    for numb in input_numb:
        result_list.append(string.ascii_lowercase[int(numb)])
    logging.info(result_list)
    return result_list


# Write your code here
@decorator
def main():
    # result = output_result(numb_list_to_char_list(input().split()))
    result = numb_list_to_char_list(get_cesar(string_list_to_numb(input().split()),3))
    output_result(result)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filename='app.log',  # Specify the file name for logging
                        filemode='w'  # Use 'w' mode to overwrite the log file on each run, or 'a' to append
                        )
    logging.info("**** solution started ****")
    # for inti in range(15, 18):
    #     print(inti)
    #     print("".join(
    #         numb_list_to_char_list(
    #             get_cesar(
    #                 string_list_to_numb("algorithms"), inti)
    #         )
    #     )
    #     )
    main()
