import measurements as ms;

class Item:
    name = "";
    weight = 0.0;
    cost = 0;
    properties = [];
    components = [];
    def __init__(self, title, components, weight, cost):
        self.name, self.properties = self.parse_properties(title);
        self.weight = ms.Weight(weight);
        self.cost = ms.get_amount(cost);
        self.components = self.parse_components(components);
    def parse_properties(self, string):
        i = string.find('(');
        if i > 0:
            prop = string[i + 1 : -1];
            return string[0 : i - 1], prop.split("; ");
        return string, [];
    def parse_components(self, string):
        c = string.split("\n");
        comp = [];
        temp = [];
        head = "";
        for i in range(0, len(c)):
            if c[i] != "OR":
                if len(c[i]) > 0:
                    k = c[i];
                    tail = False;
                    if i > 1:
                        if c[i - 1] == "OR":
                            k = head[:head.find(' ')] + " " + k;
                            tail = True;
                    if not tail:
                        head = k;
                        if len(temp) > 0:
                            comp.append(temp);
                        temp = [];
                    temp.append(Component(k));
                    print(temp[-1]);
        if len(temp) > 0:
            if len(comp) > 0:
                if comp[-1] != temp:
                    comp.append(temp);
            else:
                comp.append(temp);
        return comp;

class Component:
    name = "";
    size = 0;
    weight = 0.0;
    amount = 0;
    def __init__(self, title):
        self.name, self.weight, self.size, self.amount = self.parse_properties(title);
    def parse_properties(self, string):
        i = string.find('(');
        a = string.find(' ');
        try:
            amount = int(string[:a]);
            first = a + 1;
        except ValueError:
            amount = 1;
            first = 0;
        if i > 0:
            prop = string[i + 1 : -1].split(", ");
            weight = None;
            size = None;
            for p in prop:
                if size == None:
                    if "\" radius" in p:
                        size = ms.Radius(p);
                    elif '\"' in p:
                        if 'x' in p:
                            size = ms.Area(p);
                        else:
                            size = ms.Length(p);
                if weight == None:
                    if " lb" in p:
                        weight = p;
            return string[first : i - 1], ms.Weight(weight), size, amount;
        return string[first:], ms.Weight(None), 0, amount;
    def __str__(self):
        return self.name + " (" + str(self.size) + "; " + str(self.weight) + ") × " + str(self.amount);

athame = Item(
    "Athame (1d4 S, P; finesse)",
    "2 straight blade (0.5 lb, 10\")\n3 carved handle (0.5 lb, 5\")",
    "1 lb.",
    "10 gp");
ballAndChain = Item(
    "Ball and Chain (3d12 B; reach, grappling, spiked, windup 2)",
    "1 heavy ball (3 lbs, 6\" radius)\nOR spiked ball (3 lbs, 6\" radius)\n1 heavy chain (4 lbs, 120\")\n1 weighted pommel (3 lbs, 15\")",
    "13 lb.",
    "100 gp");
heavyShield = Item(
    "Ball and Chain (3d12 B; reach, grappling, spiked, windup 2)",
    "1 wooden plate (6.5 lbs, 15\" radius)\nOR metal plate (6.5 lbs, 15\" radius)\n1 metal strip (1.5 lbs)",
    "8 lb.",
    "25 gp");
TowerShield = Item(
    "Tower Shield (+6 AC; giant)",
    "1 wooden plate (10 lbs, 30x60\")\nOR metal plate (10 lbs, 30x60\")\n1 metal strip (3 lbs)",
    "13 lb.",
    "200 gp");
