import session11_part_1
import session11_part_2
from session11_part_1 import *
from session11_part_2 import *
from datetime import datetime
import pytest
import sys
import time
import re  
import inspect
import os

README_CONTENT_CHECK_FOR = [
    "repr",
    "gt",
    "eq",
    "edges",
    "circumradius",
    "vertices",
    "interior_angle",
    "edge_length",
    "len",
    "getitem",
    "efficient_polygon" 
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add at least 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations_1():
    ''' Returns pass if used four spaces for each level of syntactically significant indenting.'''
    lines = inspect.getsource(session11_part_1)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_indentations_2():
    ''' Returns pass if used four spaces for each level of syntactically significant indenting.'''
    lines = inspect.getsource(session11_part_2)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(
            r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_Polygon_1():
    p1 = Polygon(10, 12)
    assert bool(p1.apothem), 'It should return some value , please check your code !!'
    assert bool(p1.area), 'It should return some value , please check your code !!'
    assert bool(p1.circumradius), 'It should return some value , please check your code !!'
    assert bool(p1.edge_length), 'It should return some value , please check your code !!'
    assert bool(p1.interior_angle), 'It should return some value , please check your code !!'
    assert bool(p1.perimeter), 'It should return some value , please check your code !!'
    assert bool(p1.vertices), 'It should return some value , please check your code !!'
   

def test_Polygon_2():
    p1 = Polygon(8, 14)
    assert bool(p1.apothem), 'It should return some value , please check your code !!'
    assert bool(p1.area), 'It should return some value , please check your code !!'
    assert bool(p1.circumradius), 'It should return some value , please check your code !!'
    assert bool(p1.edge_length), 'It should return some value , please check your code !!'
    assert bool(p1.interior_angle), 'It should return some value , please check your code !!'
    assert bool(p1.perimeter), 'It should return some value , please check your code !!'
    assert bool(p1.vertices), 'It should return some value , please check your code !!'
    
    
def test_Polygon_gt():
    p1 = Polygon(10, 12)
    p2 = Polygon(8, 14)
    assert bool(p1.__gt__(p2)), 'P1 should greater than P2 , please check your code !!'
    
def test_Polygon_eq():
    p1 = Polygon(10, 12)
    p2 = Polygon(10, 12)
    assert bool(p1.__eq__(p2)), 'P1 should equal to P2 , please check your code !!'
    assert bool(p1 == p2), 'P1 should equal to P2 , please check your code !!'
    
   
def test_polygon_size():
    with pytest.raises(ValueError):
        q1 = Polygon(2, 3)

def test_PolygonSequence():
    p1 = PolygonSequence(25, 6)
    assert bool(p1._circumradius), 'It should return some value , please check your code !!'
    

def test_PolygonSequence_efficient():
    p1 = PolygonSequence(25, 6)
    assert p1.efficient_polygon.edges == 25, 'It should return 25 , please check your code !!'


def test_PolygonSequence_next():
    poly1 = PolygonSequence(25, 6)
    l = [Polygon for Polygon in poly1]
    k = iter(l)
    assert bool(next(k)), 'It should return something , please check your code !!'


def test_polygon():
    abs_tol = 0.001
    rel_tol = 0.001

    n = 4
    R = 1
    p = Polygon(n, R)
    assert p.interior_angle == 90, (f'actual: {p.interior_angle}, '
                                    ' expected: 90')
    assert math.isclose(p.area, 2,
                        rel_tol=abs_tol,
                        abs_tol=abs_tol), (f'actual: {p.area},'
                                           ' expected: 2.0')


    assert math.isclose(p.perimeter, 4 * math.sqrt(2),
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                           f' expected: {4 * math.sqrt(2)}')

    assert math.isclose(p.apothem, 0.707,
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                           ' expected: 0.707')
    p = Polygon(6, 2)
    
    assert math.isclose(p.apothem, 1.73205,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 10.3923,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 12,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 120,
                        rel_tol=rel_tol, abs_tol=abs_tol)

    p = Polygon(12, 3)
   
    assert math.isclose(p.apothem, 2.89778,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 27,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 18.635,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 150,
                        rel_tol=rel_tol, abs_tol=abs_tol)

    p1 = Polygon(3, 10)
    p2 = Polygon(10, 10)
    p3 = Polygon(15, 10)
    p4 = Polygon(15, 100)
    p5 = Polygon(15, 100)

    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5
