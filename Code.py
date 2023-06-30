#NAME: AMBAVARAPU TEJA REDDY
#COLLEGE: CMR INSTITUTE OF TECHNOLOGY
#YEAR OF PASSING: 2023
#PHONE NO: 9515689815
#EMAIL ID: amte19cs@cmrit.ac.in

class Shopping:
    def totalamount(s, price, gst, quant):
        amount = 0
        for i in range(len(price)):
            if price[i] >= 500:
                amount += price[i] * quant[i] + (gst[i] / 100 * price[i]) - (5 / 100 * price[i])
            else:
                amount += price[i] * quant[i] + (gst[i] / 100 * price[i])
        print("Amount paid to shop-keeper:")
        print(amount)

    def maxgst(s, price, gst, quant):
        amount = 0
        count = 0
        arr = []
        for i in range(len(price)):
            maxamt = gst[i] / 100 * price[i] * quant[i]
            arr.append(maxamt)
            maxamt = 0
        print()
        max_val = arr[0]
        index = 0
        for i in range(len(arr) - 1):
            if max_val < arr[i]:
                max_val = arr[i]
                index = i
        print("Maximum gst paid to:", s[index],"and Gst Amount :",price[index])

    def holdproduct(productname, price, gst, quant):
        print()
        print("Data structure:")
        products={'Products':[]} 
        for i in range(len(productname)):
            
            products['Products'].append({"product":productname[i],"price":price[i],"gst":gst[i],"Quantity":quant[i]})
        
    def extraele():
        s = ["Leather wallet", "umbrella", "cigarette", "honey"]
        print()
        print("More products to basket:")
        print(s)

    def main():
        productname = ["leather wallet", "umbrella", "cigarette", "Honey"]
        price = [1100, 900, 200, 100]
        gst = [18, 12, 28, 0]
        quant = [1, 4, 3, 2]

        Shopping.totalamount(productname, price, gst, quant) 
        Shopping.maxgst(productname, price, gst, quant)
        Shopping.holdproduct(productname, price, gst, quant) 
        Shopping.extraele()


Shopping.main()