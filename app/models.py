from enum import StrEnum


class VocabularyAreas(StrEnum):
    ADJECTIVES = "🟦 صِفَاتٌ"
    ANIMALS = "🐱 حَيَوَانَاتٌ"
    BODY = "🧠 أَجْزَاءُ ٱلْجَسَدِ"
    CLOTHES = "👕 مَلَابِسٌ"
    COLORS = "🎨 أَلْوَانٌ"
    DISHES = "🥘 أَطْبَاقٌ"
    FAMILY = "👪 أُسْرَةٌ"
    FOOD = "🍽 طَعَامٌ"
    FRUIT = "🍎 فَوَاكِهٌ"
    HOUSE = "🏠 مَنزِلٌ"
    JOBS = "👨🏻‍💻 مِهَنٌ"
    NATURE = "🏔 طَبِيعَةٌ"


WORD_FACTORY = {
    VocabularyAreas.ADJECTIVES: "app/data/adjectives.json",
    VocabularyAreas.ANIMALS: "app/data/animals.json",
    VocabularyAreas.BODY: "app/data/body.json",
    VocabularyAreas.CLOTHES: "app/data/clothes.json",
    VocabularyAreas.COLORS: "app/data/colors.json",
    VocabularyAreas.DISHES: "app/data/dishes.json",
    VocabularyAreas.FAMILY: "app/data/family.json",
    VocabularyAreas.FOOD: "app/data/food.json",
    VocabularyAreas.FRUIT: "app/data/fruit.json",
    VocabularyAreas.HOUSE: "app/data/house.json",
    VocabularyAreas.JOBS: "app/data/jobs.json",
    VocabularyAreas.NATURE: "app/data/nature.json",
}
