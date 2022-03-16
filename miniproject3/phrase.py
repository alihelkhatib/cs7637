from typing import Dict, List
from word_dict import word_dict

class Phrase:
    
    def __init__(self, phrase, type):
        self.origin = phrase
        self.type = type
        self.phrase = self._preprocess(self.origin)
        self.frame, self.tags = self._create_frame_tags(self.phrase)
        self.chunks = self._create_chunks([2, 3])
        

    def _preprocess(self, phrase) -> List:
        '''Remove punctuation and split phrase into tokens'''
        phrase = phrase.rstrip(".?")
        phrase = phrase.split()
        return phrase

    def _create_frame_tags(self, phrase) -> Dict:
        ''' Create dict with all tokens tagged with part-of-speech tag
            Then, create a list of all the tags in order.
        '''
        frame = {k:word_dict.get(k) for k in phrase}
        tags = [frame.get(token) for token in phrase]
        return frame, tags

    def _create_chunks(self, size_range):
        chunks = {}
        for size in size_range:
            chunks[size] = self._create_phrase_chunk(size)
        return chunks

    def _create_phrase_chunk(self, chunk_size) -> List[tuple]:
        ''' Create chunks from phrase to retain context
        '''
        phrase_chunked = []
        for i in range(chunk_size):
            phrase_chunked.append(self.tags[i:])
        return phrase_chunked

    def scan_chunks(self, sequence):
        chunk_size = len(sequence)
        window = self.chunks[chunk_size]
        window = list(zip(*window))
        if sequence in window:
            start = window.index(sequence)
            positions = [start + step for step in range(chunk_size)]
            return positions
        else:
            return False 

    def __repr__(self) -> str:
        return self.origin
    
    


    