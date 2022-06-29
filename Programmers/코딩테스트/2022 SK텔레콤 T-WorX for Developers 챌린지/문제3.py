def solution(n, plans, clients):
    answer = []
    plans, clients = setPlans(plans), setClients(clients)
    for client in clients:
        answer.append(getPlanNum(client, plans))
    return answer

def setPlans(plans):
    result = []
    service_set = set()
    for plan in plans:
        data, *services = map(int, plan.split(" "))
        service_set.update(services)
        result.append([data, service_set.copy()])
    return result

def setClients(clients):
    result = []
    for client in clients:
        data, *services = map(int, client.split(" "))
        result.append([data, set(services)])
    return result

def getPlanNum(client, plans):
    num = 0
    for idx, plan in enumerate(plans, start=1):
        if client[0] <= plan[0] and client[1].issubset(plan[1]):
            return idx
    return num


if __name__ == "__main__":
    print(solution())