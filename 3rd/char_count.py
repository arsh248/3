from mrjob.job import MRJob

class CharacterCount(MRJob):
    
    def mapper(self, _, line):
        # Emit each character with count 1
        for char in line:
            yield char, 1
    
    def reducer(self, key, values):
        # Sum up the counts for each character
        yield key, sum(values)

# Run the job directly
CharacterCount.run()
