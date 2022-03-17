"""
Write a function that partly emulates the built-in zip function (http://mng.bz/ Jyzv), taking any number of iterables and returning a list of tuples. Each tuple will contain one element from each of the iterables passed to the function. Thus, if I call myzip([10, 20,30], 'abc'), the result will be [(10, 'a'), (20, 'b'),(30,'c')]. You can return a list (not an iterator) and can assume that all of the iterables are of the same length.
"""
# book solution
# need to research and work out logic

def my_zip(*args):
    return [tuple(a[i] for a in args)
            for i in range(len(min(args, key=len)))]

print(my_zip([10,20,30], 'abc'))



