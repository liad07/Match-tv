
# Match Tv


## Introduction

Match Tv  is a Python script that helps you discover movies and TV series that match your interests and preferences. Using the power of IMDb's vast database, this project provides personalized recommendations for your next movie night or binge-watching session.

## Prerequisites

- Python 3.x
- [IMDbPy Library](https://imdbpy.github.io/) (included in requirements.txt)

## Installation

1. Clone this repository to your local machine.

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## How to Use

1. Run the script:

   ```
   python match_tv.py
   ```

2. Enter the name of a movie or TV series you love when prompted.

3. The script will search for related movies and TV series that share similarities based on genres, directors, actors, and more.

4. Get ready to explore your top recommendations, personalized just for you!

## Example Output

```
Please enter a movie or series to find a new series or movie in the same style:
> saving shuli

Getting first info...
Found the following movie/series information:
Title: saving shuli
Year: 2021
Type: movie

start getting data about the best 10 movies...

Found 10 recommendations similar to saving shuli:
Movie: Mezulamim | Type: tv series | Matching Genres: 1 of 1 | Appearances: 7 | ID: 13858680
Movie: HaYisraelim | Type: tv series | Matching Genres: 1 of 1 | Appearances: 7 | ID: 2592102
Movie: Am Sgula | Type: tv series | Matching Genres: 1 of 1 | Appearances: 5 | ID: 1916799
Movie: Buba Shel Medina | Type: tv series | Matching Genres: 1 of 1 | Appearances: 5 | ID: 2604284
Movie: Shutafim | Type: tv series | Matching Genres: 1 of 1 | Appearances: 4 | ID: 5979972
TV Series: Juda | Type: tv series | Matching Genres: 0 of 1 | Appearances: 4 | ID: 6839538
Movie: Anachnu BaMapa | Type: tv series | Matching Genres: 1 of 1 | Appearances: 4 | ID: 5180494
Movie: The Arbitrator | Type: tv series | Matching Genres: 1 of 1 | Appearances: 4 | ID: 0904106
Movie: Little Simico's Great Fantasy | Type: movie | Matching Genres: 1 of 1 | Appearances: 4 | ID: 2072985


Enjoy exploring these exciting recommendations for your next movie or TV series!
```

## Features

- Discover new movies/TV series similar to your favorites.
- Personalized recommendations based on genres, directors, and actors you enjoy.
- Easy-to-use command-line interface for input and results.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
