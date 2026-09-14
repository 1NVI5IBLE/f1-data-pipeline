CREATE TABLE IF NOT EXISTS race_results (
    id SERIAL PRIMARY KEY,
    season INTEGER,
    round INTEGER,
    race_name VARCHAR(100),
    race_date DATE,
    driver_id VARCHAR(50),
    driver_name VARCHAR(100),
    constructor_id VARCHAR(50),
    constructor_name VARCHAR(100),
    grid_position INTEGER,
    finish_position INTEGER,
    points DECIMAL(5, 2),
    laps INTEGER,
    status VARCHAR(100),

    CONSTRAINT unique_race_driver
    UNIQUE (season, round, driver_id)
);