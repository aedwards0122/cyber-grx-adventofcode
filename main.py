
#main class for parsing source data
class StringParser:

    #Static Data
    score_map = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }

    score_map_p2 = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }   
 
    char_key = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }

    #Constructor to setup data file and the non-static class memebers
    def __init__(self, file_name):
        self.stack = []
        self.middle_score = 0
        self.total_scores_p2 = []
        self.corrupted_lines = 0
        self.total_lines = 0
        self.total_score = 0
        self.data = []
        self.file_name = file_name

        with open(file_name) as source:
            source_row = source.readline()
            while source_row:
                self.data.append(source_row.strip('\n'))
                source_row = source.readline()
        
        self.parse_data()


    def get_key_by_value(self, v):
        for key, value in self.char_key.items():
            if v == value:
                return key
        return False


    def output_data_values(self):
        print('-----------------------------------------------------')
        print(f'File Name Used: {self.file_name}')
        print('-----------------------------------------------------')
        print(f'Part 1 Score: {self.total_score}')
        print(f'Part 1 Corrupted Line Count: {self.corrupted_lines}')
        print(f'Part 2 Score: {self.middle_score}')
        print(f'Part 2 # of Scores to Consider: {len(self.total_scores_p2)}')

    def parse_data(self):
        if not self.data:
            raise Exception("Source Data is Empty")
            return False
        else:
            right_bracket_values = self.char_key.values()
            for row in self.data:
                self.stack = []
                for char in row:
                    if (char in self.char_key):
                        self.stack.append(char)
                    elif (char in right_bracket_values):
                        if(self.stack[-1] == self.get_key_by_value(char)):
                            self.stack.pop()
                        else:
                            self.total_score += self.score_map[char]
                            self.corrupted_lines += 1
                            break
                    else:
                        raise Exception("Unexpected Charater")
                else:
                    score = 0
                    for char in self.stack[::-1]:
                        score *= 5
                        score += self.score_map_p2[self.char_key[char]]
                    self.total_scores_p2.append(score)
                    self.middle_score = sorted(self.total_scores_p2)[len(self.total_scores_p2)//2]

        self.output_data_values()
        return True
        
