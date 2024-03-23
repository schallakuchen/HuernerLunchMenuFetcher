
from datetime import datetime
import pandas as pd
import argparse
import requests
from bs4 import BeautifulSoup
from openpyxl.utils import get_column_letter


def main():
    parser = argparse.ArgumentParser(description='Parse lunch menu from Fleischerei Huerner')
    parser.add_argument('-f', '--inputf', type=str, help='URL to the menu page', default='https://www.fleischerei-huerner.at/regionales_mittagsmenue/')
    parser.add_argument('-o', '--outputf', type=str, help="Location to store the output file including it's name", default='weekly_lunch_menu')
    args = parser.parse_args()

    # Add timestamp to the output file name
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    output_file = f'{args.outputf}_{timestamp}.xlsx'

    # Read html page from webpage
    html_page = fetch_html_by_url(args.inputf)
    # Parse menu data from html content
    menu_data = parse_html_content(html_page)
    # Export data as excel file
    export_menu_data_to_excel(menu_data, output_file)

    print(f"Die Daten wurden erfolgreich in '{output_file}' exportiert.")


def fetch_html_by_url(url):
    response = requests.get(url)
    response.raise_for_status()  # Ensures the request was successful
    html_content = response.text
    return BeautifulSoup(html_content, 'html.parser')


def parse_html_content(html_soup):
    menus = html_soup.find_all('div', class_='tb-column-inner')
    menu_data = []

    for index, menu in enumerate(menus):
        # Ignore irrelevant data
        if index == 0 or index >= 6:
            continue

        date_info_full = menu.find('div', class_='module-text').get_text(strip=True)
        date_parts = date_info_full.split(',')
        if len(date_parts) >= 2:
            day = date_parts[0].strip()
            date = date_parts[1].strip()
        else:
            day = "not available"
            date = "not available"

        menu_info = menu.find_all('div', class_='module-text')[1].get_text(strip=True)
        price_info = menu.find_all('div', class_='module-text')[2].get_text(strip=True)

        menu_data.append({
            'Tag': day,
            'Datum': date,
            'Menü': menu_info,
            'Preis': price_info
        })

    return menu_data


def auto_adjust_column_width(df, writer, sheet_name='Sheet1'):
    """
    Passt die Spaltenbreiten an den Inhalt an.
    """
    for column in df:
        column_width = max(df[column].astype(str).map(len).max(), len(column))
        col_idx = df.columns.get_loc(column) + 1  # get the column index
        writer.sheets[sheet_name].column_dimensions[get_column_letter(col_idx)].width = column_width


def export_menu_data_to_excel(daten, dateiname):
    # Initialize DataFrame
    df = pd.DataFrame(daten)

    # Create ExcelWriter object with 'openpyxl' as engine
    with pd.ExcelWriter(dateiname, engine='openpyxl') as writer:
        # Write data to excel
        df.to_excel(writer, index=False)

        # adjust column width to text
        auto_adjust_column_width(df, writer)


if __name__ == '__main__':
    main()

