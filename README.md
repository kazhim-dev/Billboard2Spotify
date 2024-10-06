# Spotify Billboard Top 100 Playlist Creator

This project allows users to generate a Spotify playlist of the top 100 songs from the Billboard Hot 100 chart for a specific date. By scraping the Billboard website and searching Spotify for the corresponding tracks, it automatically compiles a playlist in the user's Spotify account. The code is written in Python and leverages several libraries such as `requests`, `BeautifulSoup`, and `Spotipy` to perform web scraping and interact with the Spotify API.

## Features
- Scrapes the Billboard Hot 100 chart for any date you specify.
- Searches for the songs on Spotify using the Spotipy library.
- Creates a private Spotify playlist with the top 100 songs for the specified date.
- Skips songs that are not found on Spotify and continues adding the rest of the songs.

## Requirements
To use this code, you will need the following:

- **Python 3.7 or higher**
- A **Spotify Developer Account** with a registered app for using Spotify's API.
- The following Python libraries:
  - `requests`: To send HTTP requests to the Billboard website.
  - `beautifulsoup4`: For scraping the Billboard Hot 100 songs from the website.
  - `spotipy`: For interacting with the Spotify API.
  - `python-dotenv`: To securely load environment variables from a `.env` file.

## How It Works

1. **Input Date**: The user is prompted to input a date in the format `YYYY-MM-DD`. This will be used to retrieve the Billboard Hot 100 chart for that specific date.
  
2. **Web Scraping**: The code sends an HTTP request to the Billboard website to retrieve the Hot 100 chart for the specified date using the `requests` library. Then, it parses the HTML response using `BeautifulSoup` to extract the song titles.
  
3. **Spotify Search**: For each song title scraped from the Billboard website, the code uses the Spotify API (via the `spotipy` library) to search for the corresponding song. If a match is found, the song's Spotify URI is collected.
  
4. **Playlist Creation**: After gathering all the available Spotify URIs, the code creates a new private playlist in the user's Spotify account and adds the songs to it.

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/spotify-billboard-top-100.git
   cd spotify-billboard-top-100
   ```

2. **Install the required Python libraries**:
   You can install all the required libraries by running:
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a Spotify App**:
   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and create a new application.
   - Once your app is created, note down the `Client ID` and `Client Secret`.

4. **Environment Variables**:
   - Create a `.env` file in the root directory of your project.
   - Add your `SPOTIFY_CLIENTID` and `SPOTIFY_CLIENTSECRET` to the `.env` file, like this:
     ```
     SPOTIFY_CLIENTID=your_spotify_client_id
     SPOTIFY_CLIENTSECRET=your_spotify_client_secret
     ```

5. **Run the Script**:
   Run the script using Python:
   ```bash
   python main.py
   ```
   
   You will be prompted to input the date (in `YYYY-MM-DD` format) for which you want to generate the playlist.

## Example Usage

```
Which year do you want to travel to? Type the date in this format YYYY-MM-DD: 2020-07-20
```

The script will scrape the Billboard Hot 100 chart for July 20, 2020, search for the songs on Spotify, and create a private playlist in your Spotify account.

## Error Handling

- The script will skip songs that aren't found on Spotify and provide a message indicating that the song was skipped.
  
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions

Feel free to open issues or submit pull requests if you would like to contribute to this project.
