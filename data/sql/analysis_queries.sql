-- Total Revenue
SELECT SUM(total_amount) AS total_revenue
FROM retail_sales;

-- Revenue by Product Category
SELECT product_category,
       SUM(total_amount) AS revenue
FROM retail_sales
GROUP BY product_category
ORDER BY revenue DESC;

-- Monthly Revenue Trend
SELECT DATE_FORMAT(date, '%Y-%m') AS month,
       SUM(total_amount) AS monthly_revenue
FROM retail_sales
GROUP BY month
ORDER BY month;

-- Top 5 Customers by Revenue
SELECT customer_id,
       SUM(total_amount) AS total_spent
FROM retail_sales
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 5;

-- Average Basket Size
SELECT AVG(quantity) AS avg_items_per_purchase
FROM retail_sales;
