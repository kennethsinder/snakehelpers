import snakehelpers as sh

if __name__ == '__main__':
    needles = ['needle1', 'needle2']
    haystack = ['needle2', 'needle3']
    result = sh.any_in(needles, haystack)
    assert result is True
    print(needles)
    print(haystack)
    print(result)
