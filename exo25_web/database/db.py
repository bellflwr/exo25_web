from dataclasses import dataclass
import sqlite3

con = sqlite3.connect("Exoplanets.db")
cur = con.cursor()


@dataclass
class Exoplanet:
    name: str
    planet_type: str
    diameter: int
    distance: int
    material: str
    gas: bool
    rings: int
    colour: str
    climate: int
    star_type: str

    @classmethod
    def from_id(cls, exoplanet_id):
        exoplanet_query = cur.execute("SELECT Name, Type, Diameter, Distance, Material, Gas, Rings, Colour,"
                                      "Climate, StarType FROM Exoplanets WHERE ID = ?", (exoplanet_id,)).fetchone()
        return cls(*exoplanet_query)

    def commit(self):
        inserted_tuple = (self.name, self.planet_type, self.diameter, self.distance, self.material,
                          self.gas, self.rings, self.colour, self.climate, self.star_type)
        cur.execute("INSERT INTO Exoplanets(Name, Type, Diameter, Distance, Material, Gas, Rings, Colour, Climate,"
                    "StarType) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", inserted_tuple)
        con.commit()

    @staticmethod
    def exoplanet_count():
        return cur.execute("SELECT COUNT(*) FROM Exoplanets").fetchone()[0]


# planet = Exoplanet("Earth", "Earth", 12742, 1, "soil", False, 0, "Blue", 20, 'O')
