class FizzBuzz():
    def is_multiple(self, divisor, number):
        return number % divisor == 0

    def is_fizz(self, number):
        return self.is_multiple(3, number)

    def is_buzz(self, number):
        return self.is_multiple(5, number)

    def is_bang(self, number):
        return self.is_multiple(7, number)

    def say(self, number):
        if self.is_bang(number) and self.is_buzz(number) and self.is_fizz(number):
            return "fizzbuzzbang"
        if self.is_buzz(number) and self.is_fizz(number):
            return "fizzbuzz"
        if self.is_fizz(number) and self.is_bang(number):
            return "fizzbang"
        if self.is_buzz(number) and self.is_bang(number):
            return "buzzbang"
        if self.is_fizz(number):
            return "fizz"
        if self.is_buzz(number):
            return "buzz"
        if self.is_bang(number):
            return "bang"
        return str(number)

#Test can say
def test_can_say_one():
    fb = FizzBuzz()
    one = fb.say(1)
    assert one == "1"

def test_can_say_fizz_for_three():
    fb = FizzBuzz()
    fizz = fb.say(3)
    assert fizz == "fizz"

def test_can_say_fizz_for_six():
    fb = FizzBuzz()
    fizz = fb.say(6)
    assert fizz == "fizz"

def test_can_say_buzz_for_five():
    fb = FizzBuzz()
    buzz = fb.say(5)
    assert buzz == "buzz"

def test_can_say_fizzbuzz_for_fifteen():
    fb = FizzBuzz()
    fizzbuzz = fb.say(15)
    assert fizzbuzz == "fizzbuzz"

def test_can_say_fizzbang_for_twentyone():
    fb = FizzBuzz()
    fizzbang = fb.say(21)
    assert fizzbang == "fizzbang"

def test_can_say_buzzbang_for_thirthyfive():
    fb = FizzBuzz()
    buzzbang = fb.say(35)
    assert buzzbang == "buzzbang"

def test_can_say_bang_for_seven():
    fb = FizzBuzz()
    bang = fb.say(7)
    assert bang == "bang"

#Test is multiple
def test_is_multiple_of_three():
    fb = FizzBuzz()
    divisor = 3
    number = 9
    _true = fb.is_multiple(divisor, number)
    assert _true == True

#Test is fizz / buzz / bang
def test_is_fizz_for_3():
    fb = FizzBuzz()
    _true = fb.is_fizz(12)
    assert _true

def test_is_buzz_for_5():
    fb = FizzBuzz()
    _true = fb.is_buzz(20)
    assert _true

def test_is_fizzbang_for_21():
    fb = FizzBuzz()
    _true = fb.is_bang(21)
    assert _true

def test_isfizzbuzzbang_for_105():
    fb = FizzBuzz()
    fbb = fb.say(105)
    assert fbb == "fizzbuzzbang"
