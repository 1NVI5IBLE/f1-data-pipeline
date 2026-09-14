SELECT
    id AS race_result_id,
    season,
    round,
    driver_id,
    constructor_id,
    grid_position,
    finish_position,
    points,
    laps,
    status
FROM {{ ref('stg_race_reesults')}}