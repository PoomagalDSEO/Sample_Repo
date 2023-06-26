import whois
import validators
import gspread as gs
import pandas as pd
import streamlit as st
from datetime import datetime, timedelta

# Function to check domain expiry date
def check_domain_expiry(dm):
    if validators.domain(dm):
        try:
            dm_info = whois.whois(dm)
            # return domain_info
            exp_date = dm_info.expiration_date

            # If expiry date is a list, consider the first element
            if isinstance(exp_date, list):
                exp_date = exp_date[0]

            # Compare with current date
            curr_date = datetime.now()
            days_remaining = (exp_date - curr_date).days

            if days_remaining <= 10:
                return f"Domain {dm} is expiring soon. Expires in {days_remaining} days."
            else:
                return f"Domain {dm} is not expiring soon. Expires in {days_remaining} days."

        except Exception as error:
            return f"Error: {str(error)}"
    # else:
    #     return None
            # f"Enter a valid domain"

# Main function to get user input and check domain expiry
def main():
    gc = gs.service_account(filename='connections.json')
    sh = gc.open_by_url(
        'https://docs.google.com/spreadsheets/d/15mODRXCtY1MoC9ChfUamm4IGmwTNuOpLK7TpYkM_fNQ/edit#gid=503088821')
    ws = sh.worksheet('sheet1')
    df = pd.DataFrame(ws.get_all_records())
    df2= df[df.columns[0]].values.tolist()
    print(df2)
    DM = df2
    for dm in DM:
        print(dm)
        if dm != '':
            result = check_domain_expiry(dm)
            st.write(result)
            # print(result)
        else:

            break
            # print('No element')
if __name__ == "__main__":
    main()
