import os
import argparse

def load_dorking_keywords(filename):
    """Load dorking keywords from a text file."""
    try:
        with open(filename, 'r') as file:
            # Read all lines and remove leading/trailing whitespaces
            keywords = [line.strip() for line in file.readlines() if line.strip()]
        return keywords
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []

def generate_search_urls(company_name, dorking_keywords):
    """Generate GitHub search URLs based on the company name and dorking keywords."""
    if not dorking_keywords:
        print("No keywords loaded. Exiting...")
        return

    print("\nGenerated GitHub Search URLs:")

    count = 0
    for keyword in dorking_keywords:
        # Generate the search query by appending the company name to each keyword
        search_query = company_name + " " + keyword
        count += 1

        # Construct the search URL and append filters for test/example exclusion
        search_url = f"{count} https://github.com/search?q={search_query.replace(' ', '+')}+NOT+test+NOT+example"

        # Print the search URL for the current keyword
        print(search_url)

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Generate GitHub search URLs using dorking keywords and a company name.")
    parser.add_argument("company", help="The company name to use in the search query.")
    parser.add_argument("-f", "--file", default="github_dorking_keywords.txt", help="Path to the text file containing dorking keywords.\nDefault: github_dorking_keywords.txt")
    
    # Parse the command-line arguments
    args = parser.parse_args()

    # Load dorking keywords from the file
    dorking_keywords = load_dorking_keywords(args.file)

    # Generate and print the search URLs
    generate_search_urls(args.company, dorking_keywords)

if __name__ == "__main__":
    main()
