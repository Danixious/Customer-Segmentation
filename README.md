# 📊 Problem Definition

## Businesses want to group customers by their purchasing behavior.

## Goal: Identify segments like high-value, frequent buyers, occasional buyers, etc.

## This helps in targeted marketing, personalized offers, and retention strategies.




## EDA
DataFrame 1 (Orders by Country):
          Country  total_orders
0  United Kingdom        356728
1         Germany          9480
2          France          8475
3            EIRE          7475
4           Spain          2528

DataFrame 2 (Top 10 Products):
                          Description  total_quantity
0   WORLD WAR 2 GLIDERS ASSTD DESIGNS           53119
1             JUMBO BAG RED RETROSPOT           44963
2       ASSORTED COLOUR BIRD ORNAMENT           35215
3  WHITE HANGING HEART T-LIGHT HOLDER           34128
4     PACK OF 72 RETROSPOT CAKE CASES           33386

DataFrame 3 (Customer Revenue):
   CustomerID    revenue
0     14646.0  279489.02
1     18102.0  256438.49
2     17450.0  187322.17
3     14911.0  132458.73
4     12415.0  123725.45


## RFM
   CustomerID Recency  Frequency  Monetary
0     12346.0    None          2      0.00
1     12347.0    None          7   4310.00
2     12348.0    None          4   1797.24
3     12349.0    None          1   1757.55
4     12350.0    None          1    334.40