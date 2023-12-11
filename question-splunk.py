'''
Suppose we have an unsorted log file of accesses to web resources. Each log entry consists of an access time, the ID of the user making the access, and the resource ID. 

The access time is represented as seconds since 00:00:00, and all times are assumed to be in the same day.

For example:
logs1 = [
    ["200", "user_1", "resource_5"],
    ["3", "user_1", "resource_1"],
    ["620", "user_1", "resource_1"],
    ["620", "user_3", "resource_1"],
    ["34", "user_6", "resource_2"],
    ["95", "user_9", "resource_1"],
    ["416", "user_6", "resource_1"],
    ["58523", "user_3", "resource_1"],
    ["53760", "user_3", "resource_3"],
    ["58522", "user_22", "resource_1"],
    ["100", "user_3", "resource_6"],
    ["400", "user_6", "resource_2"],
]


We would like to compute user sessions, specifically: write a function that takes the logs and returns a data structure that associates to each user their earliest and latest access times.

Example:
{'user_6': [34, 416],
 'user_1': [3, 620],
 'user_9': [95, 95],
 'user_22': [58522, 58522],
 'user_3': [100, 58523],
}


Example 2:
logs2 = [
    ["357", "user", "resource_2"],
    ["1262", "user", "resource_1"],
    ["1462", "user", "resource_2"],
    ["1060", "user", "resource_1"],
    ["756", "user", "resource_3"],
    ["1090", "user", "resource_3"],
]

Should return:
{'user': [357, 1462]}

Example 3:
logs3 = [
    ["300", "user_10", "resource_5"]
]

Should return:
{'user_10': [300, 300]}

Example 4:

logs4 = [
    ["1", "user_96", "resource_5"],
    ["1", "user_10", "resource_5"],
    ["301", "user_11", "resource_5"],
    ["301", "user_12", "resource_5"],
    ["603", "user_12", "resource_5"],
    ["1603", "user_12", "resource_7"],
]

Should return:
{
 'user_96': [1, 1],
 'user_10': [1, 1],
 'user_11': [301, 301],
 'user_12': [301, 1603],
}

logs5 = [
    ["300", "user_1", "resource_3"],
    ["599", "user_1", "resource_3"],
    ["900", "user_1", "resource_3"],
    ["1199", "user_1", "resource_3"],
    ["1200", "user_1", "resource_3"],
    ["1201", "user_1", "resource_3"],
    ["1202", "user_1", "resource_3"]
]

Should return:
{'user_1': [300, 1202]}

All Test Cases:
user_sessions(logs1)
user_sessions(logs2)
user_sessions(logs3)
user_sessions(logs4)
user_sessions(logs5)

Complexity analysis variables:

n: number of logs in the input
'''
logs1 = [
    ["200", "user_1", "resource_5"],
    ["3", "user_1", "resource_1"],
    ["620", "user_1", "resource_1"],
    ["620", "user_3", "resource_1"],
    ["34", "user_6", "resource_2"],
    ["95", "user_9", "resource_1"],
    ["416", "user_6", "resource_1"],
    ["58523", "user_3", "resource_1"],
    ["53760", "user_3", "resource_3"],
    ["58522", "user_22", "resource_1"],
    ["100", "user_3", "resource_6"],
    ["400", "user_6", "resource_2"],
]

logs2 = [
    ["357", "user", "resource_2"],
    ["1262", "user", "resource_1"],
    ["1462", "user", "resource_2"],
    ["1060", "user", "resource_1"],
    ["756", "user", "resource_3"],
    ["1090", "user", "resource_3"],
]

logs3 = [
    ["300", "user_10", "resource_5"],
]

logs4 = [
    ["1", "user_96", "resource_5"],
    ["1", "user_10", "resource_5"],
    ["301", "user_11", "resource_5"],
    ["301", "user_12", "resource_5"],
    ["603", "user_12", "resource_5"],
    ["1603", "user_12", "resource_7"],
]

logs5 = [
    ["300", "user_1", "resource_3"],
    ["599", "user_1", "resource_3"],
    ["900", "user_1", "resource_3"],
    ["1199", "user_1", "resource_3"],
    ["1200", "user_1", "resource_3"],
    ["1201", "user_1", "resource_3"],
    ["1202", "user_1", "resource_3"]
]


def get_logs(logs1):
    value = {}
    for log in logs1:
        print(log[1])
        value[log[1]] = [min(log[0]),max(log[0])]
        
        
        
    print(value)
    
get_logs(logs1)

