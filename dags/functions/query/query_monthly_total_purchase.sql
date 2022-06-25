INSERT INTO presentation_monthly_total_purchase_per_product (product_category_name, metrics_date, metrics_value) (
    SELECT product_category_name, DATE_TRUNC('month', to_date(order_purchase_timestamp, 'YYYY-MM-DD')) as purchase_date, COUNT(product_category_name) as total 
    FROM olist_orders_dataset as oo JOIN olist_order_items_dataset as ooi
    ON oo.order_id=ooi.order_id 
    JOIN olist_products_dataset as op
    ON ooi.product_id=op.product_id 
    WHERE product_category_name is not null 
    GROUP BY 1, 2
) 
ON CONFLICT (product_category_name, metrics_date) DO UPDATE 
SET metrics_value = EXCLUDED.metrics_value