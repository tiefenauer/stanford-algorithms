class Job(object):
    def __init__(self, i, w, l):
        self.i = i
        self.w = w
        self.l = l

    @property
    def score(self):
        return self.w / self.l

    def __lt__(self, other):
        return self.score > other.score

    def __repr__(self):
        return str((self.score, self.w, self.l))


if __name__ == '__main__':
    filename = 'jobs.txt'
    # filename = 'sample_jobs.txt'
    with open(filename, 'r') as f:
        lines = f.readlines()
        n_jobs = int(lines[0])
        jobs = []
        for i, line in enumerate(lines[1:], 1):
            w, l = line.split()
            jobs.append(Job(i, float(w), float(l)))

        jobs.sort()
        print(jobs)
        completion_time = 0
        s = 0
        for job in jobs:
            completion_time += job.l
            s += job.w * completion_time
        print(s)
