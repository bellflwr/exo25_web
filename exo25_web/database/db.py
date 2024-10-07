from dataclasses import dataclass
import sqlite3
from flask import g

# con = sqlite3.connect("../../Exoplanets.db")
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
    id: int | None
    name: str
    diameter: float
    distance: float
    gas: bool
    height_mult: float
    erosion: int
    frequency: float
    amplitude: float
    scale: float
    colour: str
    star_type: str

    # Takes a cursor and id of a row/exoplanet
    @classmethod
    def from_id(cls, cur, exoplanet_id):
        # Takes exoplanet_id and finds row with corresponding ID
        exoplanet_query = cur.execute(
            "SELECT * FROM Exoplanets WHERE ID = ?",
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
            "SELECT * FROM Exoplanets WHERE Name = ?",
            (exoplanet_name,),
        ).fetchone()
        # Checks if no row was found
        if exoplanet_query is None:
            return None
        return cls(*exoplanet_query)

    # Inserts exoplanet object into database
    def write(self, cur):
        # Makes tuple of all data to insert into SQL statement
        inserted_tuple = (
            self.name,
            self.diameter,
            self.distance,
            self.gas,
            self.height_mult,
            self.erosion,
            self.frequency,
            self.amplitude,
            self.scale,
            self.colour,
            self.star_type,
        )
        # Inserts object data into database and commits it
        cur.execute(
            "INSERT INTO Exoplanets(Name, Diameter, Distance, Gas, HeightMultiplier, Erosion, Frequency, Amplitude,"
            " Scale, Colour, StarType) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            inserted_tuple,
        )

        return cur.lastrowid

    # Searches for an exoplanet with the beginning part of entered string
    @classmethod
    def search(cls, cur, name_snip):
        # Finds exoplanets with names beginning with the name snippet
        exoplanet_query = cur.execute(
            "SELECT * FROM Exoplanets WHERE Name LIKE ?", (name_snip + "%",)
        ).fetchall()
        exoplanet_object_list = []
        for i in range(len(exoplanet_query)):
            exoplanet_object_list.append(cls(*exoplanet_query[i]))
        return exoplanet_object_list

    # Counts total amount of planet rows in table
    @staticmethod
    def exoplanet_count(cur):
        return cur.execute("SELECT COUNT(*) FROM Exoplanets").fetchone()[0]


# planet = Exoplanet(-1, "Earth", 12047, 1, False, 2.0, 2, 1.0, 1.0, 1.0, "Blue", "G")

# planet.write(cur)

# con.commit()

# print(cur.execute("SELECT * FROM Exoplanets").fetchone())

# planet2 = Exoplanet.from_id(cur, 1)
# print(planet2)

# print(Exoplanet.search(cur, "E"))
