wdraw, bal = tuple(input().split())
wdraw = int(float(wdraw))
bal = float(bal)
if ((wdraw % 5 == 0) and (bal > (wdraw+0.50))):
    print(bal-(wdraw+0.5))
else: 
   print(bal)  