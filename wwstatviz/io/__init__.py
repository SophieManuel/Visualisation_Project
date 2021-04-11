# io = input/output
import os

# Total population by sex, annually from 1950 to 2100 : 
# PopMale, PopFemale, PopTotal, PopDensity
# use differents variants

url_allvar = "https://population.un.org/wpp/Download/Files/1_Indicators%20(Standard)/CSV_FILES/WPP2019_TotalPopulationBySex.csv"
path_target_allvar = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "df_TotalPopbySex_allvar.csv")

# Population by 5-year age groups, annually from 1950 to 2100 :

url_agesex = "https://population.un.org/wpp/Download/Files/1_Indicators%20(Standard)/CSV_FILES/WPP2019_PopulationByAgeSex_Medium.csv"
path_target_agesex = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "df_TotalPopbyAgeSex.csv")

# Fertility Indicators

url_fertility = "https://population.un.org/wpp/Download/Files/1_Indicators%20(Standard)/CSV_FILES/WPP2019_Fertility_by_Age.csv"
path_target_fertility = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "df_FertilityAge.csv")

# A lot of various indicators on periods of 5 years.

url_indicators= "https://population.un.org/wpp/Download/Files/1_Indicators%20(Standard)/CSV_FILES/WPP2019_Period_Indicators_Medium.csv"
path_target_indicators = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "df_Indicators.csv")

# Indicators about life

url_life = "https://population.un.org/wpp/Download/Files/1_Indicators%20(Standard)/CSV_FILES/WPP2019_Life_Table_Medium.csv"
path_target_life = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", "df_Life_Table.csv")
