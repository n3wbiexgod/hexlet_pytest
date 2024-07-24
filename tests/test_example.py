from hexlet_pytest.example import reverse

def test_reverse():
    print('Testing reverse with Hexlet')
    assert reverse('Hexlet') == 'telxeH'

def test_reverse_for_empty_string():
    print('Testing reverse with empty string')
    assert reverse('') == ''
