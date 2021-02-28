def main():
    input_data = get_data_from_user()
    #  input_file = input()
    #  file_data = get_params_from_file(input_file)
    perm_data = perm_construct(input_data)
    cycle_data = count_cycle_data(perm_data)
    result = count_effort(cycle_data)

    return result


def get_params_from_file(input_file):
    params = []

    with open(input_file, 'r') as f:

        content = f.read().splitlines()
        str_values = [line.split() for line in content]

        for line in str_values:
            line = [int(element) for element in line]
            params.append(line)

    params[0] = int(params[0][0])

    return params


def get_data_from_user():
    n = int(input())
    weights = [int(num) for num in input().split()]
    orig = [int(num) for num in input().split()]  # original
    perm = [int(num) for num in input().split()]  # permutation

    return n, weights, orig, perm


def perm_construct(params):
    n, m, orig, perm = params

    for i in range(n):
        orig[i] -= 1

    perm_copy = perm.copy()
    for i in range(n):
        idx = perm_copy[i] - 1
        perm[idx] = orig[i]

    return n, m, orig, perm


def count_cycle_data(params):
    n, m, orig, perm = params
    odw = [False for _ in range(n)]
    min_weight = min(m)  # min weight
    cycle_data = []

    for i in range(n):
        if not odw[i]:
            min_c = None  # min weight in cycle
            weight_sum = 0
            idx = i
            c = 0  # cycle length

            while True:
                min_c = m[idx] if not min_c else min(min_c, m[idx])
                weight_sum += m[idx]
                idx = perm[idx]
                odw[idx] = True
                c += 1

                if idx == i:
                    break

            cycle_data.append((weight_sum, c, min_c))

    return cycle_data, min_weight


def count_effort(params):
    result = 0
    min_weight = params[1]
    for i in range(len(params[0])):
        weight_sum, c, min_c = params[0][i]

        met_1 = (weight_sum + ((c - 2) * min_c))
        met_2 = (weight_sum + min_c + ((c + 1) * min_weight))
        result += min(met_1, met_2)

    return result


if __name__ == "__main__":

    print(main())

