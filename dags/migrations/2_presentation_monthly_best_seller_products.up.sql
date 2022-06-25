CREATE TABLE IF NOT EXISTS presentation_monthly_best_seller_products (
    product_category_name TEXT,
    metrics_date TIMESTAMP,
    metrics_value INTEGER,
    PRIMARY KEY(product_category_name, metrics_date)
)