CREATE TABLE singer (
    name varchar(255) NOT NULL PRIMARY KEY,
    debut_year date,
    created_at timestamp,
    updated_at timestamp
);

CREATE TABLE album (
    name varchar(255) NOT NULL PRIMARY KEY,
    singer varchar(255) NOT NULL references singer(name),
    release_date date,
    created_at timestamp,
    updated_at timestamp
);

CREATE TABLE music (
    id SERIAL PRIMARY KEY,
    song varchar(255) NOT NULL,
    singer varchar(255) NOT NULL references singer(name),
    album varchar(255) NOT NULL references album(name),
    album_no SMALLINT,
    song_length INT,
    created_at timestamp,
    updated_at timestamp
);