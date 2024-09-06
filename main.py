from collections import defaultdict

def f(s):
    r = {}
    for i in s:
        if i in r:
            r[i] += 1
        else:
            r[i] = 1
    return r


# NOTE: Suggestion codes    
def get_character_counts_with_get(string: str) -> dict[str, int]:
    """Get Character Count of a string using `.get()` method in dictionary.

    Args:
        string (str): input string

    Returns:
        dict[str, int]: count result dictionary
    """
    result = {}
    for i in string:
        result[i] = result.get(i, 0) + 1
    return result


def get_character_counts_with_defaultdict(string: str) -> dict[str, int]:
    """Get Character Count of a string using `.collections.defaultdict`.

    Args:
        string (str): input string

    Returns:
        dict[str, int]: count result dictionary
    """
    result = defaultdict(int)
    for i in string:
        result[i] += 1
    return dict(result)

def get_character_counts_with_comprehension(string: str) -> dict[str, int]:
    """Get Character Count of a string using `dictionary comprehension`.

    Args:
        string (str): input string

    Returns:
        dict[str, int]: count result dictionary
    """
    return {char: string.count(char) for char in set(string)}


if __name__ == "__main__":
    print(f("Hello"))
