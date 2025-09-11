
# IN PROGRESS ------- 🚧🚧🚧🚧🚧🚧🚧


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
## RFM SCaled
D:\Customer Segmentation\notebooks>python feature_eng.py
<bound method NDFrame.head of       CustomerID    LastPurchaseDate  Frequency  Monetary  Recency
0        12346.0 2011-01-18 10:17:00          2      0.00      326
1        12347.0 2011-08-02 08:48:00          7   4310.00      130
2        12348.0 2011-09-25 13:13:00          4   1797.24       75
3        12349.0 2011-11-21 09:51:00          1   1757.55       19
4        12350.0 2011-02-02 16:01:00          1    334.40      310
...          ...                 ...        ...       ...      ...
4367     18280.0 2011-03-07 09:52:00          1    180.60      278
4368     18281.0 2011-06-12 10:53:00          1     80.82      181
4369     18282.0 2011-08-09 15:10:00          3    176.60      122
4370     18283.0 2011-09-05 12:35:00         16   2045.53       95
4371     18287.0 2011-05-22 10:39:00          3   1837.28      202

[4372 rows x 5 columns]>
[[ 2.00422961 -0.32936215 -0.23041952]
 [-0.09470421  0.20610242  0.29405454]
 [-0.68369075 -0.11517632 -0.01171748]
 [-1.28338612 -0.43645506 -0.01654727]
 [ 1.83288807 -0.43645506 -0.18972715]]



# Silhoutte analysis
k = 2,silhouette = 0.9864
k = 3,silhouette = 0.9632
k = 4,silhouette = 0.8844
k = 5,silhouette = 0.8160
k = 6,silhouette = 0.7776
k = 7,silhouette = 0.7737
k = 8,silhouette = 0.7237
k = 9,silhouette = 0.6773
k = 10,silhouette = 0.6753
Best k by silhouette score: 2
RFM table updated with clusters
   CustomerID     LastPurchaseDate  Frequency  Monetary  Recency  Cluster
0     12346.0  2011-01-18 10:17:00          2      0.00      326        0
1     12347.0  2011-08-02 08:48:00          7   4310.00      130        0
2     12348.0  2011-09-25 13:13:00          4   1797.24       75        0
3     12349.0  2011-11-21 09:51:00          1   1757.55       19        0
4     12350.0  2011-02-02 16:01:00          1    334.40      310        0
📊 Cluster Profiles (averages):
         Recency  Frequency   Monetary  Count  Recency_norm  Frequency_norm  Monetary_norm
Cluster
0         138.91       4.96    1645.87   4366           1.0             0.0            0.0
1          90.67      89.00  182108.08      6           0.0             1.0            1.0

Final Segmented Data Sample:
   CustomerID     LastPurchaseDate  Frequency  Monetary  Recency  Cluster    Segment
0     12346.0  2011-01-18 10:17:00          2      0.00      326        0  💤 At Risk
1     12347.0  2011-08-02 08:48:00          7   4310.00      130        0  💤 At Risk
2     12348.0  2011-09-25 13:13:00          4   1797.24       75        0  💤 At Risk
3     12349.0  2011-11-21 09:51:00          1   1757.55       19        0  💤 At Risk
4     12350.0  2011-02-02 16:01:00          1    334.40      310        0  💤 At Risk