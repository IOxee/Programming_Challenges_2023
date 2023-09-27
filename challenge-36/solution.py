# Name: PERMUTACIONES 
# Path: solution.py
# Author: IOxee
# TimeStamp: 27-09-2023 14:12:44

def test_generate_permutations(func):
    test_cases = [
        {'input': 'sol', 'expected': {'sol', 'slo', 'osl', 'ols', 'los', 'lso'}},
        {'input': 'abc', 'expected': {'abc', 'acb', 'bac', 'bca', 'cab', 'cba'}},
        {'input': 'a', 'expected': {'a'}},
        {'input': '', 'expected': {''}}
    ]
    
    results = []
    for i, test_case in enumerate(test_cases):
        output_set = set()
        def capture_output(word):
            nonlocal output_set
            output_set.add(word)
        
        func(test_case['input'], capture_output)
        
        is_passed = output_set == test_case['expected']
        results.append({
            'test_case': i + 1,
            'passed': '✅' if is_passed else '❌',
            'input': test_case['input'],
            'result': output_set,
            'expected': test_case['expected']
        })
    
    print("\n🔥 Test Results 🔥\n")
    for res in results:
        print(f"Test Case {res['test_case']}: {res['passed']}")
        print(f"  Input: {res['input']}")
        print(f"  Result: {res['result']}")
        print(f"  Expected: {res['expected']}\n")

def generate_permutations_with_callback(word: str, callback: callable) -> None:
    def backtrack(start=0):
        if start == len(word):
            callback(''.join(word))
            return
        for i in range(start, len(word)):
            word[start], word[i] = word[i], word[start]
            backtrack(start + 1)
            word[start], word[i] = word[i], word[start]

    word = list(word)
    backtrack()

test_generate_permutations(generate_permutations_with_callback)
