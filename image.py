with open('image.ppm', "w") as file:
    file.write("p3\n500 500\n100\n")
    for x in xrange(500):
        for y in xrange(500):
            num = (x + y) % 100
            file.write("{0} {0} {0}\n".format(num))
    file.close()
