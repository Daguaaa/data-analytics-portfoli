-- Database Schema for Real Estate Market Intelligence


CREATE TABLE IF NOT EXISTS mn_homes (
    id SERIAL PRIMARY KEY,
    scan_date DATE,
    city TEXT,
    price INTEGER,
    beds FLOAT,
    baths FLOAT,
    sqft INTEGER,
    address TEXT,
    price_per_sqft FLOAT,
    flip_potential BOOLEAN
);

-- Schema Migration: Added to track seller motivation
ALTER TABLE mn_homes ADD COLUMN days_on_market INTEGER;