CREATE user vova WITH PASSWORD '123456';

CREATE DATABASE app_db;
GRANT ALL PRIVILEGES ON DATABASE app_db TO vova;

USE app_db;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
	email VARCHAR (255),
	fam VARCHAR (255) NOT NULL,
	name VARCHAR (255) NOT NULL,
	otc VARCHAR (255),
	phone VARCHAR (255) NOT NULL,
                  );

CREATE TABLE coords (
    id SERIAL PRIMARY KEY,
	latitude REAL NOT NULL,
	longitude REAL NOT NULL,
	height INTEGER NOT NULL,
                  );

CREATE TABLE levels (
    id SERIAL PRIMARY KEY,
	winter VARCHAR (255),
	summer VARCHAR (255),
	autumn VARCHAR (255),
	spring VARCHAR (255),
                  );

CREATE TABLE images (
    id SERIAL PRIMARY KEY,
	data VARCHAR (255) NOT NULL,
	title VARCHAR (255) NOT NULL,
                  );

CREATE TABLE data (
    id SERIAL PRIMARY KEY,
	beauty_title VARCHAR (255) NOT NULL,
	title VARCHAR (255) NOT NULL,
	other_titles VARCHAR (255) NOT NULL,
	connect VARCHAR (2000) NOT NULL,
    add_time timestamp NOT NULL,
	user_id INTEGER NOT NULL REFERENCES users,
	coords_id INTEGER NOT NULL REFERENCES coords,
	level_id INTEGER NOT NULL REFERENCES levels,
	images_id INTEGER NOT NULL REFERENCES images
                  );
