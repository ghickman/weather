CREATE TABLE effects (
        flood_magnitude_index DECIMAL(4,2),
        severity DECIMAL(3,1),
        deaths INTEGER,
        displaced INTEGER,
        damage_usd FLOAT,
        main_cause VARCHAR(80),
        id INTEGER UNIQUE
);

CREATE TABLE locations (
        centroid POINT,
        sq_km DECIMAL(8,3),
        country VARCHAR(80),
        id INTEGER REFERENCES effects (id)
);

CREATE TABLE dates (
        began DATE,
        ended DATE,
        days SMALLINT CONSTRAINT valid_dates CHECK ((ended-began+1) = days),
        id INTEGER REFERENCES effects (id)
);
