import fileinput


def main():
    # input_data = get_data_from_user()
    # perm_data = perm_construct(input_data)
    file_data = get_params_from_file()
    perm_data = perm_construct(file_data)
    cycle_data = count_cycle_data(perm_data)
    result = count_effort(cycle_data)

    return result


def get_params_from_file():
    params = []

    with fileinput.input() as f:
        str_values = [line.split() for line in f]

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
    n, weights, orig, perm = params

    for i in range(n):
        orig[i] -= 1

    perm_copy = perm.copy()
    for i in range(n):
        idx = perm_copy[i] - 1
        perm[idx] = orig[i]

    return n, weights, orig, perm


def count_cycle_data(params):
    n, weights, orig, perm = params
    odw = [False for _ in range(n)]
    min_weight = min(weights)
    cycle_data = []

    for i in range(n):
        if not odw[i]:
            min_weight_in_cycle = None
            weight_sum = 0
            idx = i
            cycle_length = 0

            while True:
                min_weight_in_cycle = weights[idx] if not min_weight_in_cycle \
                    else min(min_weight_in_cycle, weights[idx])
                weight_sum += weights[idx]
                idx = perm[idx]
                odw[idx] = True
                cycle_length += 1

                if idx == i:
                    break

            cycle_data.append((weight_sum, cycle_length, min_weight_in_cycle))

    return cycle_data, min_weight


def count_effort(params):
    result = 0
    min_weight = params[1]
    for i in range(len(params[0])):
        weight_sum, cycle_length, min_weight_in_cycle = params[0][i]

        method_1 = (weight_sum + ((cycle_length - 2) * min_weight_in_cycle))
        method_2 = (weight_sum + min_weight_in_cycle + ((cycle_length + 1) * min_weight))
        result += min(method_1, method_2)

    return result


if __name__ == "__main__":

    print(main())
