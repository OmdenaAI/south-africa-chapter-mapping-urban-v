# Data Collection

## THE PROJECT GOALS

The AI solution should identify key characteristics of urban vulnerability and generate data layers on them from city-level data.

- open data sources

- extraction of data from imageries, and/or complementary sources.

The analysis could involve the creation of surface maps for each form of vulnerability and aggregating the layers to generate a composite ‘city vulnerability layer’. For useful results, the resolution of the data must be good to enable precise identification of vulnerable locations within the city fabric. Identification of locations with multiple vulnerabilities may guide decision-makers on deteriorating locations, especially when monitoring is done at a consistent temporal scale.

### Data Sources

We started with data from SAPS that was collated yearly from 2005 to 2015.  
We then found the same data from SAPS that were collated monthly from 2016 to 2021.  
We had a leaders meeting and decided to work with the monthly data sources.  
  
The data included the following features that we could easily extract:

- 'station' - Police station where crime was reported
- 'province' - The province where the crime was committed
- 'district' - The district where the crime was committed
- 'crime_category' - The type of crime committed
- 'date' - The month the crime was committed in
- 'number_of_crimes' - The number of crimes committed in the month

We then collected latitude and longitude of the stations and added two more feature:

- 'latitude'
- 'longitude'

We discussed supplementary data to try and identify any correlations between the crimes and any other features. We decided on the following:

- Weather data
- Unemployment data
- Political data
- Poverty data
- Famine data

## Road Blocks

We attempted to get monthly data from 2005 to 2016 however we never received any reply's from SAPs.  
This may come in time.  
Open source supplementary data was near on impossible to find. What was out there was either incomplete or to far back in history.  
We eventually found some open source data for weather that includes, temp, rain, wind, precipitation, sunset and sunrise, snow, and reference evapotranspiration.  
This was found late on and we are extracting this but again will take time.  
South Africa has proven to be a difficult country to find open source data, however they are actively working on this, we feel as time goes on this will vastly improve.
