#function_demo_05
#keyword parmeters

def pyramid(height) :
    off =5
    offs =' '* off
    width = 2*height + 1
    _pyramid = ''
    for i in range(height) :
        tiles = offs + ('*'*(2*i+1)).center(width)
        _pyramid += tiles + "\n"

    return _pyramid

print(pyramid(5))
print(pyramid(7))
print(pyramid(10))

def pyramid2(height=5, off=5, tile = '*', spc = ' ') :
    offs = spc * off
    width = 2*height + 1
    _pyramid = ''
    for i in range(height) :
        tiles = offs + (tile * (2*i+1)).center(width)
        _pyramid += tiles + "\n"

    return _pyramid

print(pyramid2())
print(pyramid2(7))
print(pyramid2(7,10))
print(pyramid2(7,10,'^'))
print(pyramid2(5,10,'J','-'))

print(pyramid2(height=5,spc = '.', tile ='*', off =10))
desc = {'height' : 5, 'tile' : '*', 'off' : 10,'spc' : '.'}
p2 = pyramid2(**desc) #** unpack dictionary
print(p2)

desc2 = {'height' : 7, 'tile' : '^'}
print(pyramid2(**desc2))

desc3 ={'height' : -8, 'off' : 12, 'spc' : '$'}
print(pyramid2(**desc3))


def foo(**kwargs) :
    arg_type = type(kwargs)
    print("f{arg_type=}")
    print("f{kwargs=}")

foo(**desc3)
foo(a = 1,b =2, c=3)
dc = {'a':1, 'b':2, 'c':3}
foo(**dc)



def pyramid3(height =5, **kwargs) :
    """
    height:int, tile:str, spc:str,
    off:int will have to be passed in to kwargs
    return 
    """

    spc = kwargs.get('spc', ' ')
    off = kwargs.get('off',5)
    tile = kwargs.get('tile', '=')
    height = kwargs.get('height',10)
    
    offs = spc * off
    width = 2*height + 1
    _pyramid = ''
    for i in range(height) :
        tiles = offs + (tile * (2*i+1)).center(width)
        _pyramid += tiles + "\n"

    return _pyramid

print(pyramid3(height=4, tile = '^',spc='.'))
print(pyramid3(height=14, tile = '^',off=12))
print(pyramid3(height=14, off = 8))

