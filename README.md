# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Group Project: Tanzania Waterpoint Repair & Analysis

#### Cody Can, Sb Fuller, Jackie Petersen, Kaleb Tsegaye
---

### Problem Statement

For our group project we will be focusing on pumps and water points in Tanzania, their functionality, and different metrics that can inform the urgency of their repair. Using a Water Point Mapping System dataset, we will create a predictive model for well functionality in Tanzania. We have also obtained a collection of datasets from the World Bank Climate Knowledge Portal, The WHO UNICEF JMP Global Database, and the Tanzania Socio-Economic Database in order to produce a greater analysis on the infrastructural and climatological landscape of Tanzania by region. This analysis coupled with our predictive model will serve to inform next steps for prioritizing investment in some wells over others in order to save lives by bringing about the greatest improvements in utility standards across Tanzania.

### Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**id**|*int64*|Pump_it_Up_Data_Training_set_values & Pump_it_Up_Data_Training_set_labels|Row id|
|**amount_tsh**|*float64*|Pump_it_Up_Data_Training_set_values|Total static head (amount water available to waterpoint)|
|**date_recorded**|*object*|Pump_it_Up_Data_Training_set_values|The date the row was entered|
|**funder**|*object*|Pump_it_Up_Data_Training_set_values|Who funded the well|
|**gps_height**|*int64*|Pump_it_Up_Data_Training_set_values|Altitude of the well|
|**installer**|*object*|Pump_it_Up_Data_Training_set_values|Organization that installed the well|
|**longitude**|*float64*|Pump_it_Up_Data_Training_set_values|GPS coordinate|
|**latitude**|*float64*|Pump_it_Up_Data_Training_set_values|GPS coordinate|
|**wpt_name**|*object*|Pump_it_Up_Data_Training_set_values|Name of the waterpoint if there is one|
|**num_private**|*int64*|Pump_it_Up_Data_Training_set_values||
|**basin**|*object*|Pump_it_Up_Data_Training_set_values|Geographic water basin|
|**subvillage**|*object*|Pump_it_Up_Data_Training_set_values|Geographic location|
|**region**|*object*|Pump_it_Up_Data_Training_set_values|Geographic location|
|**region_code**|*int64*|Pump_it_Up_Data_Training_set_values|Geographic location (coded)|
|**district_code**|*int64*|Pump_it_Up_Data_Training_set_values|Geographic location (coded)|
|**lga**|*object*|Pump_it_Up_Data_Training_set_values|Geographic location|
|**ward**|*object*|Pump_it_Up_Data_Training_set_values|Geographic location|
|**population**|*int64*|Pump_it_Up_Data_Training_set_values|Population around the well|
|**public_meeting**|*object*|Pump_it_Up_Data_Training_set_values|True/False|
|**recorded_by**|*object*|Pump_it_Up_Data_Training_set_values|Group entering this row of data|
|**scheme_management**|*object*|Pump_it_Up_Data_Training_set_values|Who operates the waterpoint|
|**scheme_name**|*object*|Pump_it_Up_Data_Training_set_values|Who operates the waterpoint|
|**permit**|*object*|Pump_it_Up_Data_Training_set_values|If the waterpoint is permitted|
|**construction_year**|*int64*|Pump_it_Up_Data_Training_set_values|Year the waterpoint was constructed|
|**extraction_type**|*object*|Pump_it_Up_Data_Training_set_values|he kind of extraction the waterpoint uses|
|**extraction_type_group**|*object*|Pump_it_Up_Data_Training_set_values|he kind of extraction the waterpoint uses|
|**extraction_type_class**|*object*|Pump_it_Up_Data_Training_set_values|The kind of extraction the waterpoint uses|
|**management**|*object*|Pump_it_Up_Data_Training_set_values|How the waterpoint is managed|
|**management_group**|*object*|Pump_it_Up_Data_Training_set_values|How the waterpoint is managed|
|**payment**|*object*|Pump_it_Up_Data_Training_set_values|What the water costs|
|**payment_type**|*object*|Pump_it_Up_Data_Training_set_values|What the water costs|
|**water_quality**|*object*|Pump_it_Up_Data_Training_set_values|The quality of the water|
|**quality_group**|*object*|Pump_it_Up_Data_Training_set_values|The quality of the water|
|**quantity**|*object*|Pump_it_Up_Data_Training_set_values|The quantity of water|
|**quantity_group**|*object*|Pump_it_Up_Data_Training_set_values|The quantity of water|
|**source**|*object*|Pump_it_Up_Data_Training_set_values|The source of the water|
|**source_type**|*object*|Pump_it_Up_Data_Training_set_values|The source of the water|
|**source_class**|*object*|Pump_it_Up_Data_Training_set_values|The source of the water|
|**waterpoint_type**|*object*|Pump_it_Up_Data_Training_set_values|The kind of waterpoint|
|**waterpoint_type_group**|*object*|Pump_it_Up_Data_Training_set_values|The kind of waterpoint|
|**status_group**|*object*|Pump_it_Up_Data_Training_set_labels|Functionality of the well|


### Summary of Analysis



### Conclusions and Recommendations
