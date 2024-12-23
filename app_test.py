from app import process_query


expected_str = "Dinosaurs ruled the Earth 200 million years ago"


def test_knows_about_dinosaurs():
    assert process_query("dinosaurs") == expected_str


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"


def test_knows_name():
    assert process_query("What is your name?") == "Will"


def test_largest_numbers():
    assert process_query("Which of the following numbers is the largest: 26, 36, 75?") == "75"


def test_adding_numbers():
    assert process_query("What is 8 plus 64?") == "72"
    

def test_multiplying_numbers():
    assert process_query("What is 3 multiplied by 5?") == "15"
    

def test_square_checking():
    assert process_query("Which of the following numbers is both a square and a cube: 1268, 512, 729, 3199, 1730, 196, 3886?") == "729"


def test_minus():
    assert process_query("What is 14 minus 31?") == "-17"


def test_prime():
    assert process_query("Which of the followiung numbers are primes: 7, 10, 11, 19?") == "7, 11, 19"


def test_prime_one():
    assert process_query("Which of the followiung numbers are primes: 7, 10, 12, 18?") == "7"

def test_power():
    assert process_query("What is 2 to the power of 3?") == "8"