SELECT DISTINCT
    season,
    round,
    race_name,
    race_date
FROM {{ ref("stg_race_reesults") }}