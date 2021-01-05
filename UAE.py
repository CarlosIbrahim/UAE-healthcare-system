import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from PIL import Image

st.set_page_config(layout="wide")

#Read the data of the deaths between the years 2002nand the year 2008
df2 = pd.read_csv('distribution-of-deaths-by-cause-of-death-sex-nationality-and-medical-district-2002.csv')
df3 = pd.read_csv('distribution-of-deaths-by-cause-of-death-sex-nationality-and-medical-district-2003.csv')
df4 = pd.read_csv('distribution-of-deaths-by-cause-of-death-sex-nationality-and-medical-district-2004.csv')
df5 = pd.read_csv('distribution-of-deaths-by-cause-of-death-sex-nationality-and-medical-district-2005.csv')
df6 = pd.read_csv('distribution-of-deaths-by-cause-of-death-sex-nationality-and-medical-district-2006.csv')
df7 = pd.read_csv('distribution-of-deaths-by-cause-of-death-sex-nationality-and-medical-district-2007.csv')
df8 = pd.read_csv('distribution-of-deaths-by-cause-of-death-sex-nationality-and-medical-district-2008.csv')

#Join the datasets into only one datasets
frames = [df2, df3, df4, df5, df6, df7, df8]
death_2002_2008 = pd.concat(frames)

#Drop the rows that contains value Total from the datasets
death_2002_2008.drop(death_2002_2008.index[death_2002_2008['Medical_District_EN'] == 'Total'], inplace = True)
death_2002_2008.drop(death_2002_2008.index[death_2002_2008['Nationality_EN'] == 'Total'], inplace = True)
death_2002_2008.drop(death_2002_2008.index[death_2002_2008['Sex_EN'] == 'Total'], inplace = True)
death_2002_2008.drop(death_2002_2008.index[death_2002_2008['Cause_of_Death_EN'] == 'Total'], inplace = True)

#Keep only the english columns and remove the arabic columns
death_2002_2008 = death_2002_2008[['Year','Medical_District_EN','Cause_of_Death_EN','Nationality_EN','Sex_EN','Value']]

#create a dataframe that contains the sum of the deaths
death_2002_2008_total=death_2002_2008.groupby(['Year'])['Value'].sum().reset_index()
death_2002_2008_total_gender=death_2002_2008.groupby(['Year','Sex_EN'])['Value'].sum().reset_index()

#read the data of cancer_death between the year 2011 and 2018
cancer_death_2011_2018=pd.read_csv('cancer-mortality-ds-.csv')
#remove the arabic columns
cancer_death_2011_2018 = cancer_death_2011_2018[['Year','Emirate En','Cause Of Death En','Nationality Group En','Gender En','Total Deaths']]
#change the columns name
cancer_death_2011_2018 = cancer_death_2011_2018.rename(columns={'Year':'year','Emirate En':'district', 'Cause Of Death En': 'cause', 'Nationality Group En': 'nationality','Gender En':'gender','Total Deaths':'deaths'})

#read the death data from 2011 to cancer_death_2011_2018
deaths_2011_2018=pd.read_csv('death-counts-by-gender-nationality-and-emirate-v2.csv')
#remove the arabic columns
deaths_2011_2018 = deaths_2011_2018 [['Year','Emirate En','Nationality Group En','Gender En', 'Total']]
#rename the columns
deaths_2011_2018 = deaths_2011_2018.rename(columns={'Year':'year','EmirateEn':'district', 'Nationality Group En':'nationality','Gender En':'gender','Total':'total'})

#read the  birth data from 2002 to death_2002_2008
df12=pd.read_csv('deliveries-and-births-by-nationality-mode-of-delivery-condition-of-newborn-and-district-2002.csv')
df13=pd.read_csv('deliveries-and-births-by-nationality-mode-of-delivery-condition-of-newborn-and-district-2003.csv')
df14=pd.read_csv('deliveries-and-births-by-nationality-mode-of-delivery-condition-of-newborn-and-district-2004.csv')
df15=pd.read_csv('deliveries-and-births-by-nationality-mode-of-delivery-condition-of-newborn-and-district-2005.csv')
df16=pd.read_csv('deliveries-and-births-by-nationality-mode-of-delivery-condition-of-newborn-and-district-2006.csv')
df17=pd.read_csv('deliveries-and-births-by-nationality-mode-of-delivery-condition-of-newborn-and-district-2007.csv')
df18=pd.read_csv('deliveries-and-births-by-nationality-mode-of-delivery-condition-of-newborn-and-district-2008.csv')




