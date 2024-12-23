from mrjob.job import MRJob
from mrjob.step import MRStep


class RatingsBreakdown(MRJob):
    # steps function tells the framework what functions are used as mappers and reducers
    def steps(self):
        return [
            # 1st step
            MRStep(mapper=self.mapper_get_ratings, reducer=self.reducer_count_ratings),
            # 2nd step
            MRStep(reducer=self.reducer_sorted_output),
        ]

    def mapper_get_ratings(self, _, line):
        (userId, movieId, rating, timestamp) = line.split("\t")
        yield movieId, 1

    def reducer_count_ratings(self, key, values):
        yield str(sum(values)).zfill(5), key

    def reducer_sorted_output(self, count, movies):
        for movie in movies:
            yield movie, count  # find top movies


if __name__ == "__main__":
    RatingsBreakdown.run()
