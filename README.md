This repository exclusively contains the documentation and resources for my Technical Technique Presentation, "Handling Nulls in Pandas." This presentation is an integral part of the Team ETL initiative and is specifically designed for individuals who intend to enhance their data preprocessing skills and improve their data quality. 
## Handling Nulls in Pandas
![image](https://github.com/MarianOforiYeboah/Capstone_2024/assets/149170814/053e0605-aabd-47d4-a23e-bf613515168e)


<div>
	<h1><img src="Img/panda.jpg" width="100" /> Why do datasets have nulls?</h1>
</div>
<br>

Null values typically indicate missing or unknown data. They can occur during data collection, transfer, or due to transformations applied to the data. It’s essential to handle nulls appropriately during data analysis to avoid errors or misleading results

## Detection of Null Values
In order to work with null values, you must first identify them. Pandas offers two functions for this purpose:

- isnull(): This function returns a DataFrame or Series that indicates whether each value is null.

- notnull(): This function is the opposite of isnull(). It returns True for non-null values.

##  Ways of handling nulls in pandas
Dealing with null values is a frequent task when working with data in Pandas. Various methods can be used to handle nulls, including dropping them, replacing null values, and interpolating. In this context, we'll discuss two  ways to handle nulls: dropping and replacing.
