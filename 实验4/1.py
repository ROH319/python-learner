import random
def has_duplicate_birthdays():
    birthdays = [random.randint(1, 365) for _ in range(23)]
    return len(set(birthdays)) != len(birthdays)

def calculate_probability(sample_size):
    count = 0
    for _ in range(sample_size):
        if has_duplicate_birthdays():
            count = count + 1
    return count / sample_size


#不同的随机样本数量
sample_sizes = [100, 1000, 10000, 100000]

for size in sample_sizes:
    probability = calculate_probability(size)
    print(f"当样本数量为 {size} 时，23 个人中至少两个人生日相同的概率为: {probability:.4f}")
