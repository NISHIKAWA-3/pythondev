a = 2
b = 998
print(a)
a = 2; b = 998; print(a)
print(a)
c=30; print(c)
print(b)
a+b+c
def hello():
    print("Hello!")
    print("It is a rainy day today!")

def good():
    print("Good morning!")
    print("Have a nice day!"); good()

def hello():
    print("Hello!")
    print("It is a fine day today!")

def good_morning():
    print("Good morning!")
    print("Have a nice day!")

hello()
good_morning()
a=2
b=998
print(a)
def good_morning():
    print("Good morning!")
    print("Have a nice day!")
good_morning()
def hello():
    print("Hello!")
    print("It is a fine day today!")
hello()

name="bas"
def calc_bmi(height, weight):
    ret = weight / (height ** 2)
    return ret
height = float(input("身長(m)を入力："))
weight = float(input("体重(kg)を入力："))

# %%
def calc_bmi(height, weight):
    ret = weight / (height ** 2)
    return ret

height = float(input("身長(m)を入力："))
weight = float(input("体重(kg)を入力："))

bmi = calc_bmi(height, weight)
print(f"BMI値：{bmi:.1f}")


