
assert sum([10,20,30]) == 60, 'Should be 60'

def _sum():
    assert sum([10,20,30]) == 60, 'Should be 60'

def test_sum_tuple():  
    assert sum((1, 3, 5)) == 10, "It should be 10"  
  
if __name__ == "__main__":  
    _sum()  
    #test_sum_tuple()  
    print("Everything is correct")  