from event import Event


class Esmeralda(Event):
    def __init__(self, event_start_date, event_start_month, event_start_year, event_end_date, event_end_month,
                 event_end_year, number_of_participants, winner, fund, event_head, first_score,
                 second_score, third_score, max_score, judge_fees, banner_price, ):
        Event.__init__(self, event_start_date, event_start_month, event_start_year, event_end_date, event_end_month,
                       event_end_year, number_of_participants, winner, first_score, second_score, max_score,
                       third_score, fund, event_head)
        self.judge_fees = judge_fees
        self.banner_price = banner_price

    def first_prize(self):
        return (60 / 100) * (self.fund - self.judge_fees - self.banner_price)

    def second_prize(self):
        return (30 / 100) * (self.fund - self.judge_fees - self.banner_price)

    def third_prize(self):
        return (10 / 100) * (self.fund - self.judge_fees - self.banner_price)
