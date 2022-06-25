CREATE TABLE IF NOT EXISTS presentation_monthly_total_purchase_per_product (
    product_category_name TEXT,
    metrics_date TIMESTAMP,
    metrics_value INTEGER,
    PRIMARY KEY(product_category_name, metrics_date)
)