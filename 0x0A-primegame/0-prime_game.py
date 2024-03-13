#!/usr/bin/python3
"""Prime game script
"""

def isWinner(x, nums):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(limit):
        primes = []
        for i in range(2, limit + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def remove_multiples(nums, prime):
        for i in range(prime, len(nums), prime):
            nums[i] = 0

    def play_round(nums):
        primes = get_primes(nums[-1])
        for i, num in enumerate(nums):
            if num > 1 and is_prime(num):
                remove_multiples(nums, num)
                break

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        current_nums = list(range(1, n + 1))
        for _ in range(x):
            play_round(current_nums)
        if 0 in current_nums:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins == ben_wins:
        return None
    return "Maria" if maria_wins > ben_wins else "Ben"
