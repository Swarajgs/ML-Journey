# 🗳️ Majority Element Finder

Welcome! This project shows you how to quickly find the majority element in an array—that’s the one that appears more than half the time. We use an elegant and efficient method called the **Boyer–Moore Majority Vote Algorithm**.

---

## What’s the Problem?

Given a list of numbers like `[2, 2, 1, 1, 1, 2, 2]`, can you find which number occurs more than $n/2$ times?  
Spoiler: It’s `2` in the example above!  
You’re guaranteed that such a number always exists in the data.

---

## Why Should You Care?

This problem is a classic—interviewers love it, and it comes up often when dealing with data streams or voting data. The trick is to solve it super fast and *without* using tons of memory.

---

## How Does the Algorithm Work?

Think of it as voting—every time you see your “candidate,” they get a vote. If you see someone else, your candidate loses a vote. When your candidate runs out of votes, you pick a new one.

Here’s the idea, step by step:

1. Start with no candidate and zero votes.
2. Go through each number:
    - If you’re out of votes, pick the current number as your new candidate.
    - If the current number is the candidate, up the vote.
    - Otherwise, down the vote.
3. At the end, whoever is left standing is the real majority!

---

## Python Code (Short and Sweet)

```python
def majorityElement(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
```

---

## Walkthrough Example

Let’s watch the algorithm in action on `[2, 2, 1, 1, 1, 2, 2]`:

| Step | Number | Candidate | Votes | What Happens         |
|------|--------|-----------|-------|----------------------|
| 1    | 2      | none      | 0     | Pick as candidate    |
| 2    | 2      | 2         | 1     | Votes go up          |
| 3    | 1      | 2         | 2     | Votes go down        |
| 4    | 1      | 2         | 1     | Votes go down        |
| 5    | 1      | 2         | 0     | Out of votes, pick 1 |
| 6    | 2      | 1         | 1     | Votes go down        |
| 7    | 2      | 1         | 0     | Out of votes, pick 2 |

At the end, `2` is left standing—so that's your answer!

---

## How Fast Is It?

- **Time:** Only one sweep through the list ⇒ $O(n)$
- **Space:** No extra lists or hash maps ⇒ $O(1)$

It’s blazing fast and super memory-efficient.

---

## Good to Know

If the input *might* not have a majority, you should double-check your candidate with a final pass. Here, it's always there, so you're safe!

---

## Useful Links

- Boyer–Moore Majority Vote Algorithm on Wikipedia
- LeetCode 169: Majority Element

---

## License

MIT. Do anything you’d like—just give credit!

---

*Happy coding! If you have questions or want to suggest changes, feel free to open an issue or PR.*
