def majority_vote(mturk_res):
    votes = []
    for i in range(0, len(mturk_res), 3):
        attr_id = mturk_res['Input.attr_id'][i]
        for j in range(1, 11):
            adj = mturk_res['Input.adj_%s' % j][i]
            ans1 = 1 if mturk_res['Answer.adj_%s' % j][i] == 'Yes' else 0 
            ans2 = 1 if mturk_res['Answer.adj_%s' % j][i+1] == 'Yes' else 0 
            ans3 = 1 if mturk_res['Answer.adj_%s' % j][i+2] == 'Yes' else 0
            maj_opn = ans1 + ans2 + ans3 >= 2
            votes.append((attr_id, adj, maj_opn))

    return sorted(votes, key=lambda tup: (tup[0], tup[1], tup[2]))
