-- Query n_people younger than 30yo earning more than 50k
SELECT COUNT(*) [Numero di persone]
FROM records
WHERE over_50k = 1
  AND age < 30;

-- Avg capital gain per category
SELECT w.name            [Categoria lavorativa]
     , AVG(capital_gain) [Guadagno capitale medio]
FROM records r
         JOIN workclasses w on r.workclass_id = w.id
GROUP BY w.name;

-- Unnormalized records
SELECT *
FROM records r
         JOIN countries c on r.country_id = c.id
         JOIN education_levels el on r.education_level_id = el.id
         JOIN marital_statuses ms on r.marital_status_id = ms.id
         JOIN occupations o on o.id = r.occupation_id
         JOIN races r2 on r.race_id = r2.id
         JOIN relationships r3 on r.relationship_id = r3.id
         JOIN sexes s on r.sex_id = s.id
         JOIN workclasses w on r.workclass_id = w.id;

-- Aggregated Stats query
-- E.g.:
-- aggregationType = 'age'
-- aggregationValue = 30
SELECT 'age'                                           [aggregationType]
     , 30                                              [aggregationFilter]
     , SUM(r.capital_gain)                             [capital_gain_sum]
     , AVG(r.capital_gain)                             [capital_gain_avg]
     , SUM(r.capital_loss)                             [capital_loss_sum]
     , AVG(r.capital_loss)                             [capital_loss_avg]
     , SUM(CASE WHEN r.over_50k = 1 THEN 1 ELSE 0 END) [over_50k_count]
     , SUM(CASE WHEN r.over_50k = 0 THEN 1 ELSE 0 END) [under_50k_count]
FROM records r
WHERE r.'age' = 30;