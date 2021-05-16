def get_amount(string):
    try:
        i = string.find(' ');
        if i > 0:
            return get_num_type(string[0 : i]);
        return get_num_type(string);
    except ValueError:
        return 0;
        

def get_num_type(string):
    string = string.replace(',', '');
    if '.' in string:
        return float(string);
    return int(string);

class Weight:
    weight = 0;
    approx = False;
    def __init__(self, weight):
        if weight != None:
            self.weight = self.parse_weight(weight);
    def parse_weight(self, weight):
        if (weight[0] == '~'):
            weight = weight[1:];
            approx = True;
        return get_amount(weight);
    def __str__(self):
        w = "";
        if self.approx:
            w += "~";
        w += str(self.weight);
        if self.weight == 1:
            w += " lb.";
        else:
            w += " lbs.";
        return w;

class Length:
    length = 0;
    def __init__(self, length):
        self.length = self.parse_length(length);
    def parse_length(self, string):
        return get_num_type(string[:string.find('\"')]);
    def __str__(self):
        return str(self.length) + "\"";

class Radius:
    radius = 0;
    def __init__(self, radius):
        self.radius = self.parse_radius(radius);
    def parse_radius(self, string):
        return get_num_type(string[:string.find('\"')]);
    def __str__(self):
        return str(self.radius) + "\" radius";

class Area:
    width = 0;
    height = 0;
    def __init__(self, area):
        self.width, self.height = self.parse_area(area);
    def parse_area(self, string):
        a = string[:string.find('\"')].split('x');
        return get_num_type(a[0]), get_num_type(a[1]);
    def __str__(self):
        return str(self.width) + "\" × " + str(self.height) + "\"";
