
import colorcet

def hex2rgb(val):
    return tuple(int(val[i:i+2], 16) for i in (0, 2 ,4))


print("uint8_t fire_palette[] = [")
for v in colorcet.fire:
    c = hex2rgb(v[1:])
    print("{}, {}, {},".format(c[0], c[1], c[2]))

print("];")


