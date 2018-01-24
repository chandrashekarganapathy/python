# snake and ladder
import random
count=0
while(count<=100):
    n=input("press g to roll a dice")
    if(n=='g'):
        g=random.randint(1,6)
        count=count+g
        print("your random is",g)
        print("your count is ",count)
if count==8:
    count=37
    print("great you have climbed the ladder",count)
elif count==11:
    count=2
    print("sorry snake bite you",count)
elif count==25:
    count=4
    print("sorry snake bite you",count)
elif count==38:
    count9
    print("sorry snake bite you",count)
elif count==40:
    count=68
    print("great you have climbed the laddder",count)
elif count==52:
    count=81
    print("great you have climbed the ladder",count)
elif count==65:
    count=46
    print("snake bite you",count)
elif count==76:
    count=97
    print("great you have climbed the ladder",count)
elif count==89:
    count=70
    print("sorry snake bite you",count)
elif count==93:
    count=64
    print("sorry snake bite you",count)


