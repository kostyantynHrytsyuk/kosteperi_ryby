"""
Shoty Tam is a popular gathering spot for UCU students,
where they can enjoy shots and socialize with friends.
It's a lively place to party and have fun, and is known
for its energetic atmosphere. Whether you're looking to
unwind after a long day of studying or just want to hang
out with your peers, Shoty Tam is the perfect destination
for a good time.
"""

from shoty_tam import *

def test_shoty_tam():
    """
    Print Done if all tests passed
    """

    # Shoty Tam has number people it can contain
    # at once and number of available shots and cocktails
    shoty_tam = ShotyTam(10, 42, 20)
    assert shoty_tam.people == 10
    assert shoty_tam.shots == 42
    assert shoty_tam.cocktails == 20
    assert str(shoty_tam) == "Bar contains 10 people, has 42 availabe shots and 20 cocktails"

    # shots and cocktails are different, they have taste and label

    honey_moon = Shot("Sour", "Yellow")
    tequila_sunrise = Shot('Bitter', "Yellow")
    skull_chaser = Shot("Double Trouble", "Orange")
    spicy_rainbow = Shot("Spicy", "Orange")
    red_dog = Shot("Spicy", "Red")
    hot_lava = Shot("Spicy", "Red")
    assert str(honey_moon) == "Sour shot with Yellow label"
    assert skull_chaser != red_dog

    tequila_boom = Cocktail("Bitter", "Yellow")
    new_power = Cocktail("Spicy", "Orange")
    assert str(tequila_boom) == "Bitter cocktail with Yellow label"
    assert tequila_boom != new_power

    # Studens can drink only specific number of drinks
    # UCU student can drink 10 shots
    # LNU - 6 shots 1 cocktail
    # NULP - 4 shots 4 cocktails
    UCU_student = UCUstudent(shoty_tam)
    UCU_student_drinks = [honey_moon, honey_moon, honey_moon, skull_chaser]
    UCU_student.set_drinks(UCU_student_drinks)
    assert str(UCU_student) == "UCU student wants to drink 4 shots and 0 cocktails"


    LNU_student = LNUstudent(shoty_tam)
    LNU_student_drinks = [red_dog, red_dog, red_dog, new_power]
    LNU_student.set_drinks(LNU_student_drinks)
    assert str(LNU_student) == "LNU student wants to drink 3 shots and 1 cocktails"

    NULP_student = NULPstudent(shoty_tam)
    try:
        NULP_student_drinks = [skull_chaser, skull_chaser, skull_chaser, skull_chaser, tequila_boom, tequila_boom, tequila_boom, new_power, new_power]
        NULP_student.set_drinks(NULP_student_drinks)
    except DrinkLimitException:
        assert str(NULP_student) == "NULP student wants to drink 4 shots and 5 cocktails, but can't"

    # Student can't drink more than he is eligible
    assert UCU_student.shots == 4
    assert LNU_student.cocktails == 1
    assert NULP_student.shots == 4 # if he ordered 5 he can only drink 4

    # If student reaches his limit he can't drink as well
    assert UCU_student.can_drink == True
    assert LNU_student.can_drink == True
    assert NULP_student.can_drink == False

    # If student reaches his limit he can't do anything else
    assert UCU_student.can_dance == True
    assert LNU_student.can_dance == True
    assert NULP_student.can_dance == False

    # Shoty Tam tracks queue of drinks that were sold
    assert isinstance(ShotyTam._ShotyTam__queue[3], Shot)
    assert isinstance(ShotyTam._ShotyTam__queue[0], Shot)
    assert isinstance(ShotyTam._ShotyTam__queue[7], Cocktail)

    # And shows the number of free places and drinks that are left
    assert shoty_tam.people == 7
    assert shoty_tam.shots == 31
    assert shoty_tam.cocktails == 15

    # Closer to evening more and students come to the bar
    # So it's possible that there is no place or all drinks are gone
    UCU_student2 = UCUstudent(shoty_tam)
    UCU_student_drinks2 = [tequila_sunrise, spicy_rainbow, honey_moon, hot_lava, hot_lava, hot_lava]
    UCU_student2.set_drinks(UCU_student_drinks2)

    UCU_student3 = UCUstudent(shoty_tam)
    UCU_student_drinks3 = [tequila_sunrise, tequila_sunrise, spicy_rainbow, spicy_rainbow, spicy_rainbow, spicy_rainbow, hot_lava]
    UCU_student3.set_drinks(UCU_student_drinks3)

    UCU_student4 = UCUstudent(shoty_tam)
    UCU_student_drinks4 = [honey_moon, tequila_sunrise, honey_moon, honey_moon, spicy_rainbow, spicy_rainbow, honey_moon]
    UCU_student4.set_drinks(UCU_student_drinks4)

    assert shoty_tam.people == 4
    assert shoty_tam.shots == 11
    assert shoty_tam.cocktails == 15

    LNU_student2 = LNUstudent(shoty_tam)
    LNU_student_drinks2 = [red_dog, tequila_sunrise, tequila_sunrise, tequila_sunrise, new_power]
    LNU_student2.set_drinks(LNU_student_drinks2)

    LNU_student3 = LNUstudent(shoty_tam)
    LNU_student_drinks3 = [spicy_rainbow, tequila_sunrise, spicy_rainbow, spicy_rainbow, new_power]
    LNU_student3.set_drinks(LNU_student_drinks3)

    assert shoty_tam.people == 2
    assert shoty_tam.shots == 3
    assert shoty_tam.cocktails == 13

    NULP_student2 = NULPstudent(shoty_tam)
    NULP_student_drinks2 = [spicy_rainbow, spicy_rainbow, tequila_boom, tequila_boom, new_power, new_power]
    NULP_student2.set_drinks(NULP_student_drinks2)

    NULP_student2 = NULPstudent(shoty_tam)
    NULP_student_drinks2 = [tequila_sunrise, tequila_boom, tequila_boom, tequila_boom, new_power]
    NULP_student2.set_drinks(NULP_student_drinks2)

    assert shoty_tam.people == 0
    assert shoty_tam.shots == 0
    assert shoty_tam.cocktails == 5

    try:
        NULP_student2 = NULPstudent(shoty_tam)
    except TooManyPeopleException:
        assert str(shoty_tam) == "Bar is full of people, has 0 availabe shots and 5 cocktails"

    try:
        NULP_student_drinks2.append(tequila_sunrise)
    except NoShotsException:
        assert str(shoty_tam) == "Bar is full of people, has 0 availabe shots and 5 cocktails"

    print('Done!')


if __name__ == "__main__":
    test_shoty_tam()
