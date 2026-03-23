votes = {"A": 0, "B": 0}
voted_users = set()

def cast_vote(user_id, candidate):
    """Cast a vote for a candidate"""
    if user_id in voted_users:
        return f"Error: User {user_id} has already voted."
    
    if candidate not in votes:
        return f"Error: {candidate} is not a valid candidate."
    
    votes[candidate] += 1
    voted_users.add(user_id)
    return f"Vote cast for {candidate}."

def show_winner():
    """Display the winner"""
    if not votes or all(v == 0 for v in votes.values()):
        return "No votes cast yet."
    
    winner = max(votes, key=votes.get)
    max_votes = votes[winner]
    return f"Winner: {winner} with {max_votes} votes"

def show_results():
    """Display all vote counts"""
    return f"Current votes: {votes}"

# Example usage
print(cast_vote("user1", "A"))
print(cast_vote("user2", "B"))
print(cast_vote("user1", "B"))  # Duplicate vote attempt
print(show_results())
print(show_winner())