def majority_votes(batch_results_df, num_tweets_per_worker):
    tweet_votes = dict()
    for i in range(len(batch_results_df)):
        for j in range(1, 1 + num_tweets_per_worker):
            tweet = batch_results_df['Input.tweet%s' % j][i]
            if tweet not in tweet_votes:
                tweet_votes[tweet] = [0, 0, 0]

            if batch_results_df['Answer.checkboxes.Remain%s' % j][i]:
                tweet_votes[tweet][0] += 1
            elif batch_results_df['Answer.checkboxes.Remove%s' % j][i]:
                tweet_votes[tweet][1] += 1
            elif batch_results_df['Answer.checkboxes.Warning%s' % j][i]:
                tweet_votes[tweet][2] += 1

    maj_dec = dict()
    for tweet in tweet_votes:
        index_max = np.argmax(tweet_votes[tweet])
        if index_max == 0:
            maj_dec[tweet] = 'Remain'
        elif index_max == 1:
            maj_dec[tweet] = 'Remove'
        else:
            maj_dec[tweet] = 'Warning'
   
    return maj_dec

maj_decisions = majority_votes(batch_results_df, 4)
maj_decisions
