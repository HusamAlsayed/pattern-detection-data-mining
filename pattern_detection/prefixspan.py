import copy


class PrefixSpan:
    def __init__(self, min_support, database, max_level):
        self.min_support = min_support
        self.database = database
        self.max_level = max_level

    def build_prefix_span(self):
        final_ans = {}
        queue = [()]
        for level in range(self.max_level):
            ans = {}
            for pattern in queue:
                for record in self.database:
                    new_data = copy.copy(record)
                    ok = True
                    for element in pattern:
                        try:
                            new_index = new_data.index(element)
                            new_data = new_data[new_index + 1:]
                        except ValueError:
                            ok = False
                    if ok:
                        new_data = set(new_data)
                        for word in new_data:
                            new_tuple = pattern + (word,)
                            ans[new_tuple] = ans.get(new_tuple, 0) + 1
            ans = {key: value for key, value in ans.items() if value > self.min_support}
            final_ans.update(ans)
            queue = list(ans)
        return final_ans






