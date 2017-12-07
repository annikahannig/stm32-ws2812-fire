
import colorcet

def hex2rgb(val):
    return tuple(int(val[i:i+2], 16) for i in (0, 2 ,4))


print("fire = [")
for v in colorcet.fire:
    print("{},".format(hex2rgb(v[1:])))

print("]")


