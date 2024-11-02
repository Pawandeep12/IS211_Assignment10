CREATE TABLE artists (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE albums (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    artist_id INTEGER,
    FOREIGN KEY (artist_id) REFERENCES artists(id)
);

CREATE TABLE songs (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    track_number INTEGER,
    duration INTEGER,
    album_id INTEGER,
    FOREIGN KEY (album_id) REFERENCES albums(id)
);
