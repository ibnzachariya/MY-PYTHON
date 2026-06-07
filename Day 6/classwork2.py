def auction_system():
    bids = {}
    while True:
        name = input("Enter engineer's name: ")
        bid = int(input("Enter your bid amount: "))
        bids[name] = bid

        more = input("Are there more bidders? (yes/no): ").lower()
        if more == "no":
            break

    # Find highest bidder
    highest_bid = 0
    winner = ""
    for bidder in bids:
        if bids[bidder] > highest_bid:
            highest_bid = bids[bidder]
            winner = bidder

    print(f"The winner is {winner} with a bid of {highest_bid}.")

    # Track equipment status
    status = input("Enter equipment status (working/faulty): ")
    bids[winner] = {"bid": highest_bid, "status": status}

    print(f"Winner: {winner}, Bid: {highest_bid}, Equipment Status: {status}")


auction_system()
