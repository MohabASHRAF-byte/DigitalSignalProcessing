from Correlation import cross_correlation
from utilities import ReadSignalValues


def load(clss_name: str, num):
    clss = []
    for i in range(1, 6):
        s = ReadSignalValues(f"Tests/Task6/TemplateMatching/Class{num}/{clss_name}{i}.txt")
        clss.append(s)
    return clss


class TemplateMatching:

    def __init__(self):
        self.upSamples = load("down", 1)
        self.downSamples = load("up", 2)

    def CalcClssProbability(self, s, clss):
        acc = 0
        for signal in clss:
            corr = cross_correlation(s, signal)
            acc += max(abs(x) for x in corr.values())
        return acc / clss[-1].len

    def classify(self, s1):

        belong_up = self.CalcClssProbability(s1, self.upSamples)
        belong_down = self.CalcClssProbability(s1, self.downSamples)
        if belong_up > belong_down:
            return "up"
        return "down"
