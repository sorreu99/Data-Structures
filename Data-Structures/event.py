from datetime import date


class Event:
    def __init__(self, event_start_date, event_start_month, event_start_year, event_end_date, event_end_month,
                 event_end_year, number_of_participants, winner, first_score, second_score, max_score, third_score,
                 fund,event_head):
        self.event_start_date = event_start_date
        self.event_start_month = event_start_month
        self.event_start_year = event_start_year
        self.event_end_date = event_end_date
        self.event_end_month = event_end_month
        self.event_end_year = event_end_year
        self.number_of_participants = number_of_participants
        self.winner = winner
        self.fund = fund
        self.event_head = event_head
        self.first_score = first_score
        self.second_score = second_score
        self.third_score = third_score
        self.max_score = max_score

    def total_days(self):
        start_date = date(self.event_start_year, self.event_start_month, self.event_start_date)
        end_date = date(self.event_end_year, self.event_end_month, self.event_end_date)
        delta = end_date - start_date
        return delta.days

    def first_prize(self):
        return self.first_score / self.max_score

    def second_prize(self):
        return self.second_score / self.max_score

    def third_prize(self):
        return self.third_score / self.max_score

    def score_difference(self):
        print("the score difference between first and second is", self.first_score - self.second_score)
        print("the score difference between second and third is", self.second_score - self.third_score)
