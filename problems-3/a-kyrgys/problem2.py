class Biota:
    ...

class Archaea(Biota):
    ...


class Bacteria(Biota):
    ...


class Eukaryota(Biota):
    ...


class Protoza(Eukaryota):
    ...


class Chromista(Eukaryota):
    ...


class Plantae(Eukaryota):
    ...

class Pinophyta(Plantae):
    ...

if __name__ == "__main__":
    assert issubclass(Archaea, Biota)
    assert not issubclass(Pinophyta, Bacteria)
    assert issubclass(Plantae, Eukaryota)
    assert issubclass(Pinophyta, Eukaryota)
