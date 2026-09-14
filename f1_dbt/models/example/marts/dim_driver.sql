SELECT DISTINCT
    driver_id,
    driver_name
FROM {{ ref('stg_race_reesults') }}