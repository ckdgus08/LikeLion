#함수 가변인수(*, **)

def keyword_args(one, two, *args, **kwargs):
    print(one + two + sum(args))
    print(kwargs)
keyword_args(1,2,3,4,5,6, first=3,tw=4,thre=5)