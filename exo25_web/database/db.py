from dataclasses import dataclass
import sqlite3
from flask import g

con = sqlite3.connect("../../Exoplanets.db")
# cur = con.cursor()

DATABASE = "Exoplanets.db"


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@dataclass
class Exoplanet:
    # Instantiating all attributes
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

    # Takes a cursor and id of a row/exoplanet
    @classmethod
    def from_id(cls, cur, exoplanet_id):
        # Takes exoplanet_id and finds row with corresponding ID
        exoplanet_query = cur.execute(
            "SELECT Name, Type, Diameter, Distance, Material, Gas, Rings, Colour,"
            "Climate, StarType FROM Exoplanets WHERE ID = ?",
            (exoplanet_id,),
        ).fetchone()
        # Checks if no row was found
        if exoplanet_query is None:
            return None
        return cls(*exoplanet_query)

    # Takes a cursor and name of an exoplanet
    @classmethod
    def from_name(cls, cur, exoplanet_name):
        # Takes exoplanet_id and finds row with corresponding name
        exoplanet_query = cur.execute(
            "SELECT Name, Type, Diameter, Distance, Material, Gas, Rings, Colour,"
            "Climate, StarType FROM Exoplanets WHERE Name = ?",
            (exoplanet_name,),
        ).fetchone()
        # Checks if no row was found
        if exoplanet_query is None:
            return None
        return cls(*exoplanet_query)

    # Inserts exoplanet object into database
    def commit(self, cur):
        # Makes tuple of all data to insert into SQL statement
        inserted_tuple = (
            self.name,
            self.planet_type,
            self.diameter,
            self.distance,
            self.material,
            self.gas,
            self.rings,
            self.colour,
            self.climate,
            self.star_type,
        )
        # Inserts object data into database and commits it
        cur.execute(
            "INSERT INTO Exoplanets(Name, Type, Diameter, Distance, Material, Gas, Rings, Colour, Climate,"
            "StarType) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            inserted_tuple,
        )
        con.commit()

    # Counts total amount of planet rows in table
    @staticmethod
    def exoplanet_count(cur):
        return cur.execute("SELECT COUNT(*) FROM Exoplanets").fetchone()[0]


# planet = Exoplanet("Earth", "Earth", 12742, 1, "soil", False, 0, "Blue", 20, 'O')

# planet.commit()

# print(cur.execute("SELECT * FROM Exoplanets").fetchone())

# planet2 = Exoplanet.from_id(cur, 1)
# print(planet2)
