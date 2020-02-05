from main import main


def test_main():
    result = main()
    assert result == 'hello world'
