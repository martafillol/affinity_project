
# List of target interests
import pandas as pd
targets = [
    "Fashion", "Pets", "Cooking", "Fitness", "Movies", "Gaming", "Travel",
    "Cars and automobiles", "Outdoor activities", "Books", "Finance and investments",
    "Business and entrepreneurship", "Photography", "Art", "Social causes and activism",
    "Health and wellness", "Gardening", "Technology", "Education and learning",
    "Sports", "Nature", "History", "Parenting and family", "Music",
    "Food and dining", "DIY and crafts", "Beauty", "Science", "Politics"
]


base_sitemap_urls = [
    "https://www.houseandgarden.co.uk/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.vanityfair.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.epicurious.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.epicurious.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.cntraveller.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.voguebusiness.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.voguebusiness.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://pitchfork.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.self.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.self.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.worldofinteriors.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.worldofinteriors.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.worldofinteriors.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.architecturaldigest.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.newyorker.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.tatler.com/sitemap.xml?year={year}&month={month}&week={week}"
]
clusters = pd.read_csv("affinity/data/data_v2.csv")
