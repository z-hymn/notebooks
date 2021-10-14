!pip install -U sqlalchemy==1.3.9 
!pip install -U ibm_db_sa 
!pip install -U ipython-sql 
!pip install -U ibm-db 
import ibm_db

%load_ext sql

# Remember the connection string is of the format:
# %sql ibm_db_sa://my-username:my-password@my-hostname:my-port/my-db-name?security=SSL
# Enter the connection string for your Db2 on Cloud database instance below
%sql ibm_db_sa://my-username:40WrMIyhF6BWSAgk@fbd88901-ebdb-4a4f-a32e-9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud:32731/BLUDB?security=SSL
      
%sql select count(*) from chicago_crime_data
%sql SELECT community_area_name, per_capita_income FROM census_data WHERE per_capita_income > 11000 ORDER BY per_capita_income DESC 
%sql select count(percent_aged_under_18_or_over_64) from census_data

%sql select AVG(Safety_Score) AS AVG_SAFETY_SCORE from chicago_public_schools

%sql select community_area_name, percent_households_below_poverty from census_data \
     order by percent_households_below_poverty  desc nulls last limit 5

%sql SELECT community_area_name, hardship_index FROM census_data where \
    hardship_index= (select MAX(hardship_index) from census_data)
