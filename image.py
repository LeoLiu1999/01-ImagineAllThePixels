from math import sqrt, pow

with open('image.ppm', "w") as file:
    file.write("P3\n500 500\n100\n")
    for x in xrange(500):
        for y in xrange(500):
            if (x > 125 and x < 375 and y > 125 and y < 375):
                num = int(sqrt(pow(250 - x, 2) + pow(250 - y, 2))) % 100
                file.write("{0} 100 {0}\n".format(num / 2 + 25))
            else:
                y_quad = x % 500 < 250
                x_quad = y % 500 < 250
                if((y_quad and not x_quad) or (not y_quad and x_quad)):
                    num = (x + y) % 100
                    file.write("100 {0} {0}\n".format(100 - num))
                else:
                    num = (x - y) % 100
                    file.write("{0} {0} 100\n".format(num))
    file.close()
