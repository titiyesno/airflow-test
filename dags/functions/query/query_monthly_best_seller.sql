INSERT INTO presentation_monthly_best_seller_products (product_category_name, metrics_date, metrics_value) (
    SELECT product_category_name, metrics_date, metrics_value 
    FROM (
        SELECT product_category_name, metrics_date, metrics_value, 
        ROW_NUMBER() OVER (PARTITION BY metrics_date ORDER BY metrics_value) AS rn 
        FROM presentation_monthly_total_purchase_per_product
    ) t WHERE rn <= 10
) 
ON CONFLICT (product_category_name, metrics_date) DO UPDATE 
SET metrics_value = EXCLUDED.metrics_value