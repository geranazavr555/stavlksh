from collections import namedtuple

import requests
from bs4 import BeautifulSoup


Verdict = namedtuple("Verdict", ("result", "time"))
UserResult = namedtuple("UserResult", ("name", "tasks"))


class ContestData:
    def __init__(self, name, tasks, results):
        self.name = name
        self.tasks = tasks
        self.results = results

    @property
    def contestants(self):
        return [contestant.name for contestant in self.results]

    @property
    def task_count(self):
        return len(self.tasks)

    @property
    def metadata(self):
        return self.name, self.tasks

    def __str__(self):
        return "ContestData({}, {}, {})".format(self.name, self.tasks, self.results)


def get_verdict(node):
    if node.span is not None:
        time = node.span.text
        result = node.text.replace(time, "")
        return Verdict(result, time)
    else:
        result = node.text
        return Verdict(result, None)


def get_user_results(node):
    name = ""
    tasks = []
    for item in node:
        if "user" in item["class"]:
            name = item.text
        elif "task" in item["class"]:
            tasks.append(get_verdict(item.span))
    return UserResult(name, tuple(tasks))


def get_contest_metadata(root):
    title = root.find("span", {"class": "page-title"}).text
    title = title[:title.rfind("(")]
    tasks = []
    table_head = root.find_all("th")
    for item in table_head:
        if "task" in item["class"]:
            tasks.append(item.text)

    return title, tasks


def get_contest_results(root):
    standings = []
    rows = root.find_all("tr")
    for row in rows[1:]:
        standings.append(get_user_results(row))
    return tuple(standings)


def get_contest_information(contest_id):
    url = "http://contest.stavpoisk.ru/olympiad/{}/show-monitor".format(contest_id)
    html_content = requests.get(url).text
    html_content = "".join(html_content).replace('\n', '').replace('\t', '')
    root = BeautifulSoup(html_content, "lxml")

    metadata = get_contest_metadata(root)
    standings = get_contest_results(root)
    return ContestData(metadata[0], metadata[1], standings)


def count_contestant_score(x):
    tasks = x[1]
    tasks_solved = 0
    failure_attempts = 0
    for attempt in tasks:
        if "+" in attempt:
            tasks_solved += 1
            if len(attempt) > 1:
                failure_attempts += int(attempt[1:])
    score = 10000 * tasks_solved - failure_attempts
    return -score


def sort_summary_results(summary_results):
    return sorted(list(summary_results.items()), key=count_contestant_score)


def get_summary_results(*args):
    contests = [get_contest_information(contest) for contest in args]

    contestants = set()
    for contest in contests:
        contestants.update(contest.contestants)

    summary_results = {contestant: list() for contestant in contestants}
    for contestant in contestants:
        for contest in contests:
            if contestant in contest.contestants:
                for attempt in dict(contest.results)[contestant]:
                    summary_results[contestant].append(attempt.result)
            else:
                summary_results[contestant].extend(["."] * contest.task_count)

    contests_metadata = tuple(contest.metadata for contest in contests)

    return contests_metadata, sort_summary_results(summary_results)
