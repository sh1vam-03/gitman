import os
import argparse

def load_dorking_keywords(Keyword_filename):
    """Load dorking keywords from a text file."""
    try:
        with open(Keyword_filename, 'r') as file:
            # Read all lines and remove leading/trailing whitespaces
            keywords = [line.strip() for line in file.readlines() if line.strip()]
        return keywords
    except FileNotFoundError:
        print(f"Error: The file '{Keyword_filename}' was not found.")
        return []

def load_company_queries(filename):
    """Load company related keywords from a text file."""
    try:
        with open(filename, 'r') as file:
            # Read all lines and remove leading/trailing whitespaces
            keywords = [line.strip() for line in file.readlines() if line.strip()]
        return keywords
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []

def generate_search_urls(company_keywords, dorking_keywords):
    """Generate GitHub search URLs based on the company name and dorking keywords."""
    if not dorking_keywords:
        print("No keywords loaded. Exiting...")
        return

    print("\nGenerated GitHub Search URLs:")

    count = 0
    for related_keyword in company_keywords:
        for keyword in dorking_keywords:
            # Generate the search query by appending the company name to each keyword
            search_query = related_keyword + " " + keyword
            count += 1

            # Construct the search URL and append filters for test/example exclusion
            search_url = f"{count} https://github.com/search?q={search_query.replace(' ', '+')}+NOT+test+NOT+example"

            # Print the search URL for the current keyword
            print(search_url)

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Generate GitHub search URLs using dorking keywords and company-related keywords.")
    parser.add_argument("-k", "--keyword", default="", help="Company-related keyword(s) as a comma-separated list.")
    parser.add_argument("-l", "--list", default="", help="Path to the text file containing company-related keywords.")
    parser.add_argument("-f", "--file", default="github_dorking_keywords.txt", help="Path to the text file containing dorking keywords.\nDefault: github_dorking_keywords.txt")
    
    # Parse the command-line arguments
    args = parser.parse_args()

    # Load dorking keywords from the file
    dorking_keywords = load_dorking_keywords(args.file)

    # If a company keyword list file is provided, load it
    if args.list:
        company_keywords = load_company_queries(args.list)
    elif args.keyword:
        # Otherwise, use the provided company keyword(s)
        company_keywords = args.keyword.split(",")
    else:
        print("""error error error
[-k] --keyword  -Company-related keyword(s) as a comma-separated list.
[-l] --list     -Path to the text file containing company-related keywords.
[-f] --file     -Path to the text file containing dorking keywords.
                 Default: github_dorking_keywords.txt
""")
        return

    # Generate and print the search URLs
    generate_search_urls(company_keywords, dorking_keywords)

if __name__ == "__main__":
    main()
