def reverse_a_list(li: list) -> str:
    # Type your code here
    out = ""
    for l in li[::-1]:
        out += f"{l} "
    return out.strip()


if __name__ == '__main__':
    a = [1, 4, 3, 2]
    print(reverse_a_list(a))
