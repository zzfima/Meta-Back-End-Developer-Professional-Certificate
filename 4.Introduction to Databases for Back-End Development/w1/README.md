# subsets of SQL

- DDL - Data Definition Language
- DML - Data Manipulation Language
- DQL - Data Query Language
- DCL - Data Control Language.

## SQL syntax

## DDL

CREATE DATABASE store.db;

sqlite3:

    $sqlite3 store.db
    .database
    .q

CREATE TABLE contacts;

sqlite3:

    CREATE TABLE contacts (
        contact_id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        phone TEXT NOT NULL UNIQUE
    );

## DML

INSERT INTO...

sqlite3:

    INSERT INTO contacts (first_name, last_name, email, phone)
    VALUES
        ('Alex', 'Molotov', 'alex@cmp.com', '972 546694939'),
        ('Nick', 'Xu', 'xu@cmp.com', '972 549378566'),
        ('Valery', 'Jessenin', 'jes@cmp.com', '972 508475748');

UPDATE contacts

sqlite3:

    UPDATE contacts
    SET first_name = 'Sergey'
    WHERE contact_id = 2;
