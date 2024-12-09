from flask import Flask, jsonify, request

app = Flask(__name__)

# Initial video titles list
video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

def binary_search(arr, target):
    """
    Implement binary search to find a video title
    Returns index if found, -1 if not found
    """
    # First, sort the array since binary search requires sorted array
    arr = sorted(arr)
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        # Convert both strings to lowercase for case-insensitive comparison
        if arr[mid].lower() == target.lower():
            return mid
        elif arr[mid].lower() < target.lower():
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def merge_sort(arr):
    """
    Implement merge sort algorithm to sort video titles
    """
    if len(arr) <= 1:
        return arr
    
    # Divide array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    """
    Helper function to merge two sorted arrays
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i].lower() <= right[j].lower():
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

@app.route('/search', methods=['GET'])
def search_video():
    """
    API endpoint to search for a video using binary search
    """
    query = request.args.get('title', '')
    if not query:
        return jsonify({"error": "Please provide a title to search"}), 400
    
    # Create a sorted copy of video titles for binary search
    sorted_titles = sorted(video_titles)
    index = binary_search(sorted_titles, query)
    
    if index != -1:
        return jsonify({
            "message": "Video found",
            "video": sorted_titles[index]
        })
    else:
        return jsonify({
            "message": "Video not found"
        }), 404

@app.route('/sort', methods=['GET'])
def sort_videos():
    """
    API endpoint to get sorted list of videos using merge sort
    """
    sorted_videos = merge_sort(video_titles.copy())
    return jsonify({
        "message": "Videos sorted successfully",
        "videos": sorted_videos
    })

# Test the implementation
if __name__ == "__main__":
    # Test binary search
    print("Testing Binary Search:")
    test_title = "The Art of Coding"
    sorted_titles = sorted(video_titles)
    result = binary_search(sorted_titles, test_title)
    print(f"Searching for '{test_title}': {'Found' if result != -1 else 'Not Found'}")
    
    # Test merge sort
    print("\nTesting Merge Sort:")
    print("Original list:", video_titles)
    sorted_list = merge_sort(video_titles.copy())
    print("Sorted list:", sorted_list)
    
    # Run Flask app
    app.run(debug=True, port=5000)
