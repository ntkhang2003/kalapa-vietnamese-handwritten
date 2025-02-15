class StringDistance:
    '''
    Implement distance between two strings use edit distance
    '''
    def __init__(self, cost_dict_path=None):
        self.cost_dict = dict()
        if cost_dict_path is not None:
            self.load_cost_dict(cost_dict_path)

    def load_cost_dict(self, filepath):
        if self.cost_dict is None:
            self.cost_dict = dict()
        with open(filepath, encoding="utf8") as f:
            for line in f:
                char1, char2, cost = line.strip().split('\t')
                if char1 and char2:
                    self.cost_dict[(char1, char2)] = int(cost)

    def distance(self, source, target):
        insertion_weigth = 10
        deletion_weigth = 10
        substitution_weigth = 8
        if source == target: return 0
        elif len(source) == 0: return len(target)*insertion_weigth
        elif len(target) == 0: return len(source)*insertion_weigth
        v0 = [None] * (len(target) + 1)
        v1 = [None] * (len(target) + 1)
        for i in range(len(v0)):
            v0[i] = i * insertion_weigth 
        for i in range(len(source)):
            v1[0] = (i + 1)*insertion_weigth
            for j in range(len(target)):
                cost = 0 if source[i] == target[j] else self.cost_dict.get((source[i], target[j]), substitution_weigth)
                v1[j + 1] = min(v1[j] + deletion_weigth, v0[j + 1] +insertion_weigth, v0[j] + cost)
            for j in range(len(v0)):
                v0[j] = v1[j]

        return v1[len(target)]

def extract_digit(text: str):
    res = ''
    for char in text:
        if char.isdigit():
            res += char
    return res


s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'
def remove_accents(input_str):
    s = ''
    for c in input_str:
        if c in s1:
            s += s0[s1.index(c)]
        else:
            s += c
    return s
