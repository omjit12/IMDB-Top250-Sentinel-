import scrapy
import json
from datetime import datetime


class ImdbTop250Spider(scrapy.Spider):
    name = "imdb_top250"
    allowed_domains = ["imdb.com"]

    custom_settings = {
        "DOWNLOAD_DELAY": 1,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 1,
        "DEFAULT_REQUEST_HEADERS": {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
        },
    }

    def start_requests(self):
        yield scrapy.Request("https://www.imdb.com/chart/top/")

    def parse(self, response):
        # Extract Top 250 from embedded JSON
        script = response.xpath(
            '//script[@type="application/ld+json"]/text()'
        ).get()

        data = json.loads(script)
        movies = data["itemListElement"]

        self.logger.info(f"Movies found: {len(movies)}")

        for rank, movie in enumerate(movies, start=1):
            item = movie["item"]

            yield scrapy.Request(
                url=item["url"],
                callback=self.parse_movie,
                meta={
                    "rank": rank,
                    "title": item["name"],
                    "rating": item["aggregateRating"]["ratingValue"],
                    "votes": item["aggregateRating"]["ratingCount"],
                    "movie_url": item["url"],
                },
            )

    def parse_movie(self, response):
        # Extract movie-level JSON
        script = response.xpath(
            '//script[@type="application/ld+json"]/text()'
        ).get()

        data = json.loads(script)

        year = data.get("datePublished")
        if year:
            year = year[:4]  # keep only YYYY

        genres = data.get("genre", [])
        if isinstance(genres, str):
            genres = [genres]

        directors = data.get("director", [])
        if isinstance(directors, dict):
            directors = [directors]
        directors = [d["name"] for d in directors]

        duration = data.get("duration")  # ISO format: PT142M
        certificate = data.get("contentRating")

        yield {
            "rank": response.meta["rank"],
            "title": response.meta["title"],
            "year": year,
            "rating": response.meta["rating"],
            "votes": response.meta["votes"],
            "genres": ", ".join(genres),
            "duration": duration,
            "certificate": certificate,
            "directors": ", ".join(directors),
            "poster_url": data.get("image"),
            "movie_url": response.meta["movie_url"],
            "scrape_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
