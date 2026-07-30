def greetcustomer():
    print("Hello, this is an art supplies billing tool.")
greetcustomer()
cray=int(input("How many crayons are you going to buy: "))
mark=int(input("How many markers are you going to buy: "))
crayprice=float(input("What are the price per crayons: "))
markprice=float(input("What are the price per markers: "))
def caculatecraytotal(cray,crayprice):
    total= cray*crayprice
    return total
def caculatmarktotal(mark,markprice):
    tot=mark*markprice
    return tot
print("======Billing Total======")
cray_total = caculatecraytotal(cray, crayprice)
mark_total = caculatmarktotal(mark, markprice)
print("Total price for the crayons:", cray_total)
print("Total price for the markers:", mark_total)
print("Grand total:", cray_total + mark_total)