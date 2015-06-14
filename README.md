## Missions Forecast

 Using data from http://www.usaid.gov/work-usaid/get-grant-or-contract/business-forecast
 loader.py contains load_data which will load a slightly altered version
 of the csv file from that website.

This django project includes an app than displays the missions forecast in a readable format organized by Country, NAICS code, and A&A Specialist.

# To-do

- add ability to sort values on pages
- add ability to sort by award amount range
- add way to tag 'relevant' items for the organization
- add display page for 'relevant' items
- add way to compare new items against old, keep
  'relevant' and 'irrelevant' items in their categories
  if altered
