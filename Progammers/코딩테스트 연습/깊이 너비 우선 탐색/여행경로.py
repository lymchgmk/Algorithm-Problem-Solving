import collections
import copy


def solution(tickets):
    def DFS(start, route):
        if len(route) == len(tickets)+1:
            return route
        
        for idx, airport in enumerate(ticket_dict[start]):
            ticket_dict[start].pop(idx)
            
            route_copy = copy.deepcopy(route)
            route_copy.append(airport)
            
            try_DFS = DFS(airport, route_copy)
            if try_DFS:
                return try_DFS
            else:
                ticket_dict[start].insert(idx, airport)
            
    ticket_dict = collections.defaultdict(list)
    for s, e in tickets:
        ticket_dict[s].append(e)
    for key in ticket_dict:
        ticket_dict[key].sort()

    return DFS('ICN', ['ICN'])


tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))