#join the birth dast from 2002 to 2008 into 1 DataFrame
frames1 = [df12, df13, df14, df15, df16, df17, df18]
new_birth_2002_2008 = pd.concat(frames1)



#delete the rows with Total
new_birth_2002_2008.drop(new_birth_2002_2008.index[new_birth_2002_2008['Region_EN'] == 'Total'], inplace = True)
new_birth_2002_2008.drop(new_birth_2002_2008.index[new_birth_2002_2008['Birth_Status_EN'] == 'Total'], inplace = True)
new_birth_2002_2008.drop(new_birth_2002_2008.index[new_birth_2002_2008['Nationality_EN'] == 'Total'], inplace = True)
new_birth_2002_2008.drop(new_birth_2002_2008.index[new_birth_2002_2008['Delivery_Condition_EN'] == 'Total'], inplace = True)
new_birth_2002_2008.drop(new_birth_2002_2008.index[new_birth_2002_2008['Delivery_Method_EN'] == 'Total'], inplace = True)
new_birth_2002_2008.drop(new_birth_2002_2008.index[new_birth_2002_2008['Births'] == 'Total'], inplace = True)

#keep only the english columns
new_birth_2002_2008 = new_birth_2002_2008[['Year','Region_EN','Birth_Status_EN','Nationality_EN','Delivery_Condition_EN','Delivery_Method_EN','Births']]

new_birth_2002_2008=new_birth_2002_2008.dropna(subset=['Births'])
new_birth_2002_2008['Births'] =new_birth_2002_2008['Births'].astype(int)


#read the staff data (doctor ..)
staff=pd.read_csv('health-care-staff-by-emirate-sector-gender-and-job-category-ds.csv')
#keep only the english columns
staff = staff [['Year','Emirate En','Sector En','Category En','Gender En','Total']]
#change the name column for easier names
staff = staff.rename(columns={'Year':'year','Emirate En':'district', 'Sector En': 'sector', 'Category En': 'category','Gender En':'gender','Total':'total'})
# drop null values from the total column
staff = staff.dropna(subset=['total'])

#read the hospitals data
hospitals=pd.read_csv('number-of-beds-and-hospitals-by-health-sector-ds.csv')
#keep only the english columns
hospitals = hospitals [['Year','Emirate En','Sector En','Total Beds','Total Hospitals']]
# change the columns name for easier names
hospitals = hospitals.rename(columns={'Year':'year','Emirate En':'district','Sector En':'sector','Total Beds':'beds','Total Hospitals':'hospitals'})
#drop na if available
hospitals = hospitals.dropna(subset=['beds'])
hospitals = hospitals.dropna(subset=['hospitals'])

#import the doctors and staff data
staff = pd.read_csv('health-care-staff-by-emirate-sector-gender-and-job-category-ds.csv')
#keep only the needed columns (english)
staff = staff[['Year','Emirate En','Sector En','Category En','Gender En','Total']]
#change the naming of the columns
staff = staff.rename(columns={'Year':'year','Emirate En':'district', 'Sector En': 'sector', 'Category En': 'category','Gender En':'gender','Total':'total'})
# drop na from the total column
staff = staff.dropna(subset=['total'])
#change the total column to integer
staff['total'] =staff['total'].astype(int)


image = Image.open('image.jpg')
image1 = Image.open('clay-banks-_Jb1TF3kvsA-unsplash.jpg')




st.set_option('deprecation.showPyplotGlobalUse', False)

#make the user to enter the password to show the analysis
password = st.sidebar.text_input("Enter the password please", type="password")

