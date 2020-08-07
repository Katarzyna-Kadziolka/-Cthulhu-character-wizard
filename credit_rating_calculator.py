import occupation_info_extractor
from data import Data


class CreditRatingCalculator:
    def __init__(self):
        infos = occupation_info_extractor.get_infos()
        self.info = [i for i in infos if i.occupation_enum == Data.data["occupation"]][0]

    def get_cash(self, credit_rating):
        if credit_rating == 0:
            cash = 0.5
        elif 1 <= credit_rating <= 9:
            cash = credit_rating
        elif 10 <= credit_rating <= 49:
            cash = credit_rating*2
        elif 50 <= credit_rating <= 89:
            cash = credit_rating*5
        elif 90 <= credit_rating <= 98:
            cash = credit_rating*20
        elif credit_rating == 99:
            cash = 50000
        else:
            raise ValueError("Credit rating value is wrong")
        return cash

    def get_assets(self, credit_rating):
        if credit_rating == 0:
            assets = 0
        elif 1 <= credit_rating <= 9:
            assets = credit_rating*10
        elif 10 <= credit_rating <= 49:
            assets = credit_rating*50
        elif 50 <= credit_rating <= 89:
            assets = credit_rating*500
        elif 90 <= credit_rating <= 98:
            assets = credit_rating*2000
        elif credit_rating == 99:
            assets = 5000000
        else:
            raise ValueError("Credit rating value is wrong")
        return assets

    def get_spending_level(self, credit_rating):
        if credit_rating == 0:
            spending_level = 0.5
        elif 1 <= credit_rating <= 9:
            spending_level = 2
        elif 10 <= credit_rating <= 49:
            spending_level = 10
        elif 50 <= credit_rating <= 89:
            spending_level = 50
        elif 90 <= credit_rating <= 98:
            spending_level = 250
        elif credit_rating == 99:
            spending_level = 5000
        else:
            raise ValueError("Credit rating value is wrong")
        return spending_level