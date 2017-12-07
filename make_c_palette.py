
import colorcet

pal = colorcet.fire


def hex2rgb(val):
    return tuple(int(val[i:i+2], 16) for i in (0, 2 ,4))


print("#ifndef FIRE_PALETTE_H")
print("#define FIRE_PALETTE_H")
print()

print("uint8_t fire_palette[] = {")
for v in pal[:-1]:
    c = hex2rgb(v[1:])
    print("{}, {}, {},".format(c[0], c[1], c[2]))


c = hex2rgb(pal[-1][1:])
print("{}, {}, {}".format(c[0], c[1], c[2]))

print("};")

print()
print("#endif")

print()
