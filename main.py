from zoo import Zoo
from Animal import Animal
from Serpant import Serpent
from Oiseau import Oiseau
def main():
    a = Animal("cat", 1, 1)
    a.se_deplacer()
    s=Serpent("ss", 1, 1)
    s.se_deplacer()
    o=Oiseau("ss", 1, 1)
    o.se_deplacer()
    o.dosomething()
    print(o.altitude_max())
    z=Zoo([s,o])
    z.dosomething()
    print(z)
    z.add_animal(a)
    print(z)
    print(z+z)

if __name__ == "__main__":
    main()