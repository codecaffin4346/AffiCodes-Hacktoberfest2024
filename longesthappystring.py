import heapq

def longestHappyString(a: int, b: int, c: int) -> str:
    # Max-heap to store the counts of 'a', 'b', and 'c'
    heap = []
    
    # Push counts of 'a', 'b', and 'c' to the heap with negative values (to simulate max-heap)
    if a > 0:
        heapq.heappush(heap, (-a, 'a'))
    if b > 0:
        heapq.heappush(heap, (-b, 'b'))
    if c > 0:
        heapq.heappush(heap, (-c, 'c'))
    
    result = []
    
    while heap:
        # Pop the most frequent character
        count1, char1 = heapq.heappop(heap)
        
        # Check if we can add this character without violating the "no three in a row" rule
        if len(result) >= 2 and result[-1] == result[-2] == char1:
            # If the top character would make three consecutive characters, check the next one
            if not heap:
                break  # No more characters available to add, so we are done
            
            count2, char2 = heapq.heappop(heap)
            result.append(char2)
            count2 += 1  # Reduce count of char2
            
            # Push char2 back if it still has remaining occurrences
            if count2 != 0:
                heapq.heappush(heap, (count2, char2))
            
            # Push char1 back for future consideration
            heapq.heappush(heap, (count1, char1))
        
        else:
            # Append char1 to the result
            result.append(char1)
            count1 += 1  # Reduce count of char1
            
            # Push char1 back if it still has remaining occurrences
            if count1 != 0:
                heapq.heappush(heap, (count1, char1))
    
    return ''.join(result)


