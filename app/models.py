from enum import StrEnum


class VocabularyAreas(StrEnum):
    CLOTHES = "👕 مَلَابِسٌ"
    ANIMALS = "🐱 حَيَوَانَاتٌ"
    NATURE = "🏔️ طَبِيعَةٌ"
    FOOD = "🥙 طَعَامٌ"
    COLORS = "🟣 ألْوَانٌ"
    JOBS = "👨🏻‍💻 مِهَنٌ"
    BODY = "🧠 جُزْءٌ مِنَ ٱلْجَسَدِ"
    FAMILY = "👴🏻 أُسْرَةٌ"


WORD_FACTORY = {
    VocabularyAreas.CLOTHES: "app/data/clothes.json",
    VocabularyAreas.ANIMALS: "app/data/animals.json",
    VocabularyAreas.NATURE: "app/data/nature.json",
    VocabularyAreas.FOOD: "app/data/food.json",
    VocabularyAreas.COLORS: "app/data/colors.json",
    VocabularyAreas.JOBS: "app/data/jobs.json",
    VocabularyAreas.BODY: "app/data/body.json",
}
