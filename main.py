from foo.sphere import Sphere

def main():
    radius = 1
    sphere = Sphere(radius)
    print(f"The volume of a sphere with radius {radius} is {sphere.volume()}")

if __name__ == "__main__":
    main()
