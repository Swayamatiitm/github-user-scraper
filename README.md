# GitHub User Scraper
- This project scrapes GitHub user data for individuals in London with over 500 followers.  
- A surprising finding is that many users do not publicly list their email addresses, indicating a shift toward privacy.  
- Developers should enhance their profiles by adding more public information to increase visibility and networking opportunities.  

## Data Scraping Process
The project uses the GitHub API to collect user data. We make authenticated requests to retrieve profiles and their public repositories, handling rate limits by implementing pauses between requests.

## Interesting Findings
Many users do not list their email addresses, reflecting a growing concern for privacy among developers. This trend could impact how professionals connect and network on GitHub.

## Recommendations
Developers should consider enhancing their GitHub profiles by including more public information, such as contact details and project showcases. This could increase visibility to potential collaborators and employers, fostering better networking opportunities.

## Files Included
- **users.csv**: Contains user details for GitHub users located in London with over 500 followers.
- **repositories.csv**: Contains the public repositories for the users listed in users.csv.
- **README.md**: Documentation for the project.
- **github_scraper.py**: The Python script used to scrape data from GitHub.