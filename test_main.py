from fastapi.testclient import TestClient
from main import app


def test_root():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Need recipe ideas?"}


def test_recipe_tea():
    with TestClient(app) as client:
        response = client.post(
            "/recipe/tea",
            json={"q": "tea"},
        )
        assert response.status_code == 405
        assert response.json() == {
            "ingredients": [
                "teas",
                "tea bags",
                "matcha green tea powder",
                "green tea",
                "chai tea",
                "earl grey tea",
                "earl grey tea bags",
                "tea leaves",
                "iced tea",
                "green tea powder",
                "black tea leaves",
                "brewed tea",
                "earl grey tea leaves",
                "sweet tea",
                "hibiscus tea",
                "green tea leaves",
                "tea biscuits",
                "hibiscus tea bags",
                "jasmine tea",
                "instant tea powder",
                "unsweetened instant tea",
                "chai tea teabags",
                "iced tea mix",
                "lipton\u00AE cup size tea bags",
                "earl grey teabags",
                "lapsang souchong tea",
                "teardrop tomatoes",
                "unsweetened iced tea",
                "chai tea concentrate",
                "oolong tea",
                "english breakfast tea bags",
                "darjeeling tea",
                "sweet tea vodka",
                "thai tea leaves",
                "english breakfast tea",
                "lipton tea bags",
                "jasmine green tea",
                "loose leaf chai tea",
                "thai tea mix",
                "oolong tea leaves",
                "unsweetened green tea",
                "orange pekoe tea",
                "lipton\u00AE iced tea brew family size tea bags",
                "jasmine tea leaves",
                "lipton green tea with mandarin orange flavor pyramid tea bag",
                "lipton lemon iced tea mix",
                "lipton green tea",
                "jasmine tea bags",
                "sweetened iced tea",
                "darjeeling tea leaves",
                "green tea teabags",
                "raspberry tea",
                "chai tea powder",
                "lipton iced tea",
                "lipton pure leaf iced tea with raspberry",
                "lemon iced tea",
                "rooibos tea leaves",
                "mint tea leaves",
                "bigelow green tea",
                "lipton 100% natural iced tea with pomegranate blueberry",
                "fruit tea",
                "social tea biscuits",
                "tea cake",
                "ginger tea",
                "iced tea powder",
                "fennel tea",
                "lipton 100% natural iced tea with lemon",
                "lipton black tea",
                "gunpowder green tea leaves",
                "green jasmine tea",
                "lipton bedtime story caffeine-free herbal pyramid tea bag",
                "english breakfast tea leaves",
                "twinings earl grey tea",
                "cinnamon tea blend",
                "chai green tea",
                "luzianne iced tea",
                "gold peak sweet tea",
                "zen green tea liqueur",
                "rosehip tea",
                "lemonade iced tea",
                "lipton sparkling diet green tea with strawberry kiwi",
                "tazo black tea",
                "lipton diet green tea with citrus",
                "diet green tea",
                "lipton iced tea brew",
                "arizona iced tea",
                "loose-leaf chamomile tea",
                "japanese genmaicha green tea",
                "crystal light iced tea mix",
                "tetley iced tea blend",
                "lipton green tea ",
                "snapple raspberry iced tea",
                "tradewinds green tea",
                "tadin green tea",
                "lipton earl grey tea",
                "lipton\u00AE tea & honey blackberry pomegranate iced green tea mix pitcher packet",
                "lipton\u00AE tea & honey strawberry acai decaf iced green tea mix to go packe",
                "lipton\u00AE tea & honey blackberry pomegranate iced green tea mix to go packet",
                "ginseng tea bags",
                "alo aloe + olive leaf tea",
                "blackcurrant tea",
                "organic india tulsi green tea",
                "taylors of harrogate earl grey tea",
                "citrus tea leaves",
                "lipton green tea sweetened iced tea mix",
                "decaffeinated hibiscus tea bags",
                "raspberry sweet tea vodka",
                "jasmine blend tea bags",
                "raspberry iced tea",
                "decaffeinated earl grey tea leaves",
                "mango tea",
                "raspberry tea cake",
                "unsweetened chai tea",
                "arizona diet green tea",
                "ginseng tea",
                "irish breakfast tea leaves",
                "jasmine herbal tea bag",
                "gold peak lemonade iced tea",
                "mighty leaf green tea",
            ],
            "searches": [
                "tea",
                "iced tea",
                "green tea",
                "tea with alcohol",
                "milk tea",
                "chai tea",
                "ice tea",
                "tea sandwiches",
                "butter tea biscuits",
                "parsley tea",
            ],
        }
