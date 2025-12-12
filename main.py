"""Module to calculate minimum connection loss using a heap-based approach."""
import heapq


def connect_for_min_loss(data: list[int]) -> int:
    """Function to calculate the minimum connection loss.
    Args:
        data (list): List of integers representing connection losses.
    Returns:
        int: Minimum total connection loss."""

    if not all(isinstance(i, int) for i in data):
        raise ValueError("All elements in the input list must be integers.")
    if len(data) < 2:
        return sum(data)

    tot_loss = []
    heapq.heapify(data)
    while len(data) > 2:
        val = heapq.heappop(data)
        val1 = heapq.heappop(data)
        tot_loss.append(val+val1)
        heapq.heappush(data, val+val1)

    tot_loss.append(sum(data))
    return sum(tot_loss)


# Example usage
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print(f"Minimum connection loss = {connect_for_min_loss(arr)}")
