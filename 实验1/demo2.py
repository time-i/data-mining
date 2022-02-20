

# 素数1：4111
# 素数2：3947
# 私钥：15372299
# 明文：28616


n = 16226117; e = 10259; c =8196714;
r = int(n ** 0.5);
#print(r);
pr = [];
for i in range(2,r):
    if n%i == 0:
        p = i;
        q = int(n/i);
        break;
#print(p,q,p*q);
f = (p-1)*(q-1);
#print(f);
y = 1; t = 0;
while(y != 0):
    t = t + 1;
    x = 1 + f*t;
    y = x % e;
d = int(x/e);
#print(d);

g = 1;j = 1
for i in range(0,d):
    j = j+1;
    g = g * c;
    if(j==10000):
        g = g % n;
        j = 1;
    print(i);
m = g % n;
print(m);