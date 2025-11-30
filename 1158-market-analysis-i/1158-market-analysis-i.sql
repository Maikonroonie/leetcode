/* Write your T-SQL query statement below */

/* Write your T-SQL query statement below */
SELECT u.user_id AS buyer_id, u.join_date,
    SUM(
        CASE
        WHEN YEAR(o.order_date) = 2019 THEN 1
        ELSE 0 
        END
        ) AS orders_in_2019
FROM Users u LEFT JOIN Orders o
ON u.user_id = o.buyer_id
GROUP BY u.user_id, u.join_date;

/*
SELECT 
    u.user_id AS buyer_id,
    u.join_date,
    ISNULL(o.cnt, 0) AS orders_in_2019  -- Zamieniamy NULL na 0
FROM Users u
LEFT JOIN (
    SELECT buyer_id, COUNT(order_id) as cnt
    FROM Orders
    WHERE YEAR(order_date) = 2019       -- Filtrujemy tylko rok 2019
    GROUP BY buyer_id                   -- Grupujemy po KLIENCIE, nie dacie
) o ON u.user_id = o.buyer_id;
*/