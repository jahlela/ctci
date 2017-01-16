
def merge_times(times):
    """
    IN: times, an array of tuples with meeting start and end times
    OUT: an array of tuples, which represent periods of unavailability (meerged meetings)

    >>> times =  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    >>> merge_times(times)
    [(0, 1), (3, 8), (9, 10)]
    """

    sorted_times = sorted(times)
    merged_times  = [sorted_times[0]]

    for idx in range(1,len(times)-1):

        meeting1 = merged_times[-1]
        start1, end1 = meeting1
        
        meeting2 = sorted_times[idx]
        start2, end2 = meeting2
        
        if start2 <= end1:
            new_end = max(end1, end2)
            new_time = (start1, new_end)
            merged_times[-1] = new_time

        else:
            merged_times.append(meeting2)

    return merged_times

times =  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
print merge_times(times)
