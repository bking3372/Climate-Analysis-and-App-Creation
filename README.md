# Climate Analysis and App Creation

### Objective:  Conduct a climate analysis to help plan for a trip to Honolulu, Hawaii.

**Step 1:** Conduct a climate analysis and data exploration with an SQL database, analyzing and visualizing the data using Pandas and matplotlib.
* A precipitation analysis was conducted using the most recent 12 months of precipitation data; summary statistics were calculated and plotted.

   ![Image1](https://github.com/bking3372/Climate-Analysis-and-App-Creation/blob/master/images/describe.png)

* A weather station analysis was performed to find the total number of weather stations, the most active of these stations, and temperature observations (most recent 12 months)
   for the most active weather station.
   
   ![Image2](https://github.com/bking3372/Climate-Analysis-and-App-Creation/blob/master/images/P12M%20Precipitation.PNG)

**Step 2:**  Design a climate app using a Flask API based on the data collected in Step 1.
* The following routes were created in the Flask API app:
   * Home - a list all available routes in the app
   * Precipitation - precipitation results for past 12 months
   * Stations - a list of all weather stations
   * Tobs - temperature observations (past 12 months) for the most active weather station
   * Start Date - list the minimum, maximum, and average temperature for all dates greater than and equal to a specified start date
   * Start/End Date - list the minimum, maximum, and average temperature for all dates between (inclusive) of a specified start date and specified end date
   
**Step 3:**  Conduct additional analyses to explore temperatures in Hawaii including:
*  Determine if there is a meaningful difference between the temperatures in June and December.
*  Pick a time period to travel to Hawaii and determine the minimum, maximum, and average temperatures for the previous year period, creating a bar chart visualization.

   ![Image3](https://github.com/bking3372/Climate-Analysis-and-App-Creation/blob/master/images/Trip%20Avg%20Temp.PNG)

*  Using the same dates, determine the average daily rainfall for the previous year period.
*  Determine the daily normals (minimum, maximum, and average temperatures) using all the previous years corresponding to the selected trip dates.

   ![Image5](https://github.com/bking3372/Climate-Analysis-and-App-Creation/blob/master/images/Daily%20Normals.PNG)


