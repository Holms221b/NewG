import pytest

#i = 6
##b = ("")
#def lol ():
 #   if a == b:
  #      print(a)
   # elif a :
    #    print(b)


#lol("jjdf")


# def lol (c):
#     b = str(c)
#     if len(b) == 0:
#         print('Hello world!')
#     else:
#         print(f'Hello {b}')
# lol( c = 'sd')


# m = (f' Hello')
# def hello(name):
#     print(name + m)
#
# hello (name='1')

@pytest.fixture()
def before_after():
    print('Hello')
    yield
    print('\n Hello2')

def test_t():
    assert 1 == 1

def test_d(before_after):
    assert 1 != 1


