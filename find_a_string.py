def count_substring(string, substring):
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            count += 1
    return count


string = input().strip()
substring = input().strip()

print(count_substring(string, substring))