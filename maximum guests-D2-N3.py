def maxGuests(T, E, L):
    guests = [0] * (T + 1)
    for i in range(T):
        guests[E[i]] += 1
        guests[L[i]] -= 1
    max_guests = guests[0]
    for i in range(1, T + 1):
        guests[i] += guests[i - 1]
        max_guests = max(max_guests, guests[i])
    return max_guests
