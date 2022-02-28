from parabola_with_tangent import *
from circle_and_curve import *
import sys

if len(sys.argv) < 3:
    sys.exit('Proszę podać parametry wywołania:\n' +
             '1. 1 - styczna i parabola, 2 - okrag i krzywa\n' +
             '2. x(t)\n' +
             '3. y(t)\n')

#p = P()
#p.tangent_following_parabola()
#plt.show()

if sys.argv[1] == '1':
    p = P()
    le = int(input("1 - styczna po paraboli\n 2 - parabola po stycznej\n: "))
    if le == 1:
        p.tangent_following_parabola()
        plt.show()
    elif le == 2:
        p.parabola_following_tangent()
        plt.show()
elif sys.argv[1] == '2':
    r = float(input("Promien okregu: "))
    c = C(r, sys.argv[2], sys.argv[3], False)
    c.running_circle()
    plt.show()