if password == 'MsBa%%42%%':
    st.title('Health Care Analysis in the United Arab Emirates:')

    #add a radio buttons options on the sidebar for the user to select what he wants to see
    button=st.sidebar.radio('Select which Analysis Date you want to See:',
                                ('Info Page', 'Dates Between 2002 and 2008 Pages', 'Dates Between 2011 and 2018 Pages'))

    #start adding to the info page.
    if button == 'Info Page':

        st.write("")
        st.write('In this analysis, we will analyze some of the health care systems in the UAE in 2 ranges of times, one from the year 2002 to 2008, and one from the year 2011 to 2018.')
        st.write('In the first one 2002-2008, we will analyze the number of deaths, based on the gender, causes of these deaths, and how many deaths by each cause. Also, we will analyze the new births during this same period.')
        st.write('In the second one 2011-2018, we will see the number of deaths throughout the years, how many of these deaths are caused by cancer, the top cancer types leading to these deaths, and the count of each cancer type in each year. Also, we will be analyzing the hospitals in UAE, the number of hospitals based on sector, and the number of beds in these hospitals, also we will see the health care staff members in each sector and in each district in UAE.')
        st.write('You can find a detailed user manual of this Analysis and the filters in the https://docs.google.com/document/d/1M5tRz0dY8PZsKTQHAnCrgvV_0B3KaMCZ6Wk6igf7fnE/edit')

        #divide the screen between 2 columns
        col1, col2 = st.beta_columns(2)

        #display the images
        col1.image(image, use_column_width=True)
        col2.image(image1, use_column_width=True)

    #start adding analysis to to the Dates Between 2002 nd 2008 page
    elif button == 'Dates Between 2002 and 2008 Pages':

        #add a second radio button to filter based on the different analysis in this date
        button1=st.sidebar.radio('Select which Analysis you want to see:',
                                    ('Analysis of Death Cases based on the Cause, Gender Location','Analysis of New Born Babies'))



        if button1 == 'Analysis of Death Cases based on the Cause, Gender Location':

            #make the user select if deaths analysis of causes analysis
            death_analysis = st.sidebar.selectbox('Please select:',
                                                    ('Analysis of Deaths Cases','Analysis of Deaths Causes'))

            if death_analysis == 'Analysis of Deaths Cases':

                col1, col2 = st.beta_columns(2)

                col1.subheader("Total Number of Deaths:")

                col1.write('In the below plot we can see that the number of deaths in the years 2002 to 2008 is approximately equal in and the range is between 2500 and 3000 deaths in year.')

                col2.subheader("Deaths Based on Gender:")

                col2.write('In the below plot we can see that in all the years the number of deaths for male are more than double from the number of deaths of female.')



                #barplot that shows the total number of deaths
                plt.rcParams['figure.figsize'] = [10, 8]
                death_2002_2008_total_bar=sns.barplot(x="Year", y="Value",color="Blue",data=death_2002_2008_total)
                death_2002_2008_total_bar.set(ylim=(0, 3500))
                death_2002_2008_total_bar.set(xlabel='Year',ylabel='Total Deaths')
                death_2002_2008_total_bar.set_title('Total Number of Deaths',y=1.02)
                col1.pyplot(use_column_width=True)

                #barplot that display the total number of deaths based on gender
                death_2002_2008_total_gender_bar=sns.barplot(x="Year", y="Value",palette='Blues_d', color='blue', hue='Sex_EN', data=death_2002_2008_total_gender)
                death_2002_2008_total_gender_bar.set(ylim=(0, 3500))
                death_2002_2008_total_gender_bar.set(xlabel='Year',ylabel='Total Deaths')
                death_2002_2008_total_gender_bar.set_title('Total Number of Deaths based on Gender',y=1.02)
                col2.pyplot(use_column_width=True)


            elif death_analysis == 'Analysis of Deaths Causes':

                #add a gender filter in the sidebar
                gender_selection = st.sidebar.selectbox(
                        'Select the Gender you want to see',
                        ('All','Male','Female'))





                if gender_selection == 'All':

                    col1, col2 = st.beta_columns(2)
                    col3, col4 = st.beta_columns(2)

                    col3.subheader("Top Causes of Deaths")
                    col4.subheader("Deaths Based on the selected causes")

                    #make the user enter how many top causes he wants to see.
                    x = col3.number_input('Enter the number of causes you want to see:',min_value=3,)
                    x=int(x)
                    #count based on causes and put the data into a dataframe
                    death_2002_2008_total_cause=death_2002_2008.groupby(['Cause_of_Death_EN'])['Value'].sum().reset_index()
                    #take the top causes based on the user input
                    death_2002_2008_total_cause_top=death_2002_2008_total_cause.nlargest(x, ['Value'])
                    col3.write('In the below plot we see the number of deaths based on the top causes in all the years from 2002 to 2008.')
                    #plot the top causes
                    death_2002_2008_total_cause_top_bar=sns.barplot(x='Cause_of_Death_EN', y='Value',color='Blue', data=death_2002_2008_total_cause_top)
                    death_2002_2008_total_cause_top_bar.set(xlabel='Cause of Death',ylabel='Total Deaths')
                    death_2002_2008_total_cause_top_bar.set_title('Total Number of Deaths per Cause',y=1.02)
                    plt.xticks(rotation=70)
                    col3.pyplot()

                    #create a copy from the dataframe
                    cause_selection=death_2002_2008.copy()
                    #for the causes column keep only distinct values
                    cause_selection_unique=cause_selection.drop_duplicates(subset=['Cause_of_Death_EN'])
                    #create a list from these causes
                    list = cause_selection_unique['Cause_of_Death_EN'].to_numpy()
                    #display this list for the user in a multiselect
                    options = col4.multiselect('Select Cause of Death: (You can select more than 1)', list)
                    #transform his option to a dataframe
                    options_df=pd.DataFrame(options,columns = ['Cause_of_Death_EN'])
                    #merge the tranformed option with the initial dataframe to filter based on the choosen cause
                    cause_selection_selected=pd.merge(cause_selection, options_df, how='inner' )
                    cause_selection_selected = cause_selection_selected.rename(columns={'Cause_of_Death_EN':'cause'})
                    #count the number of deaths
                    cause_selection_selected=cause_selection_selected.groupby(['Year','cause'])['Value'].sum().reset_index()
                    if not options:
                        col4.warning('Please add cause above.')
                    elif options:
                        #plot the causes
                        col4.write('In the below plot we see the deaths based on the selected causes in all the years from 2002 to 2008.')
                        cause_selection_selected_line=sns.lineplot(x="Year", y="Value", hue='cause', data=cause_selection_selected)
                        cause_selection_selected_line.set(xlabel='Year',ylabel='Total Deaths')
                        cause_selection_selected_line.set_title('Total Number of Deaths per Cause',y=1.02)
                        col4.pyplot()



                elif gender_selection == 'Male':

                    #filter the data based on the Male
                    death_2002_2008_M=death_2002_2008[death_2002_2008['Sex_EN']=='M']
                    #count the deaths of Men
                    death_2002_2008_M_toal=death_2002_2008_M.groupby(['Year'])['Value'].sum().reset_index()


                    col1, col2 = st.beta_columns(2)

                    col1.subheader("Top Causes of Deaths for Men:")
                    col2.subheader("Deaths Based on the selected causes for Men:")

                    #Check the top causes of death on the men
                    x = col1.number_input('Enter the number of causes you want to see:',min_value=3,)
                    x=int(x)
                    death_2002_2008_M_cause=death_2002_2008_M.groupby(['Cause_of_Death_EN'])['Value'].sum().reset_index()
                    death_2002_2008_M_cause_top=death_2002_2008_M_cause.nlargest(x, ['Value'])
                    col1.write('In the below plot we see the number of deaths based on the top causes for Men in all the years from 2002 to 2008.')
                    death_2002_2008_M_cause_top_bar=sns.barplot(x='Cause_of_Death_EN', y='Value',color='Blue', data=death_2002_2008_M_cause_top)
                    death_2002_2008_M_cause_top_bar.set(xlabel='Cause of Death',ylabel='Total Deaths')
                    death_2002_2008_M_cause_top_bar.set_title('Total Number of Deaths per Cause',y=1.02)
                    plt.xticks(rotation=70)
                    col1.pyplot()

                    #make the user enter the cause to see the numbers
                    cause_selection_M=death_2002_2008_M.copy()
                    cause_selection_M_unique=cause_selection_M.drop_duplicates(subset=['Cause_of_Death_EN'])
                    list_M = cause_selection_M_unique['Cause_of_Death_EN'].to_numpy()
                    options_M = col2.multiselect('Select Cause of Death: (You can select more than 1)', list_M)
                    options_M_df=pd.DataFrame(options_M,columns = ['Cause_of_Death_EN'])
                    cause_selection_selected_M=pd.merge(cause_selection_M, options_M_df, how='inner' )
                    cause_selection_selected_M = cause_selection_selected_M.rename(columns={'Cause_of_Death_EN':'cause'})
                    cause_selection_selected_M=cause_selection_selected_M.groupby(['Year','cause'])['Value'].sum().reset_index()
                    if not options_M:
                        col2.warning('Please add cause above.')
                    elif options_M:
                        cause_selection_selected_M_line=sns.lineplot(x="Year", y="Value", hue='cause', data=cause_selection_selected_M)
                        col2.write('In the below plot we see the deaths based on the selected causes for Men in all the years from 2002 to 2008.')
                        cause_selection_selected_M_line.set(xlabel='Year',ylabel='Total Deaths')
                        cause_selection_selected_M_line.set_title('Total Deaths Based on Cause',y=1.02)
                        col2.pyplot()



                elif gender_selection == 'Female':

                    #filter the data based on the Female
                    death_2002_2008_F=death_2002_2008[death_2002_2008['Sex_EN']=='F']
                    #count the deaths of Female
                    death_2002_2008_F_toal=death_2002_2008_F.groupby(['Year'])['Value'].sum().reset_index()

                    col1, col2= st.beta_columns(2)

                    col1.subheader("Top Causes of Deaths for Women:")
                    col2.subheader("Deaths Based on the selected causes:")

                    #Check the top causes of death on the Female
                    x = col1.number_input('Enter the number of causes you want to see:',min_value=3,)
                    x=int(x)
                    death_2002_2008_F_cause=death_2002_2008_F.groupby(['Cause_of_Death_EN'])['Value'].sum().reset_index()
                    death_2002_2008_F_cause_top=death_2002_2008_F_cause.nlargest(x, ['Value'])
                    col1.write('In the below plot we see the number of deaths based on the top causes for Women in all the years from 2002 to 2008.')
                    death_2002_2008_F_cause_top_bar=sns.barplot(x='Cause_of_Death_EN', y='Value',color='Blue', data=death_2002_2008_F_cause_top)
                    death_2002_2008_F_cause_top_bar.set(xlabel='Cause of Death',ylabel='Total Deaths')
                    death_2002_2008_F_cause_top_bar.set_title('Total Number of Deaths per Cause',y=1.02)
                    plt.xticks(rotation=70)
                    col1.pyplot()

                    #make the user enter the cause to see the numbers
                    cause_selection_F=death_2002_2008_F.copy()
                    cause_selection_F_unique=cause_selection_F.drop_duplicates(subset=['Cause_of_Death_EN'])
                    list_F = cause_selection_F_unique['Cause_of_Death_EN'].to_numpy()
                    options_F = col2.multiselect('Select Cause of Death: (You can select more than 1)', list_F)
                    options_F_df=pd.DataFrame(options_F,columns = ['Cause_of_Death_EN'])
                    cause_selection_selected_F=pd.merge(cause_selection_F, options_F_df, how='inner' )
                    cause_selection_selected_F = cause_selection_selected_F.rename(columns={'Cause_of_Death_EN':'cause'})
                    cause_selection_selected_F=cause_selection_selected_F.groupby(['Year','cause'])['Value'].sum().reset_index()
                    if not options_F:
                        col2.warning('Please add cause above.')
                    elif options_F:
                        cause_selection_selected_F_line=sns.lineplot(x="Year", y="Value", hue='cause', data=cause_selection_selected_F)
                        col2.write('In the below plot we see the deaths based on the selected causes for Women in all the years from 2002 to 2008.')
                        cause_selection_selected_F_line.set(xlabel='Generation',ylabel='Total Transactions')
                        cause_selection_selected_F_line.set_title('Total Transactions based on Generation',y=1.02)
                        col2.pyplot()


        elif button1 == 'Analysis of New Born Babies':

            col1, col2 = st.beta_columns(2)

            col1.subheader('Number of Births from 2002 to 2008 in All Nationality:')
            col2.subheader('Number of Births from 2002 to 2008 Based on Nationality:')

            col1.write('From the below plot we can see that the year has the lowest number of births then we reached a maximum in 2005 to decrease to half in 2006 and after that we have an increase again lower to the previous increases.')

            #count the total birth based on year  and plot
            new_birth_2002_2008_total=new_birth_2002_2008.groupby(['Year'])['Births'].sum().reset_index()
            new_birth_2002_2008_total_bar=sns.barplot(x="Year", y="Births",color="Blue",data=new_birth_2002_2008_total)
            new_birth_2002_2008_total_bar.set(ylim=(0, 30000))
            new_birth_2002_2008_total_bar.set(xlabel='Year',ylabel='Total Births')
            new_birth_2002_2008_total_bar.set_title('Total Number of Births',y=1.02)
            col1.pyplot()

            col2.write('From the below plot, we can see that in the years 2002, 2004, 2005 and 2008 the Non-Citizen births are higher, while in the other years the Citizen is higher with a huge difference in the year of 2003.')

            #count the total birth based on year nationality and plot
            new_birth_2002_2008_total_Nationality=new_birth_2002_2008.groupby(['Year','Nationality_EN'])['Births'].sum().reset_index()
            new_birth_2002_2008_total_Nationality_bar=sns.barplot(x="Year", y="Births",palette='Blues_d' , hue='Nationality_EN',data=new_birth_2002_2008_total_Nationality)
            new_birth_2002_2008_total_Nationality_bar.set(ylim=(0, 25000))
            new_birth_2002_2008_total_Nationality_bar.set(xlabel='Year',ylabel='Total Births')
            new_birth_2002_2008_total_Nationality_bar.set_title('Total Number of Births based on Nationality',y=1.02)
            col2.pyplot()


    elif button == 'Dates Between 2011 and 2018 Pages':

        #add a radio button to make the user choose ehat he wants to see between deaths and health care system
        button3=st.sidebar.radio('Select which Analysis you want to see:',
                                    ('Cancer Analysis (Cases, Death, Cause)','Analysis of the Healthcare system in UAE'))


        if button3 == 'Cancer Analysis (Cases, Death, Cause)':

            #add a selectbox for the user to choose between deaths from cancer or causes of deaths
            cancer_analysis = st.sidebar.selectbox('Please Select:',
                                                ('Deaths Cases from Cancer','Cancer Causes of Death'))

            if cancer_analysis == 'Deaths Cases from Cancer':


                col1, col2 = st.beta_columns(2)

                col1.subheader("Total Number of Deaths:")
                col1.write('As displayed in the below plot, the total deaths numbers is increasing from 2011 to 2015, and it is constant in the years 2015 to 2018.')

                #count the total deaths and plot
                deaths_2011_2018_total = deaths_2011_2018.groupby(['year'])['total'].sum().reset_index()

                deaths_2011_2018_total_bar=sns.barplot(x="year", y="total",color="Blue",data=deaths_2011_2018_total)
                deaths_2011_2018_total_bar.set(ylim=(0, 10000))
                deaths_2011_2018_total_bar.set(xlabel='Year',ylabel='Total Deaths')
                deaths_2011_2018_total_bar.set_title('Total Number of Deaths',y=1.02)
                col1.pyplot(use_column_width=True)

                col2.subheader("Deaths From Cancer")
                col2.write('In the below plot, the deaths from cancer are increasing throughout the years with the peak increase from 2014 to 2015.')

                #count the deaths from cancer and plot
                cancer_death_2011_2018_total = cancer_death_2011_2018.groupby(['year'])['deaths'].sum().reset_index()
                cancer_death_2011_2018_total_bar=sns.barplot(x="year", y="deaths",color="Blue",data=cancer_death_2011_2018_total)
                cancer_death_2011_2018_total_bar.set(ylim=(0, 2000))
                cancer_death_2011_2018_total_bar.set(xlabel='Year',ylabel='Total Deaths')
                cancer_death_2011_2018_total_bar.set_title('Total Number of Cancer Deaths',y=1.02)
                col2.pyplot(use_column_width=True)

            elif cancer_analysis == 'Cancer Causes of Death':

                col1, col2 = st.beta_columns(2)

                #make the user enter the number of causes of death cancer he wants to see and plot
                col1.subheader('The Top Causes Cancer of Death:')
                x = col1.number_input('Enter the number of causes you want to see:',min_value=3,)
                x=int(x)
                cancer_death_2011_2018_cause=cancer_death_2011_2018.groupby(['cause'])['deaths'].sum().reset_index()
                cancer_death_2011_2018_cause_top=cancer_death_2011_2018_cause.nlargest(x, ['deaths'])
                col1.write('Below is the sum of the top causes of deaths from cancer in the UAE year 2011 to 2018 in all the years. ')
                cancer_death_2011_2018_cause_bar=sns.barplot(x='cause', y='deaths',color='Blue', data=cancer_death_2011_2018_cause_top)
                cancer_death_2011_2018_cause_bar.set(xlabel='Cause of Cancer Death',ylabel='Total Deaths')
                cancer_death_2011_2018_cause_bar.set_title('Total Number of Deaths per Cancer Cause',y=1.02)
                plt.xticks(rotation=70)
                col1.pyplot()

                #make the user enter the cancer cause to see the numbers
                col2.subheader('Number of Deaths by each Cancer type:')
                cause_cancer_death_2011_2018=cancer_death_2011_2018.copy()
                cause_cancer_death_2011_2018_unique=cause_cancer_death_2011_2018.drop_duplicates(subset=['cause'])
                list_C = cause_cancer_death_2011_2018_unique['cause'].to_numpy()
                options_C = col2.multiselect('Select the Cancer Cause of Death: (You can select more than 1)', list_C)
                options_C_df=pd.DataFrame(options_C,columns = ['cause'])
                cancer_cause_selected=pd.merge(cause_cancer_death_2011_2018, options_C_df, how='inner' )
                cancer_cause_selected_total=cancer_cause_selected.groupby(['cause','year'])['deaths'].sum().reset_index()
                if not options_C:
                    col2.warning('Please add cause above.')
                elif options_C:
                    cancer_cause_selected_line=sns.lineplot(x="year", y="deaths",hue='cause', data=cancer_cause_selected_total)
                    col2.write('Below are the changes of the number of deaths from the selected causes throughout the years.')
                    cancer_cause_selected_line.set(xlabel='Year',ylabel='Number of Deaths per Cause')
                    cancer_cause_selected_line.set_title('Total Deaths by each Cancer type throughout the years:',y=1.02)
                    col2.pyplot()


        elif button3 == 'Analysis of the Healthcare system in UAE':

            #make the user select if hospital or staff analysis
            select1=st.sidebar.selectbox('Please select what you want to see (Hospitals or Staff Analysis)',
                                        ('Hospitals Analysis', 'Staff Analysis'))

            if select1 == 'Hospitals Analysis':

                #count the hospitals total
                hospitals_count=hospitals.groupby(['year','sector'])['hospitals'].sum().reset_index()

                #count the beds in hospital
                hospitals_beds_count=hospitals.groupby(['year','sector'])['beds'].sum().reset_index()

                col1, col2 = st.beta_columns(2)

                #plot
                col1.subheader('Number of Hospitals throughout the years in UAE:')
                hospitals_count_bar=sns.barplot(x="year", y="hospitals", palette='Blues_d', hue='sector', data=hospitals_count)
                hospitals_count_bar.set(xlabel='Year',ylabel='Number of Hospitals')
                hospitals_count_bar.set_title('Number of Hospitals in UAE based on Sector',y=1.02)
                col1.pyplot()

                col2.subheader('Number of Beds in Hospitals throughout the years in UAE:')
                hospitals_beds_count_bar=sns.barplot(x="year", y="beds", palette='Blues_d', hue='sector', data=hospitals_beds_count)
                hospitals_beds_count_bar.set(xlabel='Year',ylabel='Number of Beds in Hospitals')
                hospitals_beds_count_bar.set_title('Number of Beds in Hospitals in UAE based on Sector',y=1.02)
                col2.pyplot()

                st.write('Based on the above plots we can realize that the number of private hospitals is increasing more than the government hospitals throughout the years with a huge difference almost double in 2018, while the numbers of beds in the government hospitals is higher even in 2018.')


            elif select1 == 'Staff Analysis':

                col1, col2, col3 = st.beta_columns(3)

                #count the staff based on category
                staff_count=staff.groupby(['year','category'])['total'].sum().reset_index()

                col1.subheader('Number of Health Care Staff Based on their Category:')
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write('In the below plot, we can see that all the categories of staff in healthcare are increasing throughout the years, but the big increase was in the nurses number between the years 2013 and the year 2017.')
                col1.write("")
                col1.write("")
                #plot
                staff_count_line=sns.lineplot(x="year", y="total", hue='category', data=staff_count)
                staff_count_line.set(xlabel='Year',ylabel='Total Health Staff')
                staff_count_line.set_title('Number of health Staff in UAE',y=1.02)
                col1.pyplot()


                staff_count_gov=staff.groupby(['year','category','sector'])['total'].sum().reset_index()

                col2.subheader('Number of Health Care Staff Based on their Category in relation to the sector they are working in:')
                col2.write("")
                col2.write("")


                col2.write('In the below plot, we can see in all the years and for all the categories of staff, the private sector has a bigger number of employees from the government sector.')
                col2.write("")
                col2.write("")
                col2.write("")
                staff_count_gov_line=sns.lineplot(x="year", y="total", hue='category', style='sector', data=staff_count_gov)
                staff_count_gov_line.set(xlabel='Year',ylabel='Total Health Staff')
                staff_count_gov_line.set_title('Number of health Staff in UAE based on the Sector',y=1.02)
                col2.pyplot()


                #make the user select the district to see the staff analysis
                col3.subheader('Number of Health Care Staff by each Category in each District:')
                staff_district=staff.copy()
                staff_district_unique=staff_district.drop_duplicates(subset=['district'])
                list_D = staff_district_unique['district'].to_numpy()
                options_D = col3.selectbox('Select the District to see the analysis of the health staff:', list_D)
                staff_district = staff_district.loc[staff_district["district"] == options_D]
                staff_district_count=staff_district.groupby(['year','category','district'])['total'].sum().reset_index()
                if not options_D:
                    col3.warning('Please add district above.')
                elif options_D:

                    #give the option f he wants to see with district or not
                    staff_dis_sec = col3.radio('Choose if you eant to see with or without Sector.',
                                                ('Without Sector:', 'With Sector'))

                    if staff_dis_sec == 'Without Sector:':

                        staff_district_count_line=sns.lineplot(x="year", y="total",hue='category', data=staff_district_count)
                        staff_district_count_line.set(xlabel='Year',ylabel='Number of Health Staff')
                        staff_district_count_line.set_title('Total Health Staff in Each District:',y=1.02)
                        col3.pyplot()

                    elif staff_dis_sec == 'With Sector':
                        staff_district_count_sector=staff_district.groupby(['year','category','district','sector'])['total'].sum().reset_index()
                        staff_district_count_line=sns.lineplot(x="year", y="total",hue='category', style='sector', data=staff_district_count_sector)
                        staff_district_count_line.set(xlabel='Year',ylabel='Number of Health Staff')
                        staff_district_count_line.set_title('Total Health Staff in Each District:',y=1.02)
                        col3.pyplot()



    st.sidebar.write('The data used in this analysis are downloaded from Bayanat.ae website https://bayanat.ae/')


elif password != '123456':
    st.write('Please Enter the Correct Password from the Sidebar to display the Analysis')

#hide the powered by streamlit and the right icon
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
