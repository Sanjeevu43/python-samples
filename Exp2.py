#import Exp1
import sys

sys.stdout.write("Welcome");
x=20; y=21;
print("\n")
print(id(x));
print(id(y));

def f2(l):
    print("Before Modify : ", l);
    l = [10,11,12];
    print("After Modify : ", l);

list = [9,11,12]
f2(list)
print("Outside Function : ",list)
print(len(list))


def test1():
    captured_amwa = captured_amwa_proc = "",""
    captured_amf, captured_amf_proc, captured_amfb, captured_amf_procb = ""

test1()
