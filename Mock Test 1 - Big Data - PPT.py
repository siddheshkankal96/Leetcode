# 1. Write a PySpark code to read a CSV file named "employees.csv" containing 
# following columns: "employee_id", "name", "age", "department". Display the top 10 records from the DataFrame.

from pyspark.sql import SparkSession
from pyspark.sql.types import *
spark = SparkSession.builder().appName("mocktest").getOrCreate()
df = spark.read.csv("/employees.csv")
# df.printSchema()
df1 = spark.read.options(header='True',inferSchema='True',delimiter=',') \
  .csv("/employees.csv")

df2 = spark.read.csv("/employees.csv",header='True',inferSchema='True',delimiter=',')


schema = StructType([ \
      StructField("employee_id",IntegerType(),True), \
      StructField("name",StringType(),True), \
      StructField("age",IntegerType(),True), \
      StructField("department",StringType(),True) 
      ])
df_with_schema = spark.read.format("csv") \
      .option("header", True) \
      .schema(schema) \
      .load("/employees.csv")
      
      
df_with_schema.show(10,truncate= False)

# 2.  Given a PySpark DataFrame named "sales_data" with columns "product_name" and 
# "revenue", write a code to calculate the total revenue for each product and display the result in descending order.


total_revenue_df  = sales_data.groupBy("product_name") \
    .agg(sum("revenue").alias("total_revenue")) \
    .orderBy(col("total_revenue").desc()) \
    .show(truncate=False)
    
# Write a PySpark code to read a JSON file named "students.json" containing student records with the following schema: "name" (string), 
# "age" (integer), "grade" (string). Filter the DataFrame to include only students whose age is greater than 18.

schema = StructType([ \
      StructField("name",StringType(),True), \
      StructField("age",IntegerType(),True), \
      StructField("grade",StringType(),True) 
      ])

df_with_schema = spark.read.schema(schema) \
        .json("/students.json",multiline = True)

df_with_schema.printSchema()
df_with_schema.show()


from pyspark.sql.functions import col
df_with_schema.filter(col("age") > 18) \
    .show(truncate=False) 

 
df_with_schema.filter("age > 18") \
    .show(truncate=False) 


# 4. Consider a PySpark DataFrame named "transactions" with columns "transaction_id", 
# "user_id", and "amount". Write a code to calculate the average transaction amount for each user and display the result.

transactions.groupBy("user_id") \
    .agg(avg("amount").alias("average_transaction_amount")) \
    .show(truncate=False)
    

# 5. Given a PySpark DataFrame named "logs" with columns "timestamp" (timestamp) and "event" (string),
# write a code to count the number of events that occurred in each hour and display the result sorted by the hour.
    
logs2 = logs.select(col("timestamp"),hour(col("timestamp")).alias("hour"),col("event"))

logs2.groupBy("hour") \
    .agg(count(*).alias("total_number_of_events_hourly")) \
    .sort('hour')\
    .show(truncate=False)

# 6.  Retrieve all the customers from the "Customers" table whose age is greater than 25 and have made at least one purchase.

select customer_id,name from Customers where age > 25  group by customer_id,name having count(purchase) >= 1;


# 7. Find the total number of orders placed by each customer and display the results in descending order of the number of orders.

select customer_id,count(orders) as number_of_orders from Customers group by customer_id  order by number_of_orders desc;

# 8. Retrieve the names of all products that are currently out of stock from the "Products" table.

select Product_name from Products where availability = 0;

# 9. Calculate the average price of all products in each category and display the results along with the category name.

select  category,avg(price) from Products group by category;

# 10. Retrieve the top 5 customers who have spent the highest total amount on purchases.

select customer_name,sum(amount) as  total_amount_on_purchases from Customers group by customer_name order by total_amount_on_purchases desc limit 5;




    
