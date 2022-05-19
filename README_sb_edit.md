![](./visualizations_sb/drop_02.png) 
# Group Project: Water Improvement in Tanzania

#### Cody Can, Sb Fuller, Jackie Petersen, Kaleb Tsegaye
---

### Problem Statement

In Tanzania, clean drinking water is accessible for only 55% of the population and improved sanitation is available for only 15% of the population. The median age of the Tanzanian population is only 17.7 years of age, with a life expectancy of 62.6 years of age. Improved sanitation and access to water could vastly improve the life expectancies of Tanzanians.

For our group project we will be focusing on pumps and water points in Tanzania, their functionality, and different metrics that can inform the urgency of their repair. Using a Water Point Mapping System dataset, we created a predictive model for well functionality in Tanzania. We also obtained a collection of datasets from the World Bank Climate Knowledge Portal, The WHO UNICEF JMP Global Database, and the Tanzania Socio-Economic Database in order to produce a greater analysis on the infrastructural and climatological landscape of Tanzania by region. This analysis coupled with our predictive model served to inform next steps for prioritizing investment in some wells over others in order to save lives by bringing about the greatest improvements in utility standards across Tanzania.

Can a model be produced that predicts water point functionality in Tanzania? Can additional information be put into an interactive application for workers in Tanzania to use for dynamic decision making?
<br>
<br>

### Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|

### Summary of Analysis


![ ](./visualizations_sb/geo_wpt_nonfunc.png)
- The above plots show that Mwanza has the highest percentage of non-functional wells.
- Iringa has the lowest percentage of non-functional wells.
<br>

![ ](./visualizations_sb/wtp_nonfunc_per.png)
- The above plots show that Mwanza has the highest percentage of non-functional wells.
- Iringa has the lowest percentage of non-functional wells.
<br>

![ ](./visualizations_sb/precip_region_20.png)
- This plot shows precipitation by region for the past 20 years. 
- Some regions have more erratic variation from year to year than others do. 

![ ](./images_jp/access to water combined.png)
![ ](./images_jp/access to water combined.png)

![ ](./visualizations_sb/pdd_region_func.png)
- This plot singles out encoded region variables with the largest and smallest precipitation ranges from year to year. 
- Regions with less range of precipitation show negative correlation with functionality.
- Regions with more range of precipitation show positive correlation with functionality.

![ ](./visualizations_sb/cmd.png)
- The best performing model had fair performance.
- 79% of all observations are correctly predicted.
- Among predicted positives, 78.6% were correctly predicted.
- Among actual positives, 79.2% were correctly predicted.
- Overall this model dramatically outperformed the baseline (50% accuracy)



### Conclusions and Recommendations
There is no “one size fits all” approach to the needs of Tanzania.

Some regions have much more water availability as precipitation than others while some regions have greater variance from year to year in precipitation than others. Different regions have different infrastuctural demands and capacityies and all of this is pretty dynamic from year to year given all of the non-profit intervention in the area. 

Information is very hard to come by in this region. Information is often incomplete or incongruous, but with the aduncance of data that we were able to dig up, we can confidently recommend that more information, better information collection practice, and greater information transparency in combination with predictive models CAN lead to the greatest improvements in living conditions in Tanzania. 

Since the nature and needs of Tanzania can be so dynamic,  predictive modeling and information transparency can be the best tools for saving lives. 

For this reason we produded an app. This app can be used by on the ground non-profit workers to pay closer attention to dynamic trends in climatological and infrastructural data as it pertains to Tanzania region by region. Accessibility and transparency of information will be key to improving the lives of Tanzanians.

![ ](./visualizations_sb/app1.png)
![ ](./visualizations_sb/app2.png)

