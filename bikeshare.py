import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # Get user input for city
    while True:
        city = input("Enter the city (Chicago, New York City, Washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid input. Please choose from Chicago, New York City, or Washington.")
    
    # Get user input for month
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("Enter the month (January to June) or 'all' for no filter: ").lower()
        if month in months:
            break
        else:
            print("Invalid input. Please enter a valid month or 'all'.")
    
    # Get user input for day
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("Enter the day of the week or 'all' for no filter: ").lower()
        if day in days:
            break
        else:
            print("Invalid input. Please enter a valid day or 'all'.")

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    """
    # Load data
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Extract month and day of week
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    # Filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    # Filter by day
    if day != 'all':
        df = df[df['day_of_week'].str.lower() == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')

    print("Most Common Month:", df['month'].mode()[0])
    print("Most Common Day of Week:", df['day_of_week'].mode()[0])
    print("Most Common Start Hour:", df['hour'].mode()[0])

    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')

    print("Most Common Start Station:", df['Start Station'].mode()[0])
    print("Most Common End Station:", df['End Station'].mode()[0])
    print("Most Frequent Trip:",
          (df['Start Station'] + " to " + df['End Station']).mode()[0])

    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    
    print("Total Travel Time:", df['Trip Duration'].sum())
    print("Average Travel Time:", df['Trip Duration'].mean())

    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')

    print("User Types:\n", df['User Type'].value_counts())

    if 'Gender' in df:
        print("\nGender Counts:\n", df['Gender'].value_counts())

    if 'Birth Year' in df:
        print("\nEarliest Birth Year:", int(df['Birth Year'].min()))
        print("Most Recent Birth Year:", int(df['Birth Year'].max()))
        print("Most Common Birth Year:", int(df['Birth Year'].mode()[0]))

    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # Option to view raw data
        view_data = input('\nWould you like to view 5 rows of raw data? Enter yes or no.\n')
        start_loc = 0
        while view_data.lower() == 'yes':
            print(df.iloc[start_loc:start_loc + 5])
            start_loc += 5
            view_data = input("Do you wish to continue? Enter yes or no: ")

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()