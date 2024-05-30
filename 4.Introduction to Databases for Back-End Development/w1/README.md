# subsets of SQL

- DDL - Data Definition Language
- DML - Data Manipulation Language
- DQL - Data Query Language
- DCL - Data Control Language.

## SQL syntax

## DDL

CREATE DATABASE

sqlite3:

    $sqlite3 store.db
    .database
    .q

CREATE TABLE

sqlite3:

    CREATE TABLE contacts (
        contact_id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        phone TEXT NOT NULL UNIQUE);

DROP TABLE

sqlite3:

    DROP TABLE contacts;

ALTER TABLE - rename

sqlite3:

    ALTER TABLE contacts
    RENAME TO myConatact;

ALTER TABLE - add column

sqlite3:

    ALTER TABLE contacts
    ADD COLUMN age INTEGER;

TRUNCATE TABLE - remove all records

sqlite3:

    TRUNCATE TABLE contacts;

## DML

INSERT

sqlite3:

    INSERT INTO contacts (first_name, last_name, email, phone)
    VALUES
        ('Alex', 'Molotov', 'alex@cmp.com', '972 546694939'),
        ('Nick', 'Xu', 'xu@cmp.com', '972 549378566'),
        ('Valery', 'Jessenin', 'jes@cmp.com', '972 508475748');

UPDATE

sqlite3:

    UPDATE contacts
    SET first_name = 'Sergey'
    WHERE contact_id = 2;

DELETE

sqlite3:

    DELETE FROM contacts
    WHERE contact_id = 2;

## DQL

SELECT

sqlite3:

    SELECT last_name, email
    FROM contacts;

SHOW TABLES

sqlite3:

    .tables
