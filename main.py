from zoo import Zoo
from Animal import Animal
from Serpant import Serpent
from Oiseau import Oiseau
def main():
    a = Animal("cat", 1, 1)
    a.se_deplacer()
    s=Serpent("ss", 1, 1)
    s.se_deplacer()
    o=Oiseau("ss", 1, 1, 100)
    print(o.altmax)
    o.altmax=150
    print(o.altmax)
    o.se_deplacer()
    o.dosomething()
    z=Zoo([s,o])
    z.dosomething()
    print(z)
    z.add_animal(a)
    print(z)
    print(z+z)

if __name__ == "__main__":
    main()