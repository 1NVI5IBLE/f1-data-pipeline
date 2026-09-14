SELECT DISTINCT
    constructor_id,
    constructor_name
FROM {{ ref('stg_race_reesults') }}