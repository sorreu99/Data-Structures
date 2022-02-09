from event import Event


class CulturalAakriti(Event):
    def __init__(self, event_start_date, event_start_month, event_start_year, event_end_date, event_end_month,
                 event_end_year, number_of_participants, winner, fund, event_head, number_of_sub_events, first_score,
                 second_score, max_score, third_score):
        Event.__init__(self, event_start_date, event_start_month, event_start_year, event_end_date,
                       event_end_month,
                       event_end_year, number_of_participants, winner, fund, event_head, first_score,
                       second_score, max_score, third_score)
        self.number_of_sub_events = number_of_sub_events


