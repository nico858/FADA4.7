programs = [1, 2, 3]
weights = [2, 1, 3]
disc_capacity = 5

def max_programas_recursive (programs, weights, discCapacity):
    if len(programs) == 0 or discCapacity == 0:
        return 0
    
    if weights[0] > discCapacity:
        return max_programas_recursive(programs[1:], weights[1:], discCapacity)
    
    add = weights[0] + max_programas_recursive(programs[1:], weights[1:], discCapacity - weights[0])
    not_add = max_programas_recursive(programs[1:], weights[1:], discCapacity)

    return max(add, not_add)

print(f'Recursiva {max_programas_recursive(programs, weights, disc_capacity)}')

def max_programs_iterative(programas, pesos, capacidad):
    n = len(programas)
    dp = [[0] * (capacidad + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(capacidad + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif pesos[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                incluir = weights[i - 1] + dp[i - 1][j - pesos[i - 1]]
                excluir = dp[i - 1][j]
                dp[i][j] = max(incluir, excluir)

    return dp[n][capacidad]

print(f'Iterativa {max_programs_iterative(programs, weights, disc_capacity)}')


def max_programs_memoized(programs, weights, disc_capacity):
    n = len(programs)
    memo = [[-1] * (disc_capacity + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(disc_capacity + 1):
            if i == 0 or j == 0:
                memo[i][j] = 0
            elif weights[i - 1] > j:
                memo[i][j] = memo[i - 1][j]
            else:
                incluir = weights[i - 1] + memo[i - 1][j - weights[i - 1]]
                excluir = memo[i - 1][j]
                memo[i][j] = max(incluir, excluir)

    return memo[n][disc_capacity]


print(f'Memoized {max_programs_memoized(programs, weights, disc_capacity)}')