# Climate Analysis and App Creation

### Objective:  Conduct a climate analysis to help plan for a trip to Honolulu, Hawaii.

**Step 1:** Conduct a climate analysis and data exploration with an SQL database, analyzing and visualizing the data using Pandas and matplotlib.
* A precipitation analysis was conducted using the most recent 12 months of precipitation data; summary statistics were calculated and plotted.
  - The average precipitation over the 12 month period was 0.177 inches with a maximum rainfall amount of 6.7 inches.

   ![Image1](https://github.com/bking3372/Climate-Analysis-and-App-Creation/blob/master/images/describe.png)
   ![Image2](https://github.com/bking3372/Climate-Analysis-and-App-Creation/blob/master/images/P12M%20Precipitation.PNG)

* A weather station analysis was performed to find the total number of weather stations, the most active of these stations, and temperature observations (most recent 12 months)
   for the most active weather station.
   -  Of the nine weather stations, Station USC00519281 is the most active station with an average temperature of 71.7.
   
   ![Image3](https://github.com/bking3372/Climate-Analysis-and-App-Creation/blob/master/images/Temp%20Histogram.PNG)
   

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
   -  The average temperature in June is 74.9 degrees and the average temperature in December is 71.0.  An independent t-test to compare these monthly averages showed there is a significant difference.

*  Pick a time period to travel to Hawaii and determine the minimum, maximum, and average temperatures for the previous year period, creating a bar chart visualization.

   ![Image4](https://github.com/bking3372/Climate-Analysis-and-App-Creation/blob/master/images/Trip%20Avg%20Temp.PNG)

*  Using the same dates, determine the average daily rainfall for the previous year period for each weather station.

   ![Image5](https://github.com/bking3372/Climate-Analysis-and-App-Creation/blob/master/images/Precip_Station.PNG)

*  Determine the daily normals (minimum, maximum, and average temperatures) using all the previous years corresponding to the selected trip dates.

   ![Image6](https://github.com/bking3372/Climate-Analysis-and-App-Creation/blob/master/images/Daily%20Normals.PNG)


