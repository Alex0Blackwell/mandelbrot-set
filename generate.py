# Credit: https://github.com/danyaal/mandelbrot

import numpy as np
import matplotlib.pyplot as plt


class Mandelbrot():
    """
    Class for generating and displaying Mandelbrot sets.

    Attributes:
        density (int): How spaced out each point of the set is. A higher number
        will result in a clearer picture and a longer run time.
    """

    def __init__(self, density):
        self.density = density


    def __itrUntilDivergent(self, complexP):
        """
        Private method to get how many iterations it takes for a point to diverge.
        Use the definition: the set for which f(z) = z^2 + c does not diverge.

        Parameters:
            complexP (ComplexNumber): The complex number to test.

        Returns:
            i (int): How many iterations it took until the function diverges (max 100)
        """
        z = complex(0, 0)
        for i in range(100):
            z = (z*z) + complexP
            if(abs(z) > 4):
                break

        return i


    def generate(self):
        """Generate and show the mandelbrot set."""

        # location and size of the atlas rectangle
        realAxis = np.linspace(-2.25, 0.75, self.density)
        imaginaryAxis = np.linspace(-1.5, 1.5, self.density)
        realAxisLen = len(realAxis)
        imaginaryAxisLen = len(imaginaryAxis)

        # 2-D list to represent mandelbrot atlas
        atlas = np.empty((realAxisLen, imaginaryAxisLen))

        # color each point in the atlas depending on the iteration count
        for x in range(realAxisLen):
            for y in range(imaginaryAxisLen):
                cx = realAxis[x]
                cy = imaginaryAxis[y]
                c = complex(cx, cy)

                atlas[x, y] = self.__itrUntilDivergent(c)

        # plot and display the set
        plt.imshow(atlas.T, cmap='Blues', interpolation="nearest")
        plt.axis("off")
        plt.show()



def main():
    set = Mandelbrot(1000)
    set.generate()


if __name__ == '__main__':
    main()